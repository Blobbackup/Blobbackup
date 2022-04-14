@section('title')
    Security and Privacy
@endsection
@extends('_layouts.main')

@section('body')
<div class="mx-auto max-w-5xl p-4">
    <div class="mx-auto max-w-lg text-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="mt-4 md:mt-10 h-16 w-16 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
        </svg>
        <h1 class="text-2xl md:text-4xl font-bold mt-4">Secure & Private by Design</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-2">Every design decision in Blobbackup begins with the safety and privacy of your data in mind.</h2>
    </div>
    <div class="flex mt-12 mb-8">
        <div class="flex-1 border-t-4 border-blue-100 mr-4"></div>
        <div class="flex-initial -mt-4 font-bold text-blue-500 text-2xl">Our Promise to You</div>
        <div class="flex-1 border-t-4 border-blue-100 ml-4"></div>
    </div>
    <div class="mx-auto max-w-4xl text-xl text-gray-600 md:text-2xl text-center mt-8">
        The information you store in Blobbackup is encrypted, and only you hold the keys to decrypt it. 
        Blobbackup is designed to protect you from breaches and other threats, and we've made our code
        open source so it can be analzyed by security experts. We can’t see your backup data, 
        so we can’t use it, share it, or sell it.
    </div>
    <div class="flex mt-12">
        <div class="flex-1 border-t-4 border-blue-100"></div>
    </div>
    <div class="max-w-4xl mx-auto text-center mt-8 md:mt-12">
        <h1 class="text-2xl md:text-4xl font-bold">Only You Have Access</h1>
        <h2 class="text-xl md:text-2xl text-gray-600 mt-2">
            Your Blobbackup data is end-to-end encrypted to keep it safe at rest and in transit. 
            Our security recipe starts with AES 256-bit encryption, and we use multiple techniques 
            to make sure only you have access to your information.
        </h2>
    </div>
    <section class="mt-8 md:mt-12 text-center grid md:grid-cols-3 gap-8">
        <div>
            <div class="text-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M18 8a6 6 0 01-7.743 5.743L10 14l-1 1-1 1H6v2H2v-4l4.257-4.257A6 6 0 1118 8zm-6-4a1 1 0 100 2 2 2 0 012 2 1 1 0 102 0 4 4 0 00-4-4z" clip-rule="evenodd" />
                </svg>
            </div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Master Password</h1>
            <p class="text-lg text-gray-600 mt-2">
                Only you know your Master Password: it’s never stored 
                alongside your data or sent over the network.
            </p>
        </div>
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
                <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M9.504 1.132a1 1 0 01.992 0l1.75 1a1 1 0 11-.992 1.736L10 3.152l-1.254.716a1 1 0 11-.992-1.736l1.75-1zM5.618 4.504a1 1 0 01-.372 1.364L5.016 6l.23.132a1 1 0 11-.992 1.736L4 7.723V8a1 1 0 01-2 0V6a.996.996 0 01.52-.878l1.734-.99a1 1 0 011.364.372zm8.764 0a1 1 0 011.364-.372l1.733.99A1.002 1.002 0 0118 6v2a1 1 0 11-2 0v-.277l-.254.145a1 1 0 11-.992-1.736l.23-.132-.23-.132a1 1 0 01-.372-1.364zm-7 4a1 1 0 011.364-.372L10 8.848l1.254-.716a1 1 0 11.992 1.736L11 10.58V12a1 1 0 11-2 0v-1.42l-1.246-.712a1 1 0 01-.372-1.364zM3 11a1 1 0 011 1v1.42l1.246.712a1 1 0 11-.992 1.736l-1.75-1A1 1 0 012 14v-2a1 1 0 011-1zm14 0a1 1 0 011 1v2a1 1 0 01-.504.868l-1.75 1a1 1 0 11-.992-1.736L16 13.42V12a1 1 0 011-1zm-9.618 5.504a1 1 0 011.364-.372l.254.145V16a1 1 0 112 0v.277l.254-.145a1 1 0 11.992 1.736l-1.735.992a.995.995 0 01-1.022 0l-1.735-.992a1 1 0 01-.372-1.364z" clip-rule="evenodd" />
                </svg>
            </div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Transparency</h1>
            <p class="text-lg text-gray-600 mt-2">
                Our team reacts swiftly to reports of bugs/vulnerabilities and 
                communicates transparently.
            </p>
        </div>
        <div>
            <div class="text-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 inline-block text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z" clip-rule="evenodd" />
                </svg>
            </div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Regular Monitoring</h1>
            <p class="text-lg text-gray-600 mt-2">
                We follow best practices to monitor our servers, databases, 
                and cloud storage for anomalies.
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
                    <path fill-rule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clip-rule="evenodd" />
                </svg>
            </div>
            <h1 class="text-2xl md:text-3xl font-bold mt-2">Endpoint Encryption</h1>
            <p class="text-lg text-gray-600 mt-2">
                Encryption happens exclusively at the device level
                before uploading data to Blobbackup's cloud.
            </p>
        </div>
    </section>
    <section class="text-center mt-8 md:mt-16 mx-auto max-w-lg">
        <h3 class="text-3xl font-bold">${{ $page->perComputerPrice }} / Month / Computer</h3>
        <h4 class="text-lg text-gray-600 mt-2">
            Fast email support and {{ $page->perComputerGB }} GB of storage per computer included. Start protecting your computer data today.
        </h4>
        <a href="https://app.blobbackup.com/register" class="font-bold text-lg text-white bg-blue-500 rounded-full px-4 py-2 inline-block mt-4">Try Free for {{ $page->trialLengthDays }} Days</a>
        <p class="text-center text-gray-600 text-sm mt-2">No card required. Cancel anytime.</p>
    </section>
</div>
@endsection
