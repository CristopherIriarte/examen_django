$("#btnCargar").click(function (event) {
    event.preventDefault();

    var nombre_pokemon= $("#txtNombrePokemon").val();
    var url = "https://pokeapi.co/api/v2/pokemon/"+nombre_pokemon;

  //   fetch(url)
  //     .then((response) => {
  //       return response.json();
  //     })
  //     .then((data) => {
  //       console.log(data);
  //     })
  //     .catch((error) => {
  //       console.error(error);
  //     });

    fetch(url)
        .then(response => response.json())
        .then(data => 
            {
                var $nombre_pokemon = $('<h1>').text(data.forms[0].name);
                var $foto_pokemon = $("<p><img src='"+data.sprites.other["official-artwork"].front_default+"'>");

                  // para limpiar el contedor antes de desplegar
                $("#info").empty();
                $('#info')
                    .append($nombre_pokemon)
                    .append($foto_pokemon)

            })
        .catch(error => console.error(error));

});