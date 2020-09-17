<aside class="main-sidebar sidebar-dark-primary elevation-4" style="background: #1cc88a;">
    <div class="pb-2">
        <img class="w-100" src="https://cecom.ifc.edu.br/wp-content/uploads/sites/17/2015/10/Logo_IFC_horizontal.png" class="brand-image" >
    </div>



    <div class="sidebar  ">

        <nav class="mt-2 mb-5 bg-white rounded-lg">
            <ul class="nav nav-pills nav-sidebar flex-column " data-widget="treeview" role="menu" data-accordion="false">

                <?php foreach ($this->data as $key => $value) :  ?>
                <li class="nav-item text-center p-2">
                    <a href="#" class="nav-link sidebar-link " data-id="<?= $value->codigo_ibge_municipio ?>">
                        <p class="text text-dark" ><?= $value->cidade ?></p>
                    </a>
                </li>
                <?php endforeach ?>

            </ul>
        </nav>
    </div>

</aside>