@section('title')
    Pricing
@endsection
@extends('_layouts.main')

@section('body')
<div class="mx-auto max-w-5xl p-4">
    <h1 class="text-4xl md:text-5xl font-bold mt-4 md:mt-16 text-center">${{ $page->perComputerPrice }} / Month</h1>
    <h2 class="text-xl md:text-2xl text-gray-600 mt-2 text-center">Per computer. All features included.</h2>
    <div class="text-center"><a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try Free for {{ $page->trialLengthDays }} Days</a></div>
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
            <h1 class="text-2xl md:text-3xl font-bold mt-2">{{ $page->perComputerGB }} GB per Computer</h1>
            <p class="text-lg text-gray-600 mt-2">
                We charge you ${{ $page->perComputerPrice }} / month per computer. Each computer is allowed to backup
                up to {{ $page->perComputerGB }} GB of data.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Secure Offsite Cloud</h1>
            <p class="text-lg text-gray-600 mt-2">
                Data is stored in datacenters with 24/7 staff, biometric 
                security and redundant power.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Extended File History</h1>
            <p class="text-lg text-gray-600 mt-2">
                Old versions of files and deleted files are kept on our secure cloud 
                for up to a full year.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Simple Monitoring</h1>
            <p class="text-lg text-gray-600 mt-2">
                Get notified via email when your computer hasn't been backed 
                up for over 2 weeks.
            </p>
        </div>
        <div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Full Backups</h1>
            <p class="text-lg text-gray-600 mt-2">
                Protect all your files including documents, photos, music, movies
                and more.
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
                We only offer monthly billing at this time. We will bill you ${{ $page->perComputerPrice }} per computer every month after your trial ends. 
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
</div>
@endsection
