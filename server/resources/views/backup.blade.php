@section('title')
    Backup New Computer
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold" id="mac">Backup New Computer</h1>
    <div class="shadow-lg my-8 p-6">
        <div>
            Step 1: <a href="" id="downloadlink" class="text-blue-600 underline">Download</a> Blobbackup.
        </div>
        <div class="mt-4">
            Step 2: Install Blobbackup on your computer (<a href="/help" class="text-blue-600 underline">Need help with this?</a>).
        </div>
        <div class="mt-4">
            Step 3: Open Blobbackup and sign in to start backing up!
        </div>
        <div>
            <img src="{{ asset('img/mac-main.png') }}" />
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