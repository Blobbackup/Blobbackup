@section('title')
    {{ $page->title }}
@endsection
@extends('_layouts.main')

@section('body')
<style>
#content p {
    margin-top: 1rem;
}
#content h1 {
    margin-top: 2rem;
    font-weight: bold;
    font-size: 1.5rem;
    line-height: 2rem;
}
#content li {
    list-style-type: disc;
    margin-left: 2rem;
}
</style>
<h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-16 text-center">{{ $page->title }}</h1>
<h2 class="text-xl md:text-2xl text-gray-600 mt-2 text-center">{{ date('F j, Y', $page->date) }} by {{ $page->author }}</h2>
<div class="mx-auto max-w-4xl text-gray-600 text-lg mt-8 md:mt-16" id="content">
    @yield('content')
</div>
@endsection
