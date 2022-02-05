var select1 = document.getElementById('player1')
select1.addEventListener('change', 
    function show_photo() {
        e = document.getElementById('player1')
        div = document.getElementById("image1")
        div.innerHTML = ''
        player_foto = document.getElementById('img_' + e.options[e.selectedIndex].text)
        player_foto.style = "display: block;"
        div.appendChild(player_foto)
    }
)

var select2 = document.getElementById('player2')
select2.addEventListener('change', 
    function show_photo() {
        e = document.getElementById('player2')
        div = document.getElementById("image2")
        div.innerHTML = ''
        player_foto = document.getElementById('img_' + e.options[e.selectedIndex].text)
        player_foto.style = "display: block;"
        div.appendChild(player_foto)
    }
)