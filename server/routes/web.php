<?php

use App\Models\Computer;
use App\Models\User;
use App\Util\Util;
use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Route;
use Illuminate\Validation\Rules\Password;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('auth.login');
});

Route::get('/group/{uuid}', function (Request $request, string $uuid) {
    $user = User::where('uuid', $uuid)->first();
    abort_unless($user && $user->groups && $user->accepting_users, 404);
    return view('auth.register', [
        'leader' => $user
    ]);
});

Route::middleware(['auth', 'verified', 'active'])->group(function () {
    Route::get('/dashboard', function () {
        return view('dashboard', [
            'user' => auth()->user()
        ]);
    })->name('dashboard');

    Route::get('/computers/{user}', function (Request $request, User $user) {
        return view('dashboard', [
            'user' => $user
        ]);
    });

    Route::get('/deletecomputer/{computer}', function (Request $request, Computer $computer) {
        abort_unless($computer->user->is(auth()->user()) || $computer->user->leader_id == auth()->user()->id, 404);
        return view('deletecomputer', [
            'computer' => $computer
        ]);
    });

    Route::post('/deletecomputer/{computer}', function (Request $request, Computer $computer) {
        abort_unless($computer->user->is(auth()->user()) || $computer->user->leader_id == auth()->user()->id, 404);
        $computer->delete();
        Util::sendEmail($computer->user->email, "Your Computer Has Been Deleted", "Your computer <b>" . $computer->name . "</b> has been deleted.");
        if ($computer->user->id == auth()->user()->id)
            return redirect('/dashboard');
        else
            return redirect('/group')->with('message', 'Computer deleted.');
    });

    Route::get('/backup', function () {
        return view('backup');
    })->name('backup');

    Route::get('/restore', function () {
        return view('restore');
    })->name('restore');

    Route::get('/payment', function (Request $request) {
        $user = auth()->user();
        $payLink = $user->subscribed() ? 
            $user->subscription()->updateUrl() :
            $user->newSubscription('default', $monthly = env('PADDLE_SUBSCRIPTION_PLAN_ID'))
                ->returnTo(route('payment'))
                ->create();
        return view('payment', [
            'payLink' => $payLink
        ]);
    })->name('payment');

    Route::get('/group', function () {
        $user = auth()->user();
        abort_unless(!$user->leader_id && $user->groups, 404);
        if (!$user->uuid) {
            $user->uuid = Str::uuid()->toString();
            $user->save();
        }
        return view('group', [
            'users' => User::where('leader_id', auth()->user()->id)->orderByDesc('created_at')->get(),
            'groupUrl' => URL::to('/') . '/group/' . $user->uuid
        ]);
    })->name('group');

    Route::post('/toggleaccepting', function () {
        $user = auth()->user();
        $user->accepting_users = !$user->accepting_users;
        $user->save();
        return back();
    });

    Route::post('/judgeuser/{user}', function (Request $request, User $user) {
        abort_unless($user->leader_id == auth()->user()->id, 404);
        if ($request->judgement == 'accept') {
            $user->status = 'active';
            $user->save();
            return back()->with('message', 'Accepted ' . $user->email . '.');
        } else {
            $user->deleteAccount();
            return back()->withErrors('Rejected ' . $user->email . '.');
        }
    });

    Route::get('/deleteuser/{user}', function (Request $request, User $user) {
        abort_unless($user->leader_id == auth()->user()->id, 404);
        return view('deleteuser', [
            'user' => $user
        ]);
    })->name('deleteuser');

    Route::post('/deleteuser/{user}', function (Request $request, User $user) {
        abort_unless($user->leader_id == auth()->user()->id, 404);
        $user->deleteAccount();
        return redirect('/group')->with('message', 'Deleted ' . $user->email . '.');
    });

    Route::post('/deletepayment', function () {
        auth()->user()->subscription()->cancelNow();
        return back();
    });

    Route::get('/settings', function () {
        return view('settings');
    })->name('settings');

    Route::post('/changeemail', function (Request $request) {
        $request->validate([
            'email' => ['required', 'string', 'email', 'max:255', 'unique:users'],
            'password' => ['required', Password::defaults()],
            'old_password' => ['required', Password::defaults()],
        ]);
        $user = auth()->user();
        if (!Hash::check($request->old_password, $user->password))
            return back()->withErrors('Password incorrect.');
        $user->email = $request->email;
        $user->password = Hash::make($request->password);
        $user->save();
        return back()->with('message', 'Email updated.');
    });
    
    Route::post('/changepassword', function (Request $request) {
        $request->validate([
            'password' => ['required', 'confirmed', Password::defaults()],
            'old_password' => ['required', Password::defaults()],
        ]);
        $user = auth()->user();
        if (!Hash::check($request->old_password, $user->password))
            return back()->withErrors('Password incorrect.');
        $user->password = Hash::make($request->password);
        $user->save();
        return back()->with('message', 'Password changed.');
    });

    Route::get('/deleteaccount', function () {
        return view('deleteaccount');
    })->name('deleteaccount');

    Route::post('/deleteaccount', function () {
        $user = auth()->user();
        $user->deleteAccount();
        auth()->logout();
        return redirect('/login')->withErrors('Your account has been deleted.');
    });
});


require __DIR__ . '/auth.php';
