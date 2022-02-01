<!DOCTYPE html>
<html>
    <head>
        <title>@yield('title') - Blobbackup</title>
        <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
        <link rel="shortcut icon" type="image/jpg" href="{{ asset('img/logo.png') }}"/>
        <script src="{{ asset('js/jquery.min.js') }}"></script>
        <script src="{{ asset('js/sjcl.min.js') }}"></script>
        <script src="{{ asset('js/utils.js') }}"></script>
    </head>
    <body>
        {{ $slot }}
    </body>
</html>
