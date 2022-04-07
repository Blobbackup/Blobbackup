<?php

return [
    'production' => false,
    'baseUrl' => 'https://blobbackup.com',
    'title' => 'Blobbackup',
    'description' => 'Private, Secure Computer Backups.',
    'collections' => [
        'posts' => [
            'path' => '/blog/{filename}',
            'sort' => '-date'
        ],
        'support' => [
            'path' => '/support/{filename}',
            'sort' => '-date'
        ]
    ],
];
