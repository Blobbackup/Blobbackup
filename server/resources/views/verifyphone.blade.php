@section('title')
    Verify Phone Number
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">Verify Phone Number</h1>
    @if($errors->any())
        <div class="text-red-600 mt-8 text-sm">
            {{ $errors->first() }}
        </div>
    @endif
    <form method="POST" action="/verifyphone" class="text-gray-600 my-8">
        @csrf
        <div>
            We just sent a verification code to '{{ $phone }}' via SMS. Please enter it below to verify your phone number. 
        </div>
        <input type="hidden" name="phone" value="{{ $phone }}"/>
        <input type="text" name="code" placeholder="Verification Code" class="w-full border border-gray-400 rounded-full px-4 py-1 mt-4" required />
        <div class="mt-4">
            <button type="submit">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                Verify
            </button>
            <a href="/settings" class="ml-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M13.477 14.89A6 6 0 015.11 6.524l8.367 8.368zm1.414-1.414L6.524 5.11a6 6 0 018.367 8.367zM18 10a8 8 0 11-16 0 8 8 0 0116 0z" clip-rule="evenodd" />
                </svg>
                Cancel
            </a>
        </div>
    </form>
</x-app-layout>
