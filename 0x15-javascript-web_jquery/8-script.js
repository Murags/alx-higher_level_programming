$;
$.get(
  "https://swapi-api.alx-tools.com/api/films/?format=json",
  function (data, status) {
    for (const movie of data.results) {
      $("#list_movies").append(`<li>${movie.title}</li>`);
    }
  }
);
