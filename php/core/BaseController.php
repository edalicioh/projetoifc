<?php

namespace Core;

abstract class BaseController
{
    protected $view;
    private $path;
    private $layoutPath;

    public function __construct()
    {
        $this->view = new \stdClass; //passa variaves e  conteudo para as views
    }

    protected function renderView($viewPath)
    {
        $this->path = __DIR__ . "/../app/Views/{$viewPath}.php";

        $this->sets();

        if ($this->layoutPath != null) {
            return $this->layout();
        } else {
            return $this->content();
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
        if (file_exists($this->path)) {
            require_once $this->path;
        } else {
            echo 'ERRO : 404';
        }
    }

    protected function layout()
    {
        if (file_exists(__DIR__ . "/../app/Views/{$this->layoutPath}.php")) {
            return require_once __DIR__ . "/../app/Views/{$this->layoutPath}.php";
        } else {
            echo 'Error: Layout path not found!';
        }
    }

    protected function component($path)
    {
        if (file_exists(__DIR__ . "/../app/Views/{$path}.php")) {
            return require_once __DIR__ . "/../app/Views/{$path}.php";
        } else {
            echo 'Error: component path not found!';
        }
    }

    private function sets():void
    {
        $arq = file($this->path);

        foreach ($arq as $key => $linha) {
            if (strstr($linha, '$js')) {
                $js = explode('"', $linha)[1];
                if ($js == null) {
                    $js = explode("'", $linha)[1];
                }
                $this->js($js);
            }
            if (strstr($linha, '$css')) {
                $css = explode('"', $linha)[1];
                if ($css == null) {
                    $css = explode("'", $linha)[1];
                }
                $this->css($css);
            }

            if (strstr($linha, '$title')) {
                $title = explode('"', $linha)[1];
                if ($title == null) {
                    $title = explode("'", $linha)[1];
                }
                $this->title($title);
            }

            if (strstr($linha, '$layout')) {
                $layoutPath = explode('"', $linha)[1];
                if ($layoutPath == null) {
                    $layoutPath = explode("'", $linha)[1];
                }
                $this->layoutPath = $layoutPath;
            }
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
