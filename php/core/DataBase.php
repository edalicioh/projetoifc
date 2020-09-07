<?php
namespace Core;
use PDO;
use PDOException;
class DataBase 
{
    public static function getDataBase()
    {
        try {              
            $pdo = new PDO("mysql:host=".DB_HOST . ";dbname=" . DB_DATABASE , DB_USERNAME, DB_PASSWORD);
            $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
            $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
            return $pdo;
        } catch (PDOException $e) {
            print($e->getMessage());
        } 

    }
   
}