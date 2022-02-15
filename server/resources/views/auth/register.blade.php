@section('title')
    Start Trial
@endsection
<x-guest-layout>
    <x-auth-card>
        <div class="text-center">
            <a href="/">
                <img src="{{ asset('img/logo.png') }}" class="inline-block w-8 h-8" />
                <h1 class="text-2xl font-bold mt-2">Blobbackup</h1>
            </a>
            <h2 class="text-gray-600 mt-2">Free 30 day trial. No card required.</h2>
        </div>
        @if($errors->any())
            <div class="text-center text-red-600 mt-2 text-sm">
                {{ $errors->first() }}
            </div>
        @endif
        <div class="mt-4">
            <form method="POST" action="/register" id="register_form" class="hidden" accept-charset="utf-8">
                @csrf
                <input type="email" name="email" id="email" placeholder="Email" class="w-full border border-gray-400 rounded-full px-4 py-1" value="{{ old('email') }}" required />
                <input type="password" name="password" id="password" placeholder="Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
                <div class="text-center mt-4 text-xs text-gray-500">
                    All your backups will be encrypted using this password. Pick a good one and do not forget it. There is no way to 
                    recover this password if you forget it.
                </div>
                <input type="password" name="password_confirmation" id="passwordconfirmation" placeholder="Confirm Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
                <button type="submit" class="bg-gray-200 rounded-full w-full py-2 font-bold mt-4">Start Trial</button>
                <div class="text-center mt-4 text-xs">
                    <div class="text-gray-500">By proceeding, you agree to the Blobbackup</div> 
                    <a href="https://blobbackup.com/terms" class="text-blue-500">Terms of Service</a> and
                    <a href="https://blobbackup.com/privacy" class="text-blue-500">Privacy Policy</a>.
                </div>
            </form>
        </div>
        <div class="mt-4 text-center">
            <a href="/login" class="text-blue-600 underline">Already have an account?</a>
        </div>
        <script>
            $("#register_form").removeClass("hidden");
            $("#register_form").submit(() => {
                let email = $("#email").val();
                let password = $("#password").val();
                let passwordConfirmation = $("#passwordconfirmation").val();
                $("#password").val(hashPassword(password, email));
                $("#passwordconfirmation").val(hashPassword(passwordConfirmation, email));
                return true;
            });
        </script>
    </x-auth-card>
</x-guest-layout>
