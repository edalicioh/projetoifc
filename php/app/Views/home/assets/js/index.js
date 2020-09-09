(function(){
    const idCampus = document.getElementById('idCampus')
    const sidebarLink = document.querySelectorAll(".sidebar-link")
    
    
    sidebarLink.forEach( link => {
        link.addEventListener('click', (e) => {
            e.preventDefault()
            const cidade = e.target.innerText
            idCampus.innerHTML = cidade;
            datas.forEach(data => {
                if (data.cidade == cidade){
                    console.log(data);

                    document.getElementById('obitos').innerHTML = data.obitos
                    document.getElementById('positivos').innerHTML = data.positivos
                    document.getElementById('incidencia').innerHTML = data.incidencia + "<small> %</small>"

                }
            })
        })
    })

   
} )()