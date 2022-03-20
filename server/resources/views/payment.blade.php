@section('title')
    Payment Method
@endsection
<x-app-layout>
    <h1 class="text-2xl font-bold">Payment Method</h1>
    <div class="shadow-lg mt-8 p-6">
        @if (auth()->user()->leader_id)
            <div class="text-gray-600">
                Payment is handled by your group owner ({{ \App\Models\User::find(auth()->user()->leader_id)->email }}).
            </div>
        @else
            @if (!auth()->user()->subscribed())
                <div class="text-gray-600">You haven't added a payment method yet.</div>
                <div class="text-gray-600 mt-2">
                    <x-paddle-button :url="$payLink" data-theme="none">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z" />
                            <path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd" />
                        </svg>
                        Add Payment Method
                    </x-paddle-button>
                </div>
            @else
                <div class="text-gray-600">
                    You will be billed ${{ auth()->user()->computersToBill() * Util::$perComputerPrice }} / month (computers: {{ auth()->user()->computersToBill() }}).
                </div>
                <div class="text-gray-600 mt-2">
                    @if (auth()->user()->subscription()->paymentMethod() == 'card')
                        Your current payment method is a {{ auth()->user()->subscription()->cardBrand() }} card ending in {{ auth()->user()->subscription()->cardLastFour() }}
                        that expires on {{ auth()->user()->subscription()->cardExpirationDate() }}.
                    @else
                        Your current payment method is a PayPal account.
                    @endif
                </div>
                <div class="text-gray-600 mt-2">
                    <x-paddle-button :url="$payLink" data-theme="none" data-success="{{ route('payment') }}">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z" />
                            <path fill-rule="evenodd" d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z" clip-rule="evenodd" />
                        </svg>
                        Update Payment Method
                    </x-paddle-button>
                    <form method="POST" action="/deletepayment" class="inline-block">
                        @csrf
                        <a href="" onclick="event.preventDefault(); this.closest('form').submit();" class="ml-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 inline-block mr-1" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                            </svg>
                            Remove
                        </a>
                    </form>
                </div>
            @endif
        @endif
    </div>
</x-app-layout>
