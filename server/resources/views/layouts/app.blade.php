<!DOCTYPE html>
<html>
    <head>
        <meta name="robots" content="noindex,nofollow"/>
        <title>@yield('title') - Blobbackup</title>
        <link href="{{ asset('css/app.css') }}" rel="stylesheet">
        <link rel="shortcut icon" type="image/jpg" href="{{ asset('img/logo.png') }}"/>
        <script src="{{ asset('js/jquery.min.js') }}"></script>
        <script src="{{ asset('js/sjcl.min.js') }}"></script>
        <script src="{{ asset('js/utils.js') }}"></script>
        @paddleJS
    </head>
    <body class="font-sans">
        <header class="sticky top-0 z-50">
            @if (!auth()->user()->subscribed() && !request()->get('checkout'))
                @if (!auth()->user()->leader_id)
                    @if (auth()->user()->onTrial())
                        <div class="bg-blue-100 text-center py-4">Your trial period will expire in {{ Util::timeDelta(new DateTime(), auth()->user()->customer->trial_ends_at) }}. <a href="/payment" class="text-blue-600 underline">Add Payment Method</a>.</div>
                    @else
                        <div class="bg-red-100 text-center py-4">Your trial period has expired. <a href="/payment" class="text-blue-600 underline">Add Payment Method</a>.</div>
                    @endif
                @endif
            @endif
            <div class="shadow-lg p-6 bg-white flex">
                @if (session('welcome'))
                    <div id="welcome" class="fixed w-full h-screen top-0 left-0 flex" style="background-color: rgba(0,0,0,0.5)">
                        <div class="bg-white p-6 mx-auto my-auto shadow-lg max-w-lg">
                            <div class="text-center">
                                <div class="rounded-full overflow-hidden inline-block">
                                    <img src="img/bimba.jpeg" width="72"/>
                                </div>
                            </div>
                            <div class="text-center">
                                Welcome from Bimba, Blobbackup's Founder
                            </div>
                            <div class="font-bold mt-8">
                                Thanks for signing up — your account's ready to go!
                            </div>
                            <div class="mt-4">
                                Now you just have to install Blobbackup on your computer. Download
                                the installer for your operating system below, follow some easy instructions,
                                and that's it! Your computer data will start backing up to our secure cloud.
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
                            <div class="mt-4">
                                If you ever need a hand, please contact me directly at 
                                <a href="mailto:bimba@blobbackup.com" target="_blank" class="underline text-blue-600">bimba@blobbackup.com</a>. 
                                I'm always happy to help!
                            </div>
                            <div class="mt-4">
                                Thanks again and all the best,
                            </div>
                            <div>
                                Bimba, Founder, Blobbackup
                            </div>
                            <a href="" class="font-bold text-lg text-white bg-blue-500 rounded-full text-center mt-8 py-2 block mt-4" id="start-backing-up">Go to My Account</a>
                        </div>
                    </div>
                @endif
                <a href="/dashboard" class="flex-initial font-bold text-2xl block">
                    <img src="{{ asset('img/logo.png') }}" class="w-8 h-8 -mt-1 mr-1 inline-block"/>
                    Blobbackup
                </a>
                <div class="flex-1 text-right text-gray-600 mt-1">
                    <span class="ml-4">{{ auth()->user()->email }}</span>
                    <form method="POST" action="/logout" class="inline-block">
                        @csrf
                        <a href="" onclick="event.preventDefault(); this.closest('form').submit();" class="ml-4 bg-gray-200 rounded-full px-4 py-2 font-bold">Sign Out</a>
                    </form>
                </div>
            </div>
        </header>
        <main class="flex">
            <div class="flex-initial shadow-lg p-8 min-h-screen text-gray-600">
                <a href="/dashboard" class="block @if(request()->routeIs('dashboard')) font-bold @endif">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
                    </svg>
                    Your Computers
                </a>
                <a href="/backup" class="block mt-4 @if(request()->routeIs('backup')) font-bold @endif">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M5.5 13a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 13H11V9.413l1.293 1.293a1 1 0 001.414-1.414l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13H5.5z" />
                        <path d="M9 13h2v5a1 1 0 11-2 0v-5z" />
                    </svg>
                    Backup New Computer
                </a>
                <a href="/restore" class="block @if(request()->routeIs('restore')) font-bold @endif">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z" clip-rule="evenodd" />
                    </svg>
                    Restore from Backup
                </a>
                <a href="/payment" class="block mt-4 @if(request()->routeIs('payment')) font-bold @endif">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" />
                        <path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd" />
                    </svg>
                    Payment Method
                </a>
                @if (!auth()->user()->leader_id && auth()->user()->groups)
                    <a href="/group" class="block @if(request()->routeIs('group')) font-bold @endif">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                        </svg>
                        My Group
                    </a>
                @endif
                <a href="/settings" class="block @if(request()->routeIs('settings')) font-bold @endif">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
                    </svg>
                    Settings
                </a>
                <a href="https://blobbackup.com/support" target="_blank" class="block mt-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                    </svg>
                    Help
                </a>
            </div>
            <div class="flex-1 pt-8">
                <div class="max-w-4xl mx-auto">
                    {{ $slot }}
                </div>
            </div>
        </main>
        @if (session('welcome'))
            <script>
                document.getElementById("start-backing-up").onclick = () => {
                    document.getElementById("welcome").classList.add("hidden");
                    return false;
                };
            </script>
        @endif
    </body>
</html>