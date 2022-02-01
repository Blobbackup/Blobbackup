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
</style>
<h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-16 text-center">{{ $page->title }}</h1>
<h2 class="text-xl md:text-2xl text-gray-600 mt-2 text-center">Last updated: {{ date('F j, Y', $page->updated_date) }}</h2>
<div class="mx-auto max-w-4xl text-gray-600 text-lg mt-8 md:mt-16" id="content">
    @yield('content')
</div>
@endsection
