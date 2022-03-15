@section('title')
    Dashboard
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">
        @if (auth()->user()->is($user))
            Your Computers
        @else
            Computers <span class="font-normal text-base ml-4 pl-4 border-l border-gray-300"> {{ $user->email }}</span>
        @endif
    </h1>
    <section class="grid grid-cols-2 gap-8 my-8">
        @if($user->computers->count() > 0)
            @foreach($user->computers as $computer)
                <div class="shadow-lg p-6">
                    <h2 class="font-bold">{{ $computer->name }}</h2>
                    <div class="text-gray-600">Selected Files: {{ number_format($computer->last_backed_up_num_files) }} files / {{ Util::formatBytes($computer->last_backed_up_size) }}</div>
                    <div class="text-gray-600">Platform: {{ $computer->operating_system }}</div>
                    @if ($computer->last_backed_up_at)
                        <div class="text-gray-600">Last Backup: {{ Util::timeDelta($computer->last_backed_up_at, new DateTime()) }} ago</div>
                    @else
                        <div class="text-gray-600">Last Backup: Never</div>
                    @endif
                    <div class="text-gray-600 mt-2">
                        @if (auth()->user()->is($user))
                            <a href="/restore" class="mr-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M2 9.5A3.5 3.5 0 005.5 13H9v2.586l-1.293-1.293a1 1 0 00-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 15.586V13h2.5a4.5 4.5 0 10-.616-8.958 4.002 4.002 0 10-7.753 1.977A3.5 3.5 0 002 9.5zm9 3.5H9V8a1 1 0 012 0v5z" clip-rule="evenodd" />
                                </svg>
                                Restore
                            </a>
                        @endif
                        <a href="/deletecomputer/{{ $computer->id }}">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                            </svg>
                            Delete
                        </a>
                    </div>
                </div>
            @endforeach
        @else
            <div class="text-gray-600">
                @if (auth()->user()->is($user))
                    You don't have any computers yet.
                @else
                    This user doesn't have any computers yet.
                @endif
            </div>
        @endif
    </section>
</x-app-layout>
