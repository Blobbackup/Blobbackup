<?php

use App\Util\Util;
use App\Models\Computer;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\Rules\Password;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Validator;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::get('/client/version', function () {
    return Util::$clientVersion;
});

Route::middleware(['auth.basic', 'active'])->group(function () {
    Route::get('/login', function () {
        $user = auth()->user();
        $leader = $user->leader_id ? User::find($user->leader_id) : $user;
        return [
            'on_trial' => $leader->onTrial(),
            'subscribed' => $leader->subscribed()
        ];
    });

    Route::middleware(['subscribed'])->group(function () {
        Route::post('/computers', function (Request $request, Response $response) {
            if (Validator::make($request->all(), [
                'name' => ['required', 'string', 'max:255'],
                'operating_system' => ['required', 'string', 'max:255']
            ])->fails())
                return $response->setStatusCode(400);
            
            // Create backblaze credentials
            $authResponse = Http::withBasicAuth(env('B2_KEY_ID'), env('B2_APPLICATION_KEY'))
                ->get('https://api.backblazeb2.com/b2api/v2/b2_authorize_account');
            if ($authResponse->status() != 200)
                return $response->setStatusCode(400);
            $uuid = Str::uuid()->toString();
            $authJson = $authResponse->json();
            $createKeyResponse = Http::withHeaders(['Authorization' => $authJson['authorizationToken']])
                ->post($authJson['apiUrl'] . '/b2api/v2/b2_create_key', [
                    'keyName' => $uuid, 'namePrefix' => $uuid, 'bucketId' => env('B2_BUCKET_ID'), 'accountId' => env('B2_ACCOUNT_ID'),
                    'capabilities' => ['listFiles', 'readFiles', 'writeFiles', 'deleteFiles', 'listBuckets']]);
            if ($createKeyResponse->status() != 200)
                return $response->setStatusCode(400);
    
            // Create computer
            $user = auth()->user();
            $createKeyJson = $createKeyResponse->json();
            $computer = new Computer();
            $computer->name = $request->name;
            $computer->uuid = $uuid;
            $computer->operating_system = $request->operating_system;
            $computer->b2_key_id = $createKeyJson['applicationKeyId'];
            $computer->b2_application_key = $createKeyJson['applicationKey'];
            $computer->user_id = $user->id;
            $computer->save();
            $computer->b2_bucket_name = env('B2_BUCKET_NAME');

            $firstComputer = $user->computers->count() == 1;
            if ($firstComputer) {
                Util::sendNotification($user->email . ' added first computer.');
                Util::sendEmailFrom(
                    'Bimba from Blobbackup',
                    $user->email,
                    'Welcome to Blobbackup - Let me know if I can help',
                    "<p>Hi there,</p><p>Thanks for trying out Blobbackup! My name is Bimba and I'm here to help you keep your computer data safe. If you ever have any questions or need assistance, you can always reach me by replying to this email.</p><p><b>Sit Back and Relax</b></p><p>Depending on your upload speeds, backups can take a while. Don't worry, you're on your way to backup peace of mind. You can turn off your computer at any time and Blobbackup will resume right where it left off when it's back on and connected to the internet.</p><p><b>Backup All Data</b></p><p>Notice how easy it was to get set up? Blobbackup ensures you don't have to worry about what gets backed up because we do it for you. (Learn more about <a href='https://blobbackup.com/support/what-is-being-backed-up/'>what gets backed up</a>).</p><p><b>Easy Restores</b></p><p>Once your first backup completes, you'll be able to restore your data from our secure cloud. We keep all old versions of your files and restoring is super simple. (Learn more about <a href='https://blobbackup.com/support/how-to-restore-your-data/'>how to restore your data</a>).</p><p>Thanks again for giving Blobbackup a shot—please don't hesitate to get in touch if there's anything I can do to help you get started!</p><p>Thanks,</p><p>Bimba</p>");
            }

            return $computer;
        });
    
        Route::post('/computers/{computer}', function (Request $request, Response $response, Computer $computer) {
            if (Validator::make($request->all(), [
                'name' => ['string', 'max:255'],
                'operating_system' => ['string', 'max:255'],
                'last_backed_up_at' => ['numeric'],
                'last_backed_up_num_files' => ['integer'],
                'last_backed_up_size' => ['integer'],
                'client_version' => ['string', 'max:8']
            ])->fails())
                return $response->setStatusCode(400);
            if ($computer->user_id != auth()->user()->id)
                return $response->setStatusCode(400);
            $firstBackup = $request->last_backed_up_at && $computer->last_backed_up_at == null;
            $firstComputer = $computer->user->computers->count() == 1;
            if ($firstComputer && $firstBackup) {
                Util::sendNotification($computer->user->email . ' made first backup.');
                Util::sendEmailFrom(
                    'Bimba from Blobbackup',
                    $computer->user->email,
                    'You Made a Backup - Try Restoring',
                    "<p>Hi there,</p><p>It looks like you made your first backup. Congrats! You're already way ahead of most people. But a backup service is only as good as its restore. Give our restore a try! It's super simple.</p><p>Click on the 'Restore Files' button from your control panel.</p><p><img src='https://app.blobbackup.com/img/email-mac-restore1.png'></p><p>Select the files you want to restore by checking them. Then hit restore!</p><p><img src='https://app.blobbackup.com/img/email-mac-restore2.png'></p><p>If you want to restore files from a different time (e.g., yesterday), click on the backups dropdown to find the point in time you want to restore.</p><p><img src='https://app.blobbackup.com/img/email-mac-restore3.png'></p><p>Thanks again for giving Blobbackup a shot—please don't hesitate to get in touch if there's anything I can do to help you get started!</p><p>Thanks,</p><p>Bimba</p>");
            }
            if ($request->name) $computer->name = $request->name;
            if ($request->operating_system) $computer->operating_system = $request->operating_system;
            if ($request->last_backed_up_at) $computer->last_backed_up_at = $request->last_backed_up_at;
            if ($request->last_backed_up_num_files) $computer->last_backed_up_num_files = $request->last_backed_up_num_files;
            if ($request->last_backed_up_size) $computer->last_backed_up_size = $request->last_backed_up_size;
            if ($request->client_version) $computer->client_version = $request->client_version;
            $computer->save();
            $computer->b2_bucket_name = env('B2_BUCKET_NAME');
            return $computer;
        });
    
        Route::get('/computers/{computer}', function (Request $request, Response $response, Computer $computer) {
            if ($computer->user_id != auth()->user()->id)
                return $response->setStatusCode(400);
            $computer->b2_bucket_name = env('B2_BUCKET_NAME');
            return $computer;
        });

        Route::post('/inherit/{fromComputer}/{toComputer}', function (Request $request, Response $response, Computer $fromComputer, Computer $toComputer) {
            if ($fromComputer->user_id != auth()->user()->id || $toComputer->user_id != auth()->user()->id)
                return $response->setStatusCode(400);

            // Swap computer repos
            $tmpUuid = $toComputer->uuid;
            $tmpB2KeyId = $toComputer->b2_key_id;
            $tmpB2ApplicationKey = $toComputer->b2_application_key;
            $toComputer->uuid = $fromComputer->uuid;
            $toComputer->b2_key_id = $fromComputer->b2_key_id;
            $toComputer->b2_application_key = $fromComputer->b2_application_key;
            $fromComputer->uuid = $tmpUuid;
            $fromComputer->b2_key_id = $tmpB2KeyId;
            $fromComputer->b2_application_key = $tmpB2ApplicationKey;

            // Copy some additional fields over
            $toComputer->last_backed_up_at = $fromComputer->last_backed_up_at;
            $toComputer->last_backed_up_num_files = $fromComputer->last_backed_up_num_files;
            $toComputer->last_backed_up_size = $fromComputer->last_backed_up_size;

            // Save changes
            $fromComputer->save();
            $toComputer->save();

            // Delete fromComputer
            $fromComputer->delete();
        });
    
        Route::get('/computers', function (Request $request, Response $response) {
            $computers = auth()->user()->computers;
            foreach ($computers as $computer)
                $computer->b2_bucket_name = env('B2_BUCKET_NAME');
            return $computers;
        });

        Route::post('/changepassword', function (Request $request, Response $response) {
            // Mark changing password as complete
            if ($request->change_complete) {
                $user = auth()->user();
                $user->changing_password = false;
                $user->save();
                return true;
            }

            if (Validator::make($request->all(), [
                'password' => ['required', Password::defaults()]
            ])->fails())
                return $response->setStatusCode(400);

            // Return false if password change already in progress    
            $user = auth()->user();
            if ($user->changing_password)
                return false;

            // Change pasword in db
            $user->password = Hash::make($request->password);
            $user->changing_password = true;
            $user->save();

            // Replace b2 keys for all computers
            foreach ($user->computers as $computer) {
                // Authorize b2
                $authResponse = Http::withBasicAuth(env('B2_KEY_ID'), env('B2_APPLICATION_KEY'))
                    ->get('https://api.backblazeb2.com/b2api/v2/b2_authorize_account');
                $authJson = $authResponse->json();

                // Delete old b2 keys
                Http::withHeaders(['Authorization' => $authJson['authorizationToken']])
                    ->post($authJson['apiUrl'] . '/b2api/v2/b2_delete_key',
                    ['applicationKeyId' => $computer->b2_key_id]);

                // Create new b2 keys
                $createKeyResponse = Http::withHeaders(['Authorization' => $authJson['authorizationToken']])
                    ->post($authJson['apiUrl'] . '/b2api/v2/b2_create_key', [
                        'keyName' => $computer->uuid, 'namePrefix' => $computer->uuid, 'bucketId' => env('B2_BUCKET_ID'), 'accountId' => env('B2_ACCOUNT_ID'),
                        'capabilities' => ['listFiles', 'readFiles', 'writeFiles', 'deleteFiles', 'listBuckets']]);
                $createKeyJson = $createKeyResponse->json();

                // Replace b2 keys in db
                $computer->b2_key_id = $createKeyJson['applicationKeyId'];
                $computer->b2_application_key = $createKeyJson['applicationKey'];
                $computer->save();
            }

            return true;
        });
    });
});