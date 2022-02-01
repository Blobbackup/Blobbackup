@section('title')
    Verify Email
@endsection
<x-guest-layout>
    <x-auth-card>
        <div class="text-center">
            <a href="/">
                <img src="{{ asset('img/logo.png') }}" class="inline-block w-8 h-8" />
                <h1 class="text-2xl font-bold mt-2">Blobbackup</h1>
            </a>
        </div>

        <div class="mt-4 text-gray-600 text-center">
            {{ __('Thanks for signing up! Before getting started, could you verify your email address by clicking on the link we just emailed to you? If you didn\'t receive the email, we will gladly send you another.') }}
        </div>

        @if (session('status') == 'verification-link-sent')
            <div class="mt-4 text-center text-green-600">
                {{ __('A new verification link has been sent to the email address you provided during registration.') }}
            </div>
        @endif

        <div class="items-center text-center justify-between">
            <form method="POST" action="{{ route('verification.send') }}">
                @csrf

                <div>
                    <button type="submit" class="bg-gray-200 rounded-full w-full py-2 font-bold mt-4">
                        {{ __('Resend Verification Email') }}
                    </button>
                </div>
            </form>

            <form method="POST" action="{{ route('logout') }}">
                @csrf

                <button type="submit" class="text-blue-600 underline mt-3">
                    {{ __('Log Out') }}
                </button>
            </form>
        </div>
    </x-auth-card>
</x-guest-layout>
