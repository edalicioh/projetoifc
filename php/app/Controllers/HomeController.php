<?php
namespace App\Controllers;
use Core\BaseController;
use Core\Container;

class HomeController extends BaseController
{
    private $db;

    public function __construct()
    {
        parent::__construct();
        $this->db = Container::getModel('Home');
    }

    public function index()
    {
        $this->data = $this->db->all() ;        
        return  $this->renderView('home/home', 'layout/index' , "Home");
           
    }

    public function chart()
    {
        $data = $this->db->all() ;
        return $this->json( $data) ; 
    }
}