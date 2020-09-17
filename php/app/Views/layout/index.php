<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <title><?= $this->view->title ?></title>
    <!-- Tell the browser to be responsive to screen width -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="public/assets/css/all.min.css">
    <!-- Ionicons -->
    <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
    <!-- overlayScrollbars -->
    <link rel="stylesheet" href="https://adminlte.io/themes/dev/AdminLTE/plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="https://adminlte.io/themes/dev/AdminLTE/dist/css/adminlte.min.css">
    <!-- Google Font: Source Sans Pro -->
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700" rel="stylesheet">
    <!-- styles globais -->
    <link rel="stylesheet" href="public/assets/css/styles.css">
    


    <?php foreach ($this->view->css as $css) : ?>
        <link rel="stylesheet" href="/app/Views/<?= $css ?>">
    <?php endforeach ?>
</head>

<body class="hold-transition sidebar-mini layout-fixed">
    <div class="wrapper">



        <?php include_once __DIR__ . "/components/_navbar.php" ?>

        <?php include_once __DIR__ . "/components/_sidebar.php" ?>


        <?php $this->content() ?>


        <?php include_once __DIR__ . "/components/_footer.php" ?>
    </div>
    <!-- ./wrapper -->
    <!-- jQuery -->
    <script src="https://adminlte.io/themes/dev/AdminLTE/plugins/jquery/jquery.min.js"></script>
    <!-- Bootstrap 4 -->
    <script src="https://adminlte.io/themes/dev/AdminLTE/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
    <!-- overlayScrollbars -->
    <script src="https://adminlte.io/themes/dev/AdminLTE/plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
    <!-- AdminLTE App -->
    <script src="https://adminlte.io/themes/dev/AdminLTE/dist/js/adminlte.min.js"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.27.0/moment.min.js"></script>
    
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <?php foreach ($this->view->js as $js) : ?>
        <script type="module" src="/app/Views/<?= $js ?>"></script>
    <?php endforeach ?>

</body>

</html>
