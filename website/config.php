<?php

return [
    'production' => false,
    'baseUrl' => '',
    'title' => 'Blobbackup',
    'description' => 'Private, Secure Computer Backups.',
    'collections' => [
        'posts' => [
            'path' => '/blog/{filename}',
            'sort' => '-date'
        ]
    ],
];
