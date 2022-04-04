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
            Step 1: Download Blobbackup.
        </div>
        <div class="mt-4">
            <a href="{{ asset('bin/blobbackup-darwin-amd-' . Util::$clientVersion . '.dmg') }}" class="bg-gray-200 rounded-full px-4 py-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                Intel Mac
            </a>
            <a href="{{ asset('bin/blobbackup-darwin-arm-' . Util::$clientVersion . '.dmg') }}" class="bg-gray-200 rounded-full px-4 py-2 ml-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                M1 Mac
            </a>
            <a href="{{ asset('bin/blobbackup-win-' . Util::$clientVersion . '.exe') }}" class="bg-gray-200 rounded-full px-4 py-2 ml-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                Windows
            </a>
        </div>
        <div class="mt-8">
            Step 2: Install Blobbackup on your computer. Step by step instructions:
            <a href="https://blobbackup.com/support/how-to-install-blobbackup-on-mac" class="text-blue-600 underline" target="_blank">Mac</a> |
            <a href="https://blobbackup.com/support/how-to-install-blobbackup-on-windows" class="text-blue-600 underline" target="_blank">Windows</a>.
        </div>
        <div class="mt-4">
            Step 3: Sign in and click the Restore Files button.
        </div>
        <div class="w-1/2">
            <img src="{{ asset('img/restore-uninstalled.png') }}" />
        </div>
    </div>
</x-app-layout>