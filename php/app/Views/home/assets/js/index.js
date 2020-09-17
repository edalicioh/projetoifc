(function () {
  const idCampus = document.getElementById("idCampus");
  const sidebarLink = document.querySelectorAll(".sidebar-link");

  sidebarLink.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const cidade = e.target.innerText;
      idCampus.innerHTML = cidade;
      datas.forEach((data) => {
        if (data.cidade == cidade) {
          console.log(data);
          document.getElementById("populacao").innerHTML = data.populacao;
          document.getElementById("obitos").innerHTML = data.obitos;
          document.getElementById("positivos").innerHTML = data.positivos;
          document.getElementById("incidencia").innerHTML =
            data.incidencia + "<small> %</small>";

          fetch("/chart/" + data.codigo_ibge_municipio)
            .then((response) => response.json())
            .then((json) => {
              chart(json )
            });
        }
      });
    });
  });

  const chart = (dados) => {
    google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

    console.log(dados);
     let saida = [['Year', 'Sales']]

      dados.map(element => {
        saida.push([
          moment(element.data_obito ).format("MM/DD/YYYY"),
          +(element.media),
        ]);
      })
      console.log(saida);
      function drawChart() {
        var data = new google.visualization.arrayToDataTable(saida);

        var options = {
          title: 'Company Performance',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }
  };
})();
