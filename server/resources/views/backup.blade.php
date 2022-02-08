@section('title')
    Backup New Computer
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold" id="mac">Backup New Computer</h1>
    <div class="shadow-lg my-8 p-6">
        <div>
            Step 1: Download Blobbackup:
            <a href="{{ asset('bin/blobbackup-darwin-amd-1.0.1.dmg') }}" class="text-blue-600 underline">Intel Mac</a> |
            <a href="{{ asset('bin/blobbackup-darwin-arm-1.0.1.dmg') }}" class="text-blue-600 underline">M1 Mac</a> |
            <a href="{{ asset('bin/blobbackup-win-1.0.1.exe') }}" class="text-blue-600 underline">Windows</a>.
        </div>
        <div class="mt-4">
            Step 2: Install Blobbackup on your computer (<a href="/help" class="text-blue-600 underline">Need help with this?</a>).
        </div>
        <div class="mt-4 ml-4">
            Note: Blobbackup on Mac requires full disk access. Make sure to provide this from your System Preferences.
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/mac-plus.png') }}"/>
        </div>
        <div class="ml-4">
            Note: Blobbackup on Windows is not code signed yet so you might see a warning when installing.
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/win-defender.png') }}"/>
        </div>
        <div>
            Step 3: Open Blobbackup and sign in to start backing up!
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/mac-main.png') }}" />
        </div>
    </div>
</x-app-layout>