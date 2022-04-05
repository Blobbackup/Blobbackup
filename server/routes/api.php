<?php

use App\Models\Computer;
use App\Models\User;
use App\Services\B2Client;
use App\Util\Util;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;

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

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::middleware(['auth.basic', 'verified', 'active'])->group(function () {
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
                'operating_system' => ['required', 'string', 'max:255'],
            ])->fails()) {
                return $response->setStatusCode(400);
            }

            // Create backblaze credentials
            $b2 = new B2Client();

            $authResponse = $b2->authorizeAccount();

            if ($authResponse->status() != 200) {
                return $response->setStatusCode(400);
            }

            $uuid = Str::uuid()->toString();
            $authJson = $authResponse->json();

            $createKeyResponse = $b2->createKey(
                $authJson['authorizationToken'],
                $authJson['apiUrl'],
                $uuid
            );

            if ($createKeyResponse->status() != 200) {
                return $response->setStatusCode(400);
            }

            // Create computer
            $createKeyJson = $createKeyResponse->json();
            $computer = new Computer();
            $computer->name = $request->name;
            $computer->uuid = $uuid;
            $computer->operating_system = $request->operating_system;
            $computer->b2_key_id = $createKeyJson['applicationKeyId'];
            $computer->b2_application_key = $createKeyJson['applicationKey'];
            $computer->user_id = auth()->user()->id;
            $computer->save();
            $computer->b2_bucket_name = env('B2_BUCKET_NAME');
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

        Route::get('/computers', function (Request $request, Response $response) {
            return auth()->user()->computers;
        });
    });
});
