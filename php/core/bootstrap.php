<?php

if (getenv('DB_CONNECTION') != null) {
    define('env', getenv());
} else {
    require_once __DIR__ . '/dotenv.php';
    define('env', $_ENV);
}

require_once __DIR__ . '/whoops.php';

$routes = require_once __DIR__ . '/../routes/web.php';
$route = new \Core\Route($routes);

function dd($dump)
{
    echo '<pre>';
    var_dump($dump);
    echo '</pre>';
    die;
}
