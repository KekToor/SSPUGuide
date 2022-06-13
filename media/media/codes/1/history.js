$(function(){
    function udalostiBlock(udalosti){
        udalosti.forEach((udalost) =>{
            $('#hist tbody').append(`<tr>
            <td class="udalost-rok font-weight-bold pt-3">${udalost.rok}</td>
            <td>
            <p class="udalost-jmeno">
                <a href="${udalost.url}" target="_new" class="text-decoration-none udalost-link pl-1">${udalost.udalost}</a>
                <a class="fa fa-chevron-down float-right text-decoration-none udalost-link" aria-hidden="true" href="#"></a>
            </p>
            <p class="udalost-detail">
              ${udalost.detaily}
              </p>
            </td>
          </tr>`);
        });

        $('h2 .fa-chevron-down').hide();
        $('h2').on('click', function(){
            $(this).nextAll().slideToggle(1500);
            $(this).children('.fa').toggleClass('fa-chevron-down fa-chevron-up');
        });

        $('.udalost-detail').hide();
        $('#hist .fa-chevron-up').hide();
        $('#hist .udalost-link').on('click',function(){
            $(this).parent().next().slideToggle(1000);
            $(this).toggleClass('fa-chevron-down fa-chevron-up');
        });
    }
    

    

     

     function hrdinoveBlock(hrdinove){
        hrdinove.forEach((hrdina) =>{
            $('#hrdinove').append(`
                <div class="col-lg-6">
                    <figure class = "text-center">
                        <img src = "img/${hrdina.portrait}" class = "m-auto udalost-link" style = "height:250px">
                        <figcaption>
                            <div>
                            <h3 class = "font-weight-bold">${hrdina.name}</h3>
                            <div class = "hero-popis">
                                <h5 class = font-weight-bold>* ${hrdina.birth} &nbsp; &#10015; ${hrdina.death}</h5>
                                <p class = "px-5 text-justify">
                                    ${hrdina.bio}
                                </p>
                                <p class = "px-3">
                                    <b>Zdroj:</b> <a href = "${hrdina.wiki}">Wikipedie</a>
                                </p>
                            </div>    
                            </div>
                        </figcaption>
                    </figure>
                </div>
            `);
        });
        $('.hero-popis').hide();
        $('#hrdinove img').on('click',function(){
            $(this).siblings('figcaption').find('.hero-popis').slideToggle(1000);
         });
     };   
     
     fetch('../historie/data/udalosti.json')
     .then(response => {
        return response.json();
     })
     .then(json =>{
         udalostiBlock(json);
     })
     .catch(function(error){
        console.error('Chyba: \n', error);
     });
     
     fetch('../historie/data/hrdinove.json')
     .then(response => {
        return response.json();
     })
     .then(json =>{
         hrdinoveBlock(json);
     })
     .catch(function(error){
        console.error('Chyba: \n', error);
     });


        
});



