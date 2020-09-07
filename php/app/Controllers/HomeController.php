<?php
namespace App\Controllers;
use App\Models\Home;
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
        $data = $this->db->all() ;
        return  $this->renderView('home/home',  $data);
           
    }

    public function chart()
    {
        $data = $this->db->all() ;
        return $this->exitJson(  $data) ; 
    }
}