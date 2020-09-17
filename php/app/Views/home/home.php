<?php
    $js = 'home/assets/js/index.js';
    $css = 'home/assets/css/styles.css';
    $title = 'Home';
    $layout = 'layout/index';
?>


<div class="content-wrapper">
    <section class="content pt-3">
        <div class="d-sm-flex align-items-center justify-content-between mx-2">
            <h1 class="h3 mb-0 text-gray-800">Boletim N. XXX <span id="idCampus">- Reitoria</span></h1>
            <h1 class="h5 mb-0 text-gray-800">Data xx/xx/2020</h1>
        </div>
    </section>

    <section class="content   pt-3">
        <div class="col-md-12">
            <div class="card">
                <ul class="nav nav-tabs">
                    <li class="nav-item">
                        <a class="nav-link active" href="#activity" data-toggle="tab">Activity</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#timeline" data-toggle="tab">Timeline</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#settings" data-toggle="tab">Settings</a>
                    </li>
                </ul>
                <div class="card-body">
                    <div class="tab-content">
                        <div class="tab-pane active" id="activity">
                            <?php $this->component('home/components/_box') ?>
                            <div id="curve_chart"></div>  
                        </div>
                    </div>
                </div>
    </section>
</div>

<script>
    datas = <?php $this->json($this->data) ?>
</script>