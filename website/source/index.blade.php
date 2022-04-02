@section('title')
    Private, Secure Computer Backups
@endsection

@extends('_layouts.main')

@section('body')
<section class="md:flex mt-4 md:mt-8">
    <div class="md:w-1/2 text-center md:text-left">
        <h1 class="text-4xl md:text-5xl font-bold mt-0 md:mt-10">Private, Secure Computer Backups</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-2">Securely backup your computers to the cloud without compromising your privacy.</h2>
        <a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try it for Free</a>
        <div class="text-gray-400 mt-4 text-xs md:text-base">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
            Open Source
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 ml-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
            Encrypted
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 ml-2" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
            </svg>
            Mac & Windows
        </div>
    </div>
    <div class="md:w-1/2 px-4 md:px-16 mt-8 md:mt-0">
        <img src="/assets/images/hero.png"/>
    </div>
</section>
<section class="mt-4 md:mt-8 grid md:grid-cols-3 gap-8 text-center md:text-left">
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M5.5 16a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 16h-8z" />
            </svg>
            Secure Offsite Cloud
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Data is stored in datacenters with 24/7 staff, 
            biometric security and redundant power.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <a href="/blog/what-is-end-to-end-encryption">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
                </svg>
                Private by Design
            </a>
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Everything is encrypted with your password and we never store
            or transmit your password.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <a href="/blog/open-source-software-vs-open-source-development">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                Fully Open Source
            </a>
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            All code is available for analysis, audit and review.
            There are no tricks under our sleeves.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <a href="/blog/getting-started-with-blobbackup">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 3a1 1 0 012 0v5.5a.5.5 0 001 0V4a1 1 0 112 0v4.5a.5.5 0 001 0V6a1 1 0 112 0v5a7 7 0 11-14 0V9a1 1 0 012 0v2.5a.5.5 0 001 0V4a1 1 0 012 0v4.5a.5.5 0 001 0V3z" clip-rule="evenodd" />
                </svg>
                Easy and Simple
            </a>
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Sign up for an account and start backing up your computer 
            within a few minutes. 
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
            </svg>
            Smart and Automatic
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Backups happen seamlessly in the background without hogging your 
            computer's resources.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
            </svg>
            Blazing Fast Restores
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Restore from our app as fast as your internet
            allows. No download limits or wait times.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M9 2a2 2 0 00-2 2v8a2 2 0 002 2h6a2 2 0 002-2V6.414A2 2 0 0016.414 5L14 2.586A2 2 0 0012.586 2H9z" />
                <path d="M3 8a2 2 0 012-2v10h8a2 2 0 01-2 2H5a2 2 0 01-2-2V8z" />
            </svg>
            Extended File History
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Old versions of files and deleted files are kept on our secure cloud 
            for up to a full year.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z" clip-rule="evenodd" />
            </svg>
            Simple Monitoring
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Get notified via email when your computer hasn't been backed 
            up for over 2 weeks.
        </p>
    </div>
    <div>
        <h4 class="text-xl font-bold">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
            </svg>
            Full Computer Backups
        </h4>
        <p class="text-lg text-gray-600 mt-2">
            Protect all your files including documents, photos, music, movies
            and more.
        </p>
    </div>
</section>
<section class="text-center mt-16">
    <h3 class="text-3xl font-bold">$9 / Month / Computer</h3>
    <h4 class="text-lg text-gray-600 mt-2">Start protecting your computer data today.</h4>
    <a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try it for Free</a>
</section>
@endsection
