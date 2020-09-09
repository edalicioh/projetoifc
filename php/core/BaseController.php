<?php

namespace Core;

abstract class BaseController
{
    protected $view;

    private $viewPath;

    public function __construct()
    {
        $this->view = new \stdClass; //passa variaves e  conteudo para as views
    }
    protected function renderView($viewPath, $layoutPath = null, $title = false)
    {
        $this->viewPath = $viewPath;
        $this->layoutPath = $layoutPath;

        if ($layoutPath) {
            return $this->layout();
        } else {
            return $this->content();
        }

        if($title){
            $this->title($title);
            
        }
    }


    public function __get($name)
    {
        return $this->$name;
    }

    public function __set($name, $value)
    {
        $this->$name = $value;
    }

    protected function content()
    {
        if (file_exists(__DIR__ . "/../app/Views/{$this->viewPath}.php")) {
            require_once __DIR__ . "/../app/Views/{$this->viewPath}.php";
        } else {
            echo "ERRO : 404";
        }
    }

    protected function layout()
    {
        if (file_exists(__DIR__ . "/../app/Views/{$this->layoutPath}.php")) {
            return require_once __DIR__ . "/../app/Views/{$this->layoutPath}.php";
        } else {
            echo "Error: Layout path not found!";
        }
    }


    /**
     * Funsao para retornar json
     *
     * @param [type] $data
     * @return void
     */
    protected function json($data)
    {
        if (!empty($data)) {
            print(json_encode($data));
        } else {
            print(json_encode(['error' => 'Dado não encontrado']));
        }
    }
    /**
     * Fusão para a inserção de javascript
     *
     * @param [type] $js
     * @return void
     */
    protected function js($js)
    {
        $this->view->js[] = $js;
    }


    /**
     * Fusão para a inserção de css
     *
     * @param [type] $css
     * @return void
     */
    protected function css($css)
    {
        $this->view->css[] = $css;
    }

    protected function title($title)
    {
        $this->view->title = $title;
    }
}
