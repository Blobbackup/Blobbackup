@section('title')
    Settings
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">Settings</h1>
    <input type="hidden" id="oldemail" value="{{ auth()->user()->email }}"/>
    @if($errors->any())
        <div class="text-red-600 mt-8 text-sm">
            {{ $errors->first() }}
        </div>
    @endif
    @if(session('message'))
        <div class="text-green-500 mt-8 text-sm">
            {{ session('message') }}
        </div>
    @endif
    <div class="shadow-lg mt-8 p-6">
        <form method="POST" action="/changeemail" id="changeemailform">
            @csrf
            <div class="text-gray-600">Update Email</div>
            <input type="email" name="email" id="changeemailemail" placeholder="Email" value="{{ auth()->user()->email }}" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
            <input type="password" name="password" id="changeemailpassword" placeholder="Current Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
            <input type="hidden" name="old_password" id="changeemailoldpassword" value=""/>
            <button type="submit" class="bg-gray-200 rounded-full px-4 py-2 font-bold mt-4">Update</button>
        </form>
    </div>
    <div class="shadow-lg mt-8 p-6">
        <form method="POST" action="/changepassword" id="changepasswordform">
            @csrf
            <div class="text-gray-600">Change Password</div>
            <input type="password" name="old_password" id="changepasswordoldpassword" placeholder="Current Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
            <input type="password" name="password" id="changepasswordpassword" placeholder="New Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
            <input type="password" name="password_confirmation" id="changepasswordpasswordconfirmation" placeholder="Confirm New Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
            <button type="submit" class="bg-gray-200 rounded-full px-4 py-2 font-bold mt-4">Change</button>
        </form>
    </div>
    <div class="shadow-lg my-8 p-6">
        <div class="text-gray-600">Delete Account</div>
        <div class="text-gray-600 mt-4">
            WARNING: This will cancel your subscription and delete all your account data (including all backups)
            immediately. Your data will be permanently deleted and cannot be recovered!
        </div>
        <a href="/deleteaccount" class="bg-gray-200 rounded-full px-4 py-2 font-bold mt-4 inline-block">Delete Account</a>
    </div>
    <script>
        $("#changeemailform").submit(() => {
            let newEmail = $("#changeemailemail").val();
            let oldEmail = $("#oldemail").val();
            let password = $("#changeemailpassword").val();
            $("#changeemailpassword").val(hashPassword(password, newEmail));
            $("#changeemailoldpassword").val(hashPassword(password, oldEmail));
            return true;
        });
        $("#changepasswordform").submit(() => {
            let email = $("#oldemail").val();
            let oldPassword = $("#changepasswordoldpassword").val();
            let password = $("#changepasswordpassword").val();
            let passwordConfirmation = $("#changepasswordpasswordconfirmation").val();
            $("#changepasswordoldpassword").val(hashPassword(oldPassword, email));
            $("#changepasswordpassword").val(hashPassword(password, email));
            $("#changepasswordpasswordconfirmation").val(hashPassword(passwordConfirmation, email));
            return true;
        });
    </script>
</x-app-layout>
