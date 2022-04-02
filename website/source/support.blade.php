@section('title')
    Support
@endsection
@extends('_layouts.main')

@section('body')
<div class="grid md:grid-cols-2 text-center">
    <div>
        <svg xmlns="http://www.w3.org/2000/svg" class="text-blue-500 h-12 w-12 inline-block mt-4 md:mt-10" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
        </svg>
        <h1 class="text-4xl md:text-5xl font-bold md:mt-4">How-to Guides</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-4 text-center">New to Blobbackup? Start here.</h2>
        <a href="/support/getting-started-with-blobbackup" class="text-xl text-blue-600 underline mt-2 block">Getting Started With Blobbackup</a>
        <a href="/support/how-to-restore-your-data" class="text-xl text-blue-600 underline mt-2 block">How to Restore Your Data</a>
        <a href="/support/blobbackup-settings" class="text-xl text-blue-600 underline mt-2 block">Change Blobbackup App Settings</a>
    </div>
    <div>
        <svg xmlns="http://www.w3.org/2000/svg" class="text-blue-500 h-12 w-12 inline-block mt-8 md:mt-10" viewBox="0 0 20 20" fill="currentColor">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
        </svg>
        <h1 class="text-4xl md:text-5xl font-bold md:mt-4">Support</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-4 text-center">
            We are here to help! Email us at <a href="mailto:support@blobbackup.com" class="underline">support@blobbackup.com</a>.
        </h2>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-4">
            You can also check out one of our community driven support fourms: 
            <a href="https://reddit.com/r/blobbackup" target="_blank" class="underline">Reddit</a>, 
            <a href="https://github.com/blobbackup/blobbackup" target="_blank" class="underline">Github</a>.
        </h2>
    </div>
</div>
<div class="text-center">
    <svg xmlns="http://www.w3.org/2000/svg" class="text-blue-500 h-12 w-12 inline-block mt-8 md:mt-16" viewBox="0 0 20 20" fill="currentColor">
        <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
    </svg>
    <h1 class="text-4xl md:text-5xl font-bold md:mt-4">All Articles</h1>
    <section class="text-xl mt-4 md:my-8 grid md:grid-cols-3 md:gap-y-2 md:gap-x-4">
        @foreach($support as $article)
            <a href="{{ $article->getPath() }}" class="text-ellipsis truncate text-blue-600 underline block mt-2">{{ $article->title }}</a>
        @endforeach
    </section>
</div>
@endsection
