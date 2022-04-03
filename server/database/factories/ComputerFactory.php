<?php

namespace Database\Factories;

use App\Models\User;
use App\Util\Util;
use Illuminate\Database\Eloquent\Factories\Factory;

class ComputerFactory extends Factory
{
    public function definition(): array
    {
        return [
            'name' => $this->faker->name(),
            'uuid' => $this->faker->uuid(),
            'operating_system' => $this->faker->word(),
            'b2_key_id' => $this->faker->word(),
            'b2_application_key' => $this->faker->word(),
            'last_backed_up_at' => now(),
            'last_backed_up_num_files' => $this->faker->randomNumber(5),
            'last_backed_up_size' => $this->faker->randomNumber(9),
            'created_at' => now(),
            'updated_at' => now(),
            'client_version' => Util::$clientVersion,
            'user_id' => User::factory(),
        ];
    }

    public function existingUser(User $user)
    {
        return $this->state(function (array $attributes) use ($user) {
            return [
                'user_id' => $user->id,
            ];
        });
    }
}
