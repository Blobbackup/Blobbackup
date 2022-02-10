@section('title')
    Company
@endsection
@extends('_layouts.main')

@section('body')
<section class="md:flex mt-4 md:mt-8">
    <div class="md:w-2/5 px-16 py-8 md:mt-0">
        <div class="rounded-full overflow-hidden">
            <img src="/assets/images/bimba.jpeg"/>
        </div>
    </div>
    <div class="md:w-3/5 px-4 md:px-0">
        <h1 class="text-4xl md:text-5xl font-bold mt-0 md:mt-10 text-center md:text-left">
            <img src="/assets/images/wave.png" class="w-16 h-16 -mt-3 mr-1 inline-block"/>
            Hi There!
        </h1>
        <p class="text-xl md:text-2xl text-gray-600 mt-8">
            I'm Bimba, founder of Blobbackup.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            It's just me right now. One guy who cares about computer backups, kind of doing everything.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            If that concerns you a little, I don't blame you.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            You might ask: should I trust you with my computer data? What if something happens to you? Will this company be around next year?
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            Those are very good questions.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            In some ways, there is no getting around it. It's risky to trust any new, small company (in general but especially when it comes to backups).
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            All I can say is that I don't take my responsibility to protect your data lightly.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            I've taken great pains to make offsite computer backups as easy, reliable and private as possible.
            You can read the <a href="/blog" class="text-blue-600 underline">blog</a> for the details but in short:
        </p>
        <ul class="text-xl md:text-2xl text-gray-600 list-disc ml-8 mt-4">
            <li>
                Blobbackup is end to end <strong>encrypted</strong> so your privacy won't be compromised.
            </li>
            <li>
                Blobbackup is <strong>open source</strong> so
                the public can analyze the code and more importantly, retain access to their data if the company
                disappears.
            </li>
            <li>
                Blobbackup is extremely <strong>simple</strong> and easy to use.
            </li>
        </ul>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            Computer backups are an essential part of good digital hygiene. I had trouble finding a service
            that matched my needs so I decided to build one myself. 
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            Blobbackup has already saved me a few times from some data loss tragedies and I hope that it'll be able to
            do the same for some of you.
        </p>
        <p class="text-xl md:text-2xl text-gray-600 mt-4">
            - Bimba
        </p>
    </div>
</section>
@endsection
