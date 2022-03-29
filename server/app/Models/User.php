<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;
use Laravel\Paddle\Billable;

class User extends Authenticatable implements MustVerifyEmail
{
    use HasApiTokens, HasFactory, Notifiable, Billable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = [
        'name',
        'email',
        'password',
        'leader_id',
        'status',
        'groups',
        'email_verified_at',
    ];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];

    public function computers()
    {
        return $this->hasMany(Computer::class);
    }

    public function deleteComputers()
    {
        foreach ($this->computers as $computer)
            $computer->delete();
    }

    public function deleteAccount()
    {
        $group = User::where('leader_id', $this->id)->get();
        foreach ($group as $member)
            $member->deleteAccount();
        if ($this->subscribed()) {
            $this->subscription()->cancelNow();
            $this->subscription()->delete();
            foreach ($this->receipts as $receipt)
                $receipt->delete();
        }
        $this->deleteComputers();
        $this->customer()->delete();
        $this->delete();
    }

    public function computersToBill()
    {
        $computers = $this->computers->count();
        foreach (User::where('leader_id', $this->id)->where('status', 'active')->get() as $user)
            $computers += $user->computers->count();
        return $computers;
    }
}
