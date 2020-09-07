(function(){


    saida = []
    dados.forEach(element => {
        saida.push( [
            element.cidade,
            element.incidencia,
            element.obitos,
            element.positivos,
        ])
    });



    google.charts.load('current', {'packages':['table']});
      google.charts.setOnLoadCallback(drawTable);
      function drawTable() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'cidade');
        data.addColumn('string', 'incidencia');
        data.addColumn('string', 'obitos');
        data.addColumn('string', 'positivos');

        data.addRows(saida);
    
        
        

        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
      }
})()