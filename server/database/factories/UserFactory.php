<?php

namespace Database\Factories;

use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

class UserFactory extends Factory
{
    /**
     * Configure the model factory.
     *
     * @return $this
     */
    public function configure()
    {
        return $this->afterCreating(function (User $user) {
            $user->createAsCustomer([
                'trial_ends_at' => now()->addDays(30),
            ]);
        });
    }

    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'email' => $this->faker->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => bcrypt('password'),
            'remember_token' => Str::random(10),
        ];
    }

    /**
     * Indicate that the model's email address should be unverified.
     *
     * @return Factory
     */
    public function unverified()
    {
        return $this->state(function (array $attributes) {
            return [
                'email_verified_at' => null,
            ];
        });
    }

    /**
     * Indicate that the model's email and password should be fixed for testing consistency
     * because the front-end uses encryption
     *
     * @return Factory
     */
    public function forTesting(?string $email = null, ?string $encrypted_password = null)
    {
        return $this->state(function () use ($email, $encrypted_password) {
            return [
                'email' => $email ?? 'test@email.com',
                'password' => $encrypted_password ?? bcrypt('b6yOfA0cIthbuYerlb/KodNcJlp1aO4uW8hOpXydBdk='),
            ];
        });
    }
}
