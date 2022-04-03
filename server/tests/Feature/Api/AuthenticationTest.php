<?php

namespace Tests\Feature\Api;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Symfony\Component\HttpFoundation\Response;
use Tests\TestCase;

class AuthenticationTest extends TestCase
{
    use RefreshDatabase;

    public $user;

    public function setUp(): void
    {
        parent::setUp();

        $this->user = User::factory()->forTesting()->create();
    }

    public function test_user_can_authenticate_with_basic_auth()
    {
        $base64_credentials = base64_encode('test@email.com:b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk=');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/login');

        $response->assertStatus(Response::HTTP_OK);

        $response->assertJson([
            'on_trial' => true,
            'subscribed' => false,
        ]);
    }

    public function test_user_can_not_authenticate_with_invalid_password()
    {
        $base64_credentials = base64_encode('test@email.com:invalid_password');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/login');

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }

    public function test_it_returns_unauthorized_when_missing_basic_auth_headers()
    {
        $headers = [
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/login');

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }
}
