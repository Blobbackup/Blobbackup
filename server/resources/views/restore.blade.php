@section('title')
    Restore from Backup
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">Restore from Backup</h1>
    <div class="shadow-lg my-8 p-6">
        <h2 class="font-bold">Option 1: Restore to the Computer You Installed Blobbackup On</h2>
        <div class="mt-4">
            Just click the Restore Files button on the control panel.
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/restore-installed.png') }}" />
        </div>
        <h2 class="font-bold">Option 2: Restore to a Computer Where You Don’t Have Blobbackup Installed</h2>
        <div class="mt-4">
            Step 1: Download Blobbackup:
            <a href="{{ asset('bin/blobbackup-darwin-amd-1.0.2.dmg') }}" class="text-blue-600 underline">Intel Mac</a> |
            <a href="{{ asset('bin/blobbackup-darwin-arm-1.0.2.dmg') }}" class="text-blue-600 underline">M1 Mac</a> |
            <a href="{{ asset('bin/blobbackup-win-1.0.2.exe') }}" class="text-blue-600 underline">Windows</a>.
        </div>
        <div class="mt-4">
            Step 2: Install Blobbackup on your computer (<a href="/help" class="text-blue-600 underline">Need help with this?</a>).
        </div>
        <div class="mt-4">
            Step 3: Sign in and click the Restore Files button.
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/restore-uninstalled.png') }}" />
        </div>
    </div>
</x-app-layout>