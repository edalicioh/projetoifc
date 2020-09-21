<?php

namespace Core;

use PDO;
use PDOException;

class DataBase
{
    public static function getDataBase()
    {
        switch (env['DB_CONNECTION']) {
            case 'mysql':
                return self::mysql();
        }
    }

    private static function mysql()
    {
        try {
            $pdo = new PDO('mysql:host=' . env['DB_HOST'] . ';dbname=' . env['DB_DATABASE'], env['DB_USERNAME'], env['DB_PASSWORD']);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
            return $pdo;
        } catch (PDOException $e) {
            print($e->getMessage());
        }
    }
}
