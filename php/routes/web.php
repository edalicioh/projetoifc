<?php
$route[] = [BASE_URL . '/', 'HomeController@index'];
$route[] = [BASE_URL . '/chart/{codeIbge}', 'HomeController@chart'];
return $route;
