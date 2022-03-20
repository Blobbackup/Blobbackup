@section('title')
    My Group
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold" id="mac">
        My Group
        <span class="font-normal text-sm ml-4 pl-4 border-l border-gray-300">
            @if (auth()->user()->accepting_users)
                <span class="text-green-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1 -mt-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                    </svg>
                    Accepting New Users
                </span>
            @else
                <span class="text-gray-500">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1 -mt-1" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                    </svg>
                    Not Accepting New Users
                </span>
            @endif
            <form method="POST" action="/toggleaccepting" class="inline-block ml-2">
                @csrf
                <button type="submit" class="underline text-blue-500">
                    @if (auth()->user()->accepting_users)
                        (Close)
                    @else
                        (Open)
                    @endif
                </button>
            </form>
        </span>
    </h1>
    @if($errors->any())
        <div class="text-red-600 mt-8 text-sm">
            {{ $errors->first() }}
        </div>
    @endif
    @if(session('message'))
        <div class="text-green-500 mt-8 text-sm">
            {{ session('message') }}
        </div>
    @endif
    <div class="shadow-lg mt-8 p-6">
        <div class="text-gray-600 mb-4">Users</div>
        @if ($users->count() == 0)
            <div class="text-gray-600 border-t border-gray-300 py-2">
                You don't have any group users.
            </div>
        @else
            @foreach ($users as $user)
                @if ($user->status == 'pending')
                    <div class="text-gray-600 border-t border-gray-300 py-2 flex">
                        <div class="flex-1">
                            {{ $user->email }} (pending)
                        </div>
                        <form method="POST" action="/judgeuser/{{ $user->id }}" class="flex-initial">
                            @csrf
                            <button type="submit" name="judgement" value="accept" class="mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block -mt-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                                </svg>
                                Accept
                            </button>
                            <button type="submit" name="judgement" value="reject" class="mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block -mt-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                                Reject
                            </button>
                        </form>
                    </div>
                @else
                    <div class="text-gray-600 border-t border-gray-300 py-2 flex">
                        <div class="flex-1">
                            {{ $user->email }}
                        </div>
                        <div class="flex-initial">
                            <a href="/computers/{{ $user->id }}" class="mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block -mt-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
                                </svg>
                                Computers ({{ $user->computers->count() }})
                            </a>
                            <a href="/deleteuser/{{ $user->id }}" class="mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block -mt-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                                </svg>
                                Delete
                            </a>
                        </div>
                    </div>
                @endif
            @endforeach
        @endif
    </div>
    @if (auth()->user()->accepting_users)
        <div class="shadow-lg mt-8 p-6">
            <div class="text-gray-600">Invite Users</div>
            <div class="text-gray-600 mt-4">
                Send the link below to invite new users into your group.
            </div>
            <div class="bg-gray-100 p-4 text-gray-600 mt-2 flex">
                <a href="{{ $groupUrl }}" target="_blank" class="underline text-blue-500 flex-1" id="copy_link">{{ $groupUrl }}</a>
                <button class="inline-block flex-initial text-sm" id="copy_button">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 -mt-1 inline-block" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M8 7v8a2 2 0 002 2h6M8 7V5a2 2 0 012-2h4.586a1 1 0 01.707.293l4.414 4.414a1 1 0 01.293.707V15a2 2 0 01-2 2h-2M8 7H6a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2v-2" />
                    </svg>
                    Copy
                </button>
            </div>
        </div>
    @endif
    <script>
        document.getElementById("copy_button").onclick = () => {
            navigator.clipboard.writeText(document.getElementById("copy_link").getAttribute("href"));
        }
    </script>
</x-app-layout>