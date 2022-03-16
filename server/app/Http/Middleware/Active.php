<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

class Active
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure(\Illuminate\Http\Request): (\Illuminate\Http\Response|\Illuminate\Http\RedirectResponse)  $next
     * @return \Illuminate\Http\Response|\Illuminate\Http\RedirectResponse
     */
    public function handle(Request $request, Closure $next)
    {
        if (!auth()->check())
            return response('', 400);
        $user = auth()->user();
        if ($user->status == 'active')
            return $next($request);
        if ($user->status == 'pending' && $user->onTrial())
            return $next($request);
        auth()->logout();
        if (Str::contains($request->url(), '/api'))
            return response('Invalid credentials', 400);
        return back()->withErrors('Invalid credentials');
    }
}
