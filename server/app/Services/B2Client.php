<?php

namespace App\Services;


use Illuminate\Support\Facades\Http;

class B2Client
{
    public function __construct()
    {
        // todo: implement constructor
    }

    public function authorizeAccount()
    {
        return Http::withBasicAuth(env('B2_KEY_ID'), env('B2_APPLICATION_KEY'))
            ->get('https://api.backblazeb2.com/b2api/v2/b2_authorize_account');
    }

    public function createKey($token, $api_url, $name)
    {
        $data = [
            'keyName' => $name,
            'namePrefix' => $name,
            'bucketId' => env('B2_BUCKET_ID'),
            'accountId' => env('B2_ACCOUNT_ID'),
            'capabilities' => [
                'listFiles',
                'readFiles',
                'writeFiles',
                'deleteFiles',
                'listBuckets',
            ],
        ];

        return Http::withHeaders(['Authorization' => $token])
            ->post($api_url . '/b2api/v2/b2_create_key', $data);
    }
}
