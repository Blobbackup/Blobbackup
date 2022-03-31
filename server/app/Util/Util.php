<?php

namespace App\Util;

use Illuminate\Support\Facades\Mail;

class Util
{
    public static $perComputerPrice = 9;
    public static $clientVersion = "1.1.5";

    public static function formatBytes($size, $precision = 2)
    {
        if (!$size)
            return '0 B';
            
        $base = log($size, 1024);
        $suffixes = array('B', 'KB', 'MB', 'GB', 'TB');   
    
        return round(pow(1024, $base - floor($base)), $precision) .' '. $suffixes[floor($base)];
    }

    public static function timeDelta(\DateTime $from, \DateTime $now)
    {
        $delta = $from->diff($now);
        if ($delta->days > 1)
            return $delta->days . ' days';
        elseif ($delta->days == 1)
            return '1 day';
        elseif ($delta->h > 1)
            return $delta->h . ' hours';
        elseif ($delta->h == 1)
            return '1 hour';
        else return $delta->i . ' minutes';
    }

    public static function sendEmail(string $email, string $subject, string $content)
    {
        Mail::send(['html' => 'genericemail'], ['content' => $content], function ($message) use ($email, $subject) {
            $message->to($email)->subject($subject);
        });
    }
}