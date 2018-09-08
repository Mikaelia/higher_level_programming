$(function () {
  $.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      for (movie of data.results) {
        $('#list_movies').append(`<li>${movie.title}</li>`);
      }
    }
  });
});
