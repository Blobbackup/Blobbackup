<?php

namespace Tests\Feature\Api;

use App\Models\Computer;
use App\Models\User;
use App\Util\Util;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Http;
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

    public function test_it_can_create_a_computer_correctly()
    {
        $this->withoutExceptionHandling();

        $fake_response_authorization = [
            'authorizationToken' => 'fake-api-token',
            'apiUrl' => 'http://fake.test',
        ];

        $fake_response_create_key = [
            'applicationKeyId' => 'fake-app-key-id',
            'applicationKey' => 'fake-app-key',
        ];

        Http::fake([
            'https://api.backblazeb2.com/*' => Http::response($fake_response_authorization),
            'http://fake.test/*' => Http::response($fake_response_create_key),
        ]);

        $base64_credentials = base64_encode('test@email.com:b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk=');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $data = [
            'name' => 'computer-name',
            'operating_system' => 'FAKE_TEST_OS',
        ];

        $response = $this->withHeaders($headers)
            ->post('api/computers', $data);

        $expected_response = [
            'name' => 'computer-name',
            'operating_system' => 'FAKE_TEST_OS',
            "b2_key_id" => "fake-app-key-id",
            "b2_application_key" => "fake-app-key",
            "user_id" => 1,
        ];

        $response->assertStatus(Response::HTTP_CREATED)
            ->assertJson($expected_response);

        $this->assertDatabaseHas('computers', $expected_response);
    }

    public function test_it_can_not_create_a_computer_without_authentication()
    {
        Http::fake([
            '*' => Http::response([], Response::HTTP_BAD_REQUEST),
        ]);

        $headers = [
            'Accept' => 'application/json',
        ];

        $data = [
            'name' => 'computer-name',
            'operating_system' => 'FAKE_TEST_OS',
        ];

        $response = $this->withHeaders($headers)
            ->post('api/computers', $data);

        Http::assertNothingSent();

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }

    public function test_it_can_update_a_computer_correctly()
    {
        $base64_credentials = base64_encode('test@email.com:b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk=');

        $headers = [
            'Authorization' => 'Basic ' . $base64_credentials,
            'Accept' => 'application/json',
        ];

        $data = [
            'name' => 'computer-name',
            'operating_system' => 'FAKE_TEST_OS',
            'last_backed_up_at' => '1649199766',
            'last_backed_up_num_files' => '17',
            'last_backed_up_size' => '84033019',
            'client_version' => Util::$clientVersion,
        ];

        $response = $this->withHeaders($headers)
            ->post('api/computers/1', $data);

        $expected_result = [
            'id' => 1,
            'name' => 'computer-name',
            'operating_system' => 'FAKE_TEST_OS',
            'last_backed_up_at' => '2022-04-05 23:02:46',
            'last_backed_up_num_files' => '17',
            'last_backed_up_size' => '84033019',
            'client_version' => Util::$clientVersion,
        ];

        $response->assertStatus(Response::HTTP_OK)
            ->assertJsonStructure(array_keys($expected_result));

        $this->assertDatabaseHas('computers', $expected_result);
    }

    public function test_it_can_not_update_a_computer_without_authentication()
    {
        $headers = [
            'Accept' => 'application/json',
        ];

        $data = [
            'client_version' => Util::$clientVersion,
        ];

        $response = $this->withHeaders($headers)
            ->post('api/computers/1', $data);

        $response->assertStatus(Response::HTTP_UNAUTHORIZED);
    }
}
