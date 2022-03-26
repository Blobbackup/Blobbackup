@section('title')
    Personal Backup
@endsection
@extends('_layouts.main')

@section('body')
<div class="mx-auto max-w-lg text-center">
    <h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-10">Personal Backup</h1>
    <h2 class="text-xl md:text-2xl text-gray-600 mt-2">Securely backup your personal computers to the cloud without compromising your privacy.</h2>
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
<section class="mt-8 md:mt-16 text-center grid md:grid-cols-3 gap-8">
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M5.5 16a3.5 3.5 0 01-.369-6.98 4 4 0 117.753-1.977A4.5 4.5 0 1113.5 16h-8z" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Secure Offsite Cloud</h1>
        <p class="text-lg text-gray-600 mt-2">
            Data is stored in datacenters with 24/7 staff, biometric 
            security and redundant power.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Private by Design</h1>
        <p class="text-lg text-gray-600 mt-2">
            Everything is encrypted with your password and we never store
            or transmit your password.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Perfect for Families</h1>
        <p class="text-lg text-gray-600 mt-2">
            Pay for and manage all family computer backups from 
            our simple web admin panel.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Fully Open Source</h1>
        <p class="text-lg text-gray-600 mt-2">
            All code is available for analysis, audit and review.
            There are no tricks under our sleeves.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 3a1 1 0 012 0v5.5a.5.5 0 001 0V4a1 1 0 112 0v4.5a.5.5 0 001 0V6a1 1 0 112 0v5a7 7 0 11-14 0V9a1 1 0 012 0v2.5a.5.5 0 001 0V4a1 1 0 012 0v4.5a.5.5 0 001 0V3z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Easy and Simple</h1>
        <p class="text-lg text-gray-600 mt-2">
            Sign up for an account and start backing up your computer 
            within a few minutes.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Smart and Automatic</h1>
        <p class="text-lg text-gray-600 mt-2">
            Backups happen seamlessly in the background without hogging your 
            computer's resources.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Blazing Fast Restores</h1>
        <p class="text-lg text-gray-600 mt-2">
            Restore from our app as fast as your internet
            allows. No download limits or wait times.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M9 2a2 2 0 00-2 2v8a2 2 0 002 2h6a2 2 0 002-2V6.414A2 2 0 0016.414 5L14 2.586A2 2 0 0012.586 2H9z" />
                <path d="M3 8a2 2 0 012-2v10h8a2 2 0 01-2 2H5a2 2 0 01-2-2V8z" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Extended File History</h1>
        <p class="text-lg text-gray-600 mt-2">
            Old versions of files and deleted files are kept on our secure cloud 
            for up to a full year.
        </p>
    </div>
    <div>
        <div class="text-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1 class="text-2xl md:text-3xl font-bold mt-2">Full Backups</h1>
        <p class="text-lg text-gray-600 mt-2">
            Protect all your computer data including documents, photos, music, movies
            and more.
        </p>
    </div>
</section>
<section class="text-center md:mt-16">
    <h1 class="text-4xl md:text-5xl font-bold mt-8 md:mt-16 text-center">$9 / Month Flat</h1>
    <h2 class="text-xl md:text-2xl text-gray-600 mt-2 text-center">Per computer. All features included.</h2>
    <div class="text-center"><a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try Free for 30 Days</a></div>
    <p class="text-center text-gray-600 text-sm mt-2">No card required. Cancel anytime.</p>
    <section class="mt-8 md:mt-16 text-center grid md:grid-cols-3 gap-8">
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Email Support</h1>
            <p class="text-lg text-gray-600 mt-2">
                Your subscription includes access to fast technical support
                directly with our engineers.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">5 TB per Computer</h1>
            <p class="text-lg text-gray-600 mt-2">
                We charge you $9 / month per computer. Each computer is allowed to backup
                up to 5 TB of data.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Simple Monitoring</h1>
            <p class="text-lg text-gray-600 mt-2">
                Get notified via email when your computer hasn't been backed 
                up for over 2 weeks.
            </p>
        </div>
    </section>
    <h1 class="text-4xl md:text-5xl font-bold mt-8 md:mt-16 text-center">Common Questions</h1>
    <section class="mt-8 max-w-2xl mx-auto md:mt-16 text-center grid gap-8">
        <div>
            <h1 class="text-xl md:text-2xl font-bold mt-2">
                Can your employees see my files?
            </h1>
            <p class="text-lg text-gray-600 mt-2">
                No. All your files are <a href="/blog/what-is-end-to-end-encryption" class="text-blue-600 underline">encrypted</a> before it leaves your computer with your password. Your password is never stored (or even sent) to our servers and we use state of the art encryption algorithms.
            </p>
        </div>
        <div>
            <h1 class="text-xl md:text-2xl font-bold mt-2">
                Can I pay yearly? What are the payment options?
            </h1>
            <p class="text-lg text-gray-600 mt-2">
                We only offer monthly billing at this time. We will bill you $9 per computer every month after your trial ends. 
                We accept payment via credit card, debit card and PayPal. We don't accept orders, checks, ACH/wire or 
                cryptocurrency.
            </p>
        </div>
        <div>
            <h1 class="text-xl md:text-2xl font-bold mt-2">
                Are taxes included in the price?
            </h1>
            <p class="text-lg text-gray-600 mt-2">
                No. Any taxes we collect are in addition to the per computer price. Whether or not we collect tax and how much
                depends on your jurisdiction.
            </p>
        </div>
        <div>
            <h1 class="text-xl md:text-2xl font-bold mt-2">
                Will I be charged when my trial is up?
            </h1>
            <p class="text-lg text-gray-600 mt-2">
                No. We don't ask for your credit card up front, so you'll only be charged when you decide you’re ready. If you want to continue after your trial, we'll ask for payment details. If not — cancel with a click, no questions asked.
            </p>
        </div>
        <div>
            <h1 class="text-xl md:text-2xl font-bold mt-2">
                What if I have more questions?
            </h1>
            <p class="text-lg text-gray-600 mt-2">
                We'd be happy <a href="/support" class="text-blue-600 underline">to answer them</a>.
            </p>
        </div>
    </section>
</section>
@endsection
