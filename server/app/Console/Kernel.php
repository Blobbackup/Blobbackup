<?php

namespace App\Console;

use App\Models\Computer;
use App\Models\User;
use App\Util\Util;
use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;
use Symfony\Component\Process\Process;
use Illuminate\Support\Facades\Http;

class Kernel extends ConsoleKernel
{
    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
        $schedule->call(function () {
            foreach (User::whereNull('leader_id')->whereNotNull('email_verified_at')->get() as $user) {
                if ($user->subscribed()) {
                    $subscription = $user->subscription();
                    $amount = Util::$perComputerPrice * $user->computersToBill();
                    foreach ($subscription->modifiers() as $modifier)
                        $modifier->delete();
                    $subscription->newModifier($amount)->create();
                } else if ($user->customer->trial_ends_at->diff(new \DateTime())->days == 3) {
                    if (new \DateTime() < $user->customer->trial_ends_at) {
                        Util::sendEmail($user->email,
                            "Your Blobbackup Trial Will Expire In 3 Days!",
                            "Your Blobbackup trial will expire in 3 days. Please sign in and add a payment method if you'd like to continue using the service after the trial expires. Note that 3 days after your trial expires, all your computer backups will be deleted.");
                    } else {
                        $user->deleteComputers();
                    }
                } else if ($user->customer->trial_ends_at->diff(new \DateTime())->days == 0) {
                    Util::sendEmail($user->email,
                        "Your Data Will Be Deleted In 3 Days.",
                        "Your Blobbackup trial has expired. Please sign in and add a payment method if you'd like to continue using the service. Note that 3 days from today, all your computer backups will be deleted.");
                }
            }
        })->daily();
        $schedule->call(function () {
            foreach (Computer::all() as $computer) {
                $last_backed_up = $computer->last_backed_up_at;
                if ($last_backed_up) {
                    $delta = $last_backed_up->diff(new \DateTime());
                    if ($delta->y == 0 && $delta->m == 0 && $delta->d >= 14 && $delta->d <= 16) {
                        Util::sendEmail($computer->user->email,
                            "Computer Not Backed up for 14 Days!",
                            "It's been more than 14 days since we've backed up your computer <b>" . $computer->name . "</b>.");
                        if ($computer->user->leader_id)
                            Util::sendEmail(User::find($computer->user->leader_id)->email,
                                "Computer Not Backed up for 14 Days!",
                                "It's been more than 14 days since we've backed up " . $computer->user->email . "'s computer <b>" . $computer->name . "</b>.");
                    }
                }
            }
        })->daily();
        $schedule->call(function () {
            foreach (Computer::onlyTrashed()->get() as $computer) {
                $delta = $computer->deleted_at->diff(new \DateTime());
                if ((!$computer->user || $delta->days > 30) || env('APP_ENV') == 'local') {
                    $path = 'b2:' . env('B2_BUCKET_NAME') . '/' . $computer->uuid;

                    // Delete repo contents
                    $process = new Process(['rclone', 'purge', $path]);
                    $process->run();

                    // Delete repo b2 key
                    $authResponse = Http::withBasicAuth(env('B2_KEY_ID'), env('B2_APPLICATION_KEY'))
                        ->get('https://api.backblazeb2.com/b2api/v2/b2_authorize_account');
                    $authJson = $authResponse->json();
                    Http::withHeaders(['Authorization' => $authJson['authorizationToken']])
                        ->post($authJson['apiUrl'] . '/b2api/v2/b2_delete_key',
                        ['applicationKeyId' => $computer->b2_key_id]);

                    // Delete computer from db
                    $computer->forceDelete();
                }
            }
        })->everyMinute();
    }

    /**
     * Register the commands for the application.
     *
     * @return void
     */
    protected function commands()
    {
        $this->load(__DIR__.'/Commands');

        require base_path('routes/console.php');
    }
}
