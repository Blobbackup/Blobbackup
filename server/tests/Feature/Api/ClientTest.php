<?php

namespace Tests\Feature\Api;

use App\Util\Util;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ClientTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_client_version_correctly()
    {
        $expected_version = Util::$clientVersion;

        $response = $this->get('/api/client/version');
        
        $response->assertStatus(200)
            ->assertSee($expected_version);
    }
}
