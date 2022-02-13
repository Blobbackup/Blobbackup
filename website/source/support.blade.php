@section('title')
    Support
@endsection
@extends('_layouts.main')

@section('body')
<h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-16 text-center">Support</h1>
<section class="mt-4 md:mt-8 text-center">
    <div>
        Email Support: <a href="mailto:support@blobbackup.com" class="underline text-blue-600">support@blobbackup.com</a>
    </div>
    <div class="mt-2">
        Community Support: 
            <a href="https://github.com/blobbackup/blobbackup/issues" class="underline text-blue-600">Github</a> | 
            <a href="https://reddit.com/r/blobbackup" class="underline text-blue-600">Reddit</a>
    </div>
</section>
<h1 class="text-4xl md:text-5xl font-bold mt-8 md:mt-16 text-center">Articles</h1>
<section class="mt-4 md:my-8 text-center">
    @foreach($support as $article)
        <a href="{{ $article->getPath() }}" class="text-blue-600 underline block mt-2">{{ $article->title }}</a>
    @endforeach
</section>
@endsection
