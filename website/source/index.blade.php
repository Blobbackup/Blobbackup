@section('title')
    Private, Secure Computer Backups
@endsection

@extends('_layouts.main')

@section('body')
<div class="mx-auto max-w-5xl p-4">
    <section class="md:flex mt-4 md:mt-8">
        <div class="md:w-1/2 text-center md:text-left my-auto">
            <h1 class="text-3xl md:text-5xl font-bold">Simple Cloud Backup</h1>
            <h2 class="text-xl md:text-2xl text-gray-600 mt-2">
                We back up your entire computer to the cloud for 
                ${{ $page->perComputerPrice }}/month flat. No hidden fees or price tiers. All of your files. 
                For the price of a cup of coffee. <strong>Your privacy, guaranteed.</strong>
            </h2>
            <a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try Free for {{ $page->trialLengthDays }} Days</a>
            <div class="text-gray-600 mt-4 text-xs md:text-base">
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
        <div class="md:w-1/2 px-4 md:px-16 mt-8 md:my-auto">
            <img src="/assets/images/hero.webp"/>
        </div>
    </section>
    <div class="max-w-4xl mx-auto text-center mt-4 md:mt-8">
        <h1 class="text-2xl md:text-4xl font-bold">Don't Risk Losing Your Files</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-2">
            Remember that time you almost spilled coffee on your keyboard?
            Or that time you left your laptop in your car? Liquid damage and
            computer theft are just two of the many ways you could lose your 
            important files. Here are the <strong>Top 9 Causes of Data Loss.</strong>
        </h2>
    </div>
    <section class="mt-8 md:mt-16 grid md:grid-cols-3 gap-8 text-center md:text-left">
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                1. Accidental Deletion
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                People accidentally deleting or overwriting
                important files is the most common form of data loss.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 100 100" fill="currentColor" width="100" height="100" xml:space="preserve">
                    <path d="M50 10c-5.521 0-10 4.479-10 10v5h20v-5c0-5.521-4.479-10-10-10zM90 56.666V50H69.434c.146-1.199.257-2.396.342-3.602 9.567-1.494 16.892-9.748 16.892-19.732H80c0 6.205-4.261 11.373-10 12.861V30H30v9.527c-5.742-1.488-10-6.656-10-12.861h-6.667c0 9.984 7.324 18.238 16.892 19.732A69.07 69.07 0 0 0 30.567 50H10v6.666h21.722a69.396 69.396 0 0 0 1.403 5.367c-9.658 4.008-16.458 13.523-16.458 24.633h6.666c0-8.236 4.98-15.299 12.084-18.365C38.747 76.184 43.581 83.58 50 90c6.419-6.42 11.253-13.816 14.583-21.699 7.104 3.068 12.084 10.133 12.084 18.365h6.666c0-11.109-6.8-20.625-16.458-24.633.55-1.773.999-3.564 1.403-5.367H90z"/>
                </svg>
                2. Virus & Ransomware
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Downloading the wrong file or using insecure Wifi 
                can infect your computer with viruses or ransomware.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13 7H7v6h6V7z" />
                    <path fill-rule="evenodd" d="M7 2a1 1 0 012 0v1h2V2a1 1 0 112 0v1h2a2 2 0 012 2v2h1a1 1 0 110 2h-1v2h1a1 1 0 110 2h-1v2a2 2 0 01-2 2h-2v1a1 1 0 11-2 0v-1H9v1a1 1 0 11-2 0v-1H5a2 2 0 01-2-2v-2H2a1 1 0 110-2h1V9H2a1 1 0 010-2h1V5a2 2 0 012-2h2V2zM5 5h10v10H5V5z" clip-rule="evenodd" />
                </svg>
                3. Hard Drive Crash
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Both classic hard drives and modern solid
                state drives can and do fail through no 
                fault of the user.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
                </svg>
                4. Power Outages
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Sudden power outages can corrupt your files
                as well as various computer hardware components.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10 1.944A11.954 11.954 0 012.166 5C2.056 5.649 2 6.319 2 7c0 5.225 3.34 9.67 8 11.317C14.66 16.67 18 12.225 18 7c0-.682-.057-1.35-.166-2.001A11.954 11.954 0 0110 1.944zM11 14a1 1 0 11-2 0 1 1 0 012 0zm0-7a1 1 0 10-2 0v3a1 1 0 102 0V7z" clip-rule="evenodd" />
                </svg>
                5. Computer Theft
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                If you travel with your laptop or work in 
                public spaces often (eg: cafes), you're 
                vulnerable to computer theft.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg version="1.0" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 100 100" fill="currentColor" width="100" height="100" xml:space="preserve">
                    <path d="M80 36.667H10V60c0 9.434 4.358 17.839 11.165 23.333H10V90h60v-6.667H58.838a29.967 29.967 0 0 0 10.394-16.666H80c5.521 0 10-4.479 10-10v-10c0-5.521-4.479-10-10-10zm3.333 20A3.333 3.333 0 0 1 80 60H70V43.333h10a3.338 3.338 0 0 1 3.333 3.334v10zM36.667 10h6.666v20h-6.666zM23.333 10H30v20h-6.667zM50 10h6.667v20H50z"/>
                </svg>
                6. Liquid Damage
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Spilling coffee or water on your computer can cause a 
                short circuit, making data loss very likely. 
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M12.395 2.553a1 1 0 00-1.45-.385c-.345.23-.614.558-.822.88-.214.33-.403.713-.57 1.116-.334.804-.614 1.768-.84 2.734a31.365 31.365 0 00-.613 3.58 2.64 2.64 0 01-.945-1.067c-.328-.68-.398-1.534-.398-2.654A1 1 0 005.05 6.05 6.981 6.981 0 003 11a7 7 0 1011.95-4.95c-.592-.591-.98-.985-1.348-1.467-.363-.476-.724-1.063-1.207-2.03zM12.12 15.12A3 3 0 017 13s.879.5 2.5.5c0-1 .5-4 1.25-4.5.5 1 .786 1.293 1.371 1.879A2.99 2.99 0 0113 13a2.99 2.99 0 01-.879 2.121z" clip-rule="evenodd" />
                </svg>
                7. Sudden Disasters
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                From tornadoes to fire, disasters can happen unexpectedly.
                And when they do, data loss is inevitable.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                8. Corrupt Software
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Improper software failures and shutdowns at the wrong time can 
                cause serious issues for your data.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                </svg>
                9. Hackers & Insiders
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Bad actors on the internet or even inside your
                home/business can cause harm to your important files.
            </p>
        </div>
    </section>
    <div class="max-w-4xl mx-auto text-center mt-8 md:mt-16">
        <h1 class="text-2xl md:text-4xl font-bold">How Blobbackup Works</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-2">
            Blobbackup is an app for your Mac or PC that protects you from data loss by 
            automatically backing up your files to the cloud. Unlike others, we're built 
            on a foundation of <strong>Privacy, Security and Open Source Transparency.</strong>
        </h2>
    </div>
    <section class="mt-8 md:mt-16 grid md:grid-cols-3 gap-8 text-center md:text-left">
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
        <div>
            <h4 class="text-xl font-bold">
                <a href="/blog/getting-started-with-blobbackup">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" />
                    </svg>
                    Perfect for Famililes
                </a>
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Pay for and manage your family's computer backups 
                from our simple web admin panel.
            </p>
        </div>
        <div>
            <h4 class="text-xl font-bold">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline-block -mt-1 mr-1 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z" clip-rule="evenodd" />
                    <path d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z" />
                </svg>
                Perfect for Small Business
            </h4>
            <p class="text-lg text-gray-600 mt-2">
                Easily protect your employees' computers while respecting 
                their personal privacy.
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
                for as long as you need.
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
    </section>
    <section class="text-center mt-16">
        <h3 class="text-3xl font-bold">${{ $page->perComputerPrice }} / Month / Computer</h3>
        <h4 class="text-lg text-gray-600 mt-2">Start protecting your computer data today.</h4>
        <a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try Free for {{ $page->trialLengthDays }} Days</a>
    </section>
</div>
@endsection
