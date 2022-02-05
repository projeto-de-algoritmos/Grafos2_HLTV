var select1 = document.getElementById('player1')
var select2 = document.getElementById('player2')

select1.addEventListener('change', 
    function show_photo() {
        e = document.getElementById('player1')
        div = document.getElementById("image1")
        div.innerHTML = ''
        player_foto = document.getElementById('img_' + e.options[e.selectedIndex].text)
        player_foto = player_foto.cloneNode(false)
        player_foto.style = "display: block;"
        div.appendChild(player_foto)
    }
)

select2.addEventListener('change', 
    function show_photo() {
        e = document.getElementById('player2')
        div = document.getElementById("image2")
        div.innerHTML = ''
        player_foto = document.getElementById('img_' + e.options[e.selectedIndex].text)
        player_foto = player_foto.cloneNode(false)
        player_foto.style = "display: block;"
        div.appendChild(player_foto)
    }
)

window.addEventListener('load', 
    function ordenar() {
        e = document.getElementById('player1')
        tmpAry = new Array();
        for(var i=0; i<e.options.length; i++){
            tmpAry[i] = new Array();
            tmpAry[i][0] = e.options[i].text;
            tmpAry[i][1] = e.options[i].value;
        }
        tmpAry.sort();
        while (e.options.length > 0) {
            e.options[0] = null;
        }
        for (var i=0;i<tmpAry.length;i++) {
            var op = new Option(tmpAry[i][0], tmpAry[i][1]);
            e.options[i] = op;
        }
        return;
    }
)

window.addEventListener('load', 
    function ordenar() {
        e = document.getElementById('player2')
        tmpAry = new Array();
        for(var i=0; i<e.options.length; i++){
            tmpAry[i] = new Array();
            tmpAry[i][0] = e.options[i].text;
            tmpAry[i][1] = e.options[i].value;
        }
        tmpAry.sort();
        while (e.options.length > 0) {
            e.options[0] = null;
        }
        for (var i=0;i<tmpAry.length;i++) {
            var op = new Option(tmpAry[i][0], tmpAry[i][1]);
            e.options[i] = op;
        }
        return;
    }
)