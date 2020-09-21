<?php
$route[] = ['/', 'HomeController@index'];
$route[] = ['/chart/{codeIbge}', 'HomeController@chart'];
return $route;
