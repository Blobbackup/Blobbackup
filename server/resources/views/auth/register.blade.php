@section('title')
    @if(isset($leader))
        Start Backing Up
    @else
        Start Trial
    @endif
@endsection
<x-guest-layout>
    <x-auth-card>
        <div class="text-center">
            <a href="/">
                <img src="{{ asset('img/logo.png') }}" class="inline-block w-8 h-8" />
                <h1 class="text-2xl font-bold mt-2">Blobbackup</h1>
            </a>
            <h2 class="text-gray-600 mt-2">
                @if(isset($leader))
                    <strong>{{ $leader->email }}</strong> has invited you to join their group and will pay for your account's computer backups.
                @else
                    Free {{ Util::$trialLengthDays }} day trial. No card required.
                @endif
            </h2>
            @if(isset($leader))
                <div class="bg-blue-100 border-blue-500 text-blue-600 text-xs border-1 text-center mt-2 mb-4 p-2 rounded">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 inline-block mr-1 -mt-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                    </svg>
                    <strong>{{ $leader->email }}</strong> can't access your data
                </div>
            @endif
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
                <input type="password" name="password" id="password" placeholder="Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" minlength="8" required />
                <div class="text-center mt-4 text-xs text-gray-500">
                    All your backups will be encrypted using this password. Pick a good one and don't forget it. There is no way to
                    recover this password (or your backups) if you do.
                </div>
                <input type="password" name="password_confirmation" id="passwordconfirmation" placeholder="Confirm Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
                @if(isset($leader))
                    <input type="hidden" name="leader_id" value="{{ $leader->id }}"/>
                @endif
                <button @if(auth()->check()) disabled @endif type="submit" class="bg-gray-200 rounded-full w-full py-2 font-bold mt-4">
                    @if(isset($leader))
                        Create Account
                    @else
                        Start Trial
                    @endif
                </button>
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
