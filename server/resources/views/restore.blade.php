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
        <div>
            <img src="{{ asset('img/restore-installed.png') }}" />
        </div>
        <h2 class="font-bold">Option 2: Restore to a Computer Where You Don’t Have Blobbackup Installed</h2>
        <div class="mt-4">
            Step 1: <a href="" id="downloadlink" class="text-blue-600 underline">Download</a> Blobbackup.
        </div>
        <div class="mt-4">
            Step 2: Install Blobbackup on your computer (<a href="/help" class="text-blue-600 underline">Need help with this?</a>).
        </div>
        <div class="mt-4">
            Step 3: Sign in and click the Restore Files button.
        </div>
        <div>
            <img src="{{ asset('img/restore-uninstalled.png') }}" />
        </div>
    </div>
    <script>
        function isMac() { return navigator.platform.indexOf('Mac') > -1; }
        function isWindows() { return navigator.platform.indexOf('Win') > -1; }
        if (isMac())
            document.getElementById("downloadlink").setAttribute("href", "{{ asset('bin/blobbackup-osx-1.0.0.dmg') }}");
        else if (isWindows())
            document.getElementById("downloadlink").setAttribute("href", "{{ asset('bin/blobbackup-win-1.0.0.exe') }}");
        else alert("Blobbackup currently only supports Mac and Windows.");
    </script>
</x-app-layout>