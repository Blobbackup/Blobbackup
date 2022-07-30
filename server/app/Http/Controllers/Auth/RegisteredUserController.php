<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Models\User;
use App\Util\Util;
use Illuminate\Auth\Events\Registered;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\Rules;
use Illuminate\Support\Facades\URL;

class RegisteredUserController extends Controller
{
    /**
     * Display the registration view.
     *
     * @return \Illuminate\View\View
     */
    public function create()
    {
        return view('auth.register');
    }

    private function getNewUserFields(Request $request)
    {
        $fields = [
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
            'groups' => true,
            'accepting_users' => true,
        ];
        if ($request->leader_id && User::find($request->leader_id)->accepting_users) {
            $fields += [
                'leader_id' => $request->leader_id,
                'status' => 'pending',
                'groups' => false,
            ];
        }
        return $fields;
    }

    /**
     * Handle an incoming registration request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\RedirectResponse
     *
     * @throws \Illuminate\Validation\ValidationException
     */
    public function store(Request $request)
    {
        $request->validate([
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'string', 'email', 'max:255', 'unique:users'],
            'password' => ['required', 'confirmed', Rules\Password::defaults()],
            'leader_id' => ['numeric', 'exists:users,id']
        ]);

        $user = User::create($this->getNewUserFields($request));

        $user->createAsCustomer([
            'trial_ends_at' => now()->addDays(Util::$trialLengthDays)
        ]);

        if ($request->leader_id) {
            $url = URL::to('/') . '/group';
            Util::sendEmail(User::find($request->leader_id)->email,
                "A New User Has Requested to Join Your Group",
                $request->email . " has requested to join your group.<br/><br/><a href='" . $url . "'>Accept Request</a>");
        }

        event(new Registered($user));

        Auth::login($user);

        if (env('APP_ENV') != "testing") {
            Util::sendNotification('New user: ' . $user->email . ' (' . htmlspecialchars($user->name) . ')');
        }

        return redirect(route('backup'))->with('welcome', true);
    }
}
