@section('title')
    Blog
@endsection
@extends('_layouts.main')

@section('body')
<div class="mx-auto max-w-6xl p-4">
    <h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-10 text-center">Blobbackup Blog</h1>
    <h2 class="text-xl md:text-2xl text-gray-600 mt-2 text-center">Digital Hygiene, Stories and Product News.</h2>
    <section class="grid md:grid-cols-3 gap-8 mt-8 md:mt-16">
        @foreach($posts as $post)
        <div>
            <h4 class="text-ellipsis truncate text-xl font-bold"><a href="{{ $post->getPath() }}">{{ $post->title }}</a></h4>
            <h5 class="text-gray-600 mt-4 text-sm">{{ date('F j, Y', $post->date) }} by {{ $post->author }}</h5>
            <p class="text-gray-600 mt-4 text-lg">
                {{ $post->description }}
            </p>
            <a href="{{ $post->getPath() }}" class="underline text-blue-600 inline-block mt-4">Continue reading</a>
        </div>
        @endforeach
    </section>
</div>
@endsection
