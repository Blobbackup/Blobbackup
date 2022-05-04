@section('title')
    Sign In
@endsection
<x-guest-layout>
    <x-auth-card>
        <div class="text-center">
            <a href="/">
                <img src="{{ asset('img/logo.png') }}" class="inline-block w-8 h-8" />
                <h1 class="text-2xl font-bold mt-2">Blobbackup</h1>
            </a>
            <h2 class="text-gray-600 mt-2">Sign in to your account.</h2>
        </div>
        @if($errors->any())
            <div class="text-center text-red-600 mt-2 text-sm">
                {{ $errors->first() }}
            </div>
        @endif
        <div class="mt-4">
            <form method="POST" action="/login" id="login_form" class="hidden" accept-charset="utf-8">
                @csrf
                <input type="email" name="email" id="email" placeholder="Email" class="w-full border border-gray-400 rounded-full px-4 py-1" value="{{ old('email') }}" required />
                <input type="password" name="password" id="password" placeholder="Password" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" minlength="8" required />
                <button type="submit" class="bg-gray-200 rounded-full w-full py-2 font-bold mt-4">Sign In</button>
            </form>
        </div>
        <div class="mt-4 text-center">
            <a href="/register" class="text-blue-600 underline">Don't have an account yet?</a>
        </div>
        <script>
            $("#login_form").removeClass("hidden");
            $("#login_form").submit(() => {
                let email = $("#email").val();
                let password = $("#password").val();
                $("#password").val(hashPassword(password, email));
                return true;
            });
        </script>
    </x-auth-card>
</x-guest-layout>
