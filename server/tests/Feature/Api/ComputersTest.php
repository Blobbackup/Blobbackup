<?php

namespace Tests\Feature\Api;

use App\Models\Computer;
use App\Models\User;
use App\Util\Util;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Symfony\Component\HttpFoundation\Response;
use Tests\TestCase;

class ComputersTest extends TestCase
{
    use RefreshDatabase;

    public $user1;
    public $user2;
    public $computer1;
    public $computer2;
    public $computer3;

    public function setUp(): void
    {
        parent::setUp();

        $this->user1 = User::factory()->forTesting()->create();
        $this->user2 = User::factory()->forTesting('test2@email.com')->create();

        $this->computer1 = Computer::factory()->existingUser($this->user1)->create();
        $this->computer2 = Computer::factory()->existingUser($this->user1)->create();
        $this->computer3 = Computer::factory()->existingUser($this->user2)->create();
    }

    public function test_it_can_list_all_computers_for_authenticated_user()
    {
        $base64_credentials = base64_encode('test@email.com:b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk=');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/computers');

        $expected_response = [
            [
                'id' => 1,
                'user_id' => 1,
                'name' => $this->computer1->name,
            ],
            [
                'id' => 2,
                'user_id' => 1,
                'name' => $this->computer2->name,
            ],
        ];

        $response->assertOk()
            ->assertJsonCount(2)
            ->assertJson($expected_response);
    }

    public function test_it_can_not_access_computers_without_authentication()
    {
        $headers = [
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/computers');

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }

    public function test_it_can_get_a_computer()
    {
        $base64_credentials = base64_encode('test@email.com:b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk=');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/computers/2');

        $expected_response = [
            'id' => 2,
            'user_id' => 1,
            'name' => $this->computer2->name,
            'uuid' => $this->computer2->uuid,
            'operating_system' => $this->computer2->operating_system,
            'b2_key_id' => $this->computer2->b2_key_id,
            'b2_application_key' => $this->computer2->b2_application_key,
            'last_backed_up_num_files' => $this->computer2->last_backed_up_num_files,
            'last_backed_up_size' => $this->computer2->last_backed_up_size,
            'deleted_at' => null,
            'client_version' => Util::$clientVersion,
            'b2_bucket_name' => env('B2_BUCKET_NAME'),
        ];

        $response->assertOk()
            ->assertJson($expected_response);
    }

    public function test_it_can_not_access_a_computer_without_authentication()
    {
        $headers = [
            'Accept' => 'application/json',
        ];

        $response = $this->withHeaders($headers)
            ->get('/api/computers/1');

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }
}