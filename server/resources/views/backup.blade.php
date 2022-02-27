@section('title')
    Backup New Computer
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold" id="mac">Backup New Computer</h1>
    <div class="shadow-lg my-8 p-6">
        <div>
            Step 1: Download Blobbackup:
            <a href="{{ asset('bin/blobbackup-darwin-amd-1.0.4.dmg') }}" class="text-blue-600 underline">Intel Mac</a> |
            <a href="{{ asset('bin/blobbackup-darwin-arm-1.0.4.dmg') }}" class="text-blue-600 underline">M1 Mac</a> |
            <a href="{{ asset('bin/blobbackup-win-1.0.4.exe') }}" class="text-blue-600 underline">Windows</a>.
        </div>
        <div class="mt-4">
            Step 2: Install Blobbackup on your computer. Step by step instructions:
            <a href="https://blobbackup.com/support/how-to-install-blobbackup-on-mac" class="text-blue-600 underline" target="_blank">Mac</a> |
            <a href="https://blobbackup.com/support/how-to-install-blobbackup-on-windows" class="text-blue-600 underline" target="_blank">Windows</a>.
        </div>
        <div class="mt-4">
            Step 3: Open Blobbackup and sign in to start backing up!
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/mac-main.png') }}" />
        </div>
    </div>
</x-app-layout>