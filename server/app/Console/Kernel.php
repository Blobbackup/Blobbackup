<?php

namespace App\Console;

use App\Models\Computer;
use App\Models\User;
use App\Util\Util;
use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;
use Symfony\Component\Process\Process;

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
            $price = 10.00;
            foreach (User::all() as $user) {
                if ($user->subscribed()) {
                    $subscription = $user->subscription();
                    $amount = $price * $user->computers->count();
                    foreach ($subscription->modifiers() as $modifier)
                        $modifier->delete();
                    $subscription->newModifier($amount)->create();
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
                    }
                }
            }
        })->daily();
        $schedule->call(function () {
            foreach (Computer::onlyTrashed()->get() as $computer) {
                $path = 'b2:' . env('B2_BUCKET_NAME') . '/' . $computer->uuid;
                $process = new Process(['rclone', 'purge', $path]);
                $process->run();
                $computer->forceDelete();
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
