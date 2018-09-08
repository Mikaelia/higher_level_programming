$.get("https://swapi.co/api/films/?format=json", function(data, textStatus) {
    for (movie of data.results) {
        $("UL#list_movies").append(`<li>${movie.title}</li>`)
    }
});