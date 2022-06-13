$(document).ready(function () {
    let mesta = [];
    let cityColor = $('#gruppe').attr('fill');
    let lastfill = $("svg").attr('fill');
    console.log(cityColor);

    fetch('../geografie/data/cities.json')
     .then(response => {
        return response.json();
     })
     .then(json =>{
        mesta = json;
     })
     .catch(function(error){
        console.error('Chyba: \n', error);
     });
    

    $('#mapa ellipse, #mapa rect').on('click', function () {
        let id = $(this).attr('id');
        console.log(id)
        $('#mapa ellipse, #mapa rect').css({ 'fill': cityColor });
        $(this).css('fill', 'teal');
        let mesto = mesta.find(item => {return item.id == id});
        console.log(mesto);
        $('#infoBox').html(`
        <div class = "row">
            <div class = "col-12">
                <h2 class = "text-center py-1">${mesto.name}</h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col-8 pt-2">
                <p style = "font-size:1.5em;" class = "pl-4">Populace: <strong>${mesto.pop}</strong></p>
                <p class = "text-justify">${mesto.popis}</p>
            </div>
            <div class = "col-4">
                <figure class = "text-center">
                    <img src = "img/${mesto.znak}" class = "m-auto" style = "height:250px">
                    <figcaption class = "pt-1"><strong>Městský Znak</strong></figcaption>
                </figure>
            </div>
        </div>
        <div class = "row">
            <figure class = "text-center col-12">
                <img src = "img/${mesto.obrazky}" class = "m-auto" style = "width:900px">
                <figcaption class = "pt-1" style = "font-size:1.2em;"><b><i>${mesto.desc}</i></b></figure>
            </figure>
        </div>

        `)
    })

    $("path").on('click', function () { //on click on path
        if (lastfill == 'rgb(255, 255, 0)') { //if lastfill is yellow
            $(this).css({ 'fill': 'black' }); //set the color to black
            lastfill = "#7c7c7c"; //set lastfill to grey
        } else {
            $("path").css('fill', $("svg").attr('fill')); //revert all to grey
            $(this).css({ 'fill': 'yellow' }); //set current to yellow
            lastfill = "rgb(255, 255, 0)"; //set last fill to yellow
        }
    });
    $("path").on('mouseover', function () { //on mouse over on path
        lastfill = $(this).css('fill');
        if (lastfill == 'rgb(255, 255, 0)') { //if lastfill is yellow
            $(this).css({ 'fill': 'goldenrod' }); //set path to blackish yellow
        } else {
            $(this).css({ 'fill': 'black' }); //set path to black
        }
    });
    $("path").on('mouseout', function () { //on mouse out on path set previous color
        $(this).css({ 'fill': lastfill });
    });

    $('#mestaS').on('click', function(){
        $('#mapa ellipse, #mapa rect').toggle(350);
    });
})