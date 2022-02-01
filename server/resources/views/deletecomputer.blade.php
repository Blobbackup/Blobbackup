@section('title')
    Delete Computer
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">Delete Computer</h1>
    <form method="POST" action="/deletecomputer/{{ $computer->id }}" class="text-gray-600 my-8">
        @csrf
        <div>
            Are you sure you want to delete the computer "{{ $computer->name }}"?
        </div>
        <div class="mt-4">
            All of your backup data for this computer will be permanently deleted!
        </div>
        <div class="mt-4">
            <button type="submit">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                Delete
            </button>
            <a href="/dashboard" class="ml-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M13.477 14.89A6 6 0 015.11 6.524l8.367 8.368zm1.414-1.414L6.524 5.11a6 6 0 018.367 8.367zM18 10a8 8 0 11-16 0 8 8 0 0116 0z" clip-rule="evenodd" />
                </svg>
                Cancel
            </a>
        </div>
    </form>
</x-app-layout>
