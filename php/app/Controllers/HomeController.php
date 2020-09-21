<?php

namespace App\Controllers;

use Core\BaseController;
use Core\Container;

class HomeController extends BaseController
{
    private $db;
    private $mediaMovel;

    public function __construct()
    {
        parent::__construct();
        $this->db = Container::getModel('Home');
        $this->mediaMovel = Container::getModel('MediaMovel');
    }

    public function index()
    {
        $this->data = $this->db->findAll() ;
        return  $this->renderView('home/home');
    }

    public function chart($codeIbge)
    {
        $mediaObitos = $this->mediaMovel->findByParam("where codigo_ibge_municipio  = {$codeIbge}");
        return $this->json($mediaObitos);
    }
}
