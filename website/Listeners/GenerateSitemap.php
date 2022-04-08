<?php namespace App\Listeners;

use TightenCo\Jigsaw\Jigsaw;
use samdark\sitemap\Sitemap;

class GenerateSitemap
{
    public function handle(Jigsaw $jigsaw)
    {
        $baseUrl = $jigsaw->getConfig('baseUrl');
        $sitemap = new Sitemap($jigsaw->getDestinationPath() . '/sitemap.xml');

        collect($jigsaw->getOutputPaths())->each(function ($path) use ($baseUrl, $sitemap) {
            if (!$this->isAsset($path) && !$this->isAd($path)) {
                $sitemap->addItem($baseUrl . $path);
            }
        });

        $sitemap->write();

        $robots = "User-agent: *\nsitemap: https://blobbackup.com/sitemap.xml";
        $robotsPath = $jigsaw->getDestinationPath() . '/robots.txt';

        $robotsFile = fopen($robotsPath, "w");
        fwrite($robotsFile, $robots);
        fclose($robotsFile);
    }

    public function isAd($path)
    {
        return str_starts_with($path, '/ads');
    }

    public function isAsset($path)
    {
        return str_starts_with($path, '/assets');
    }
}