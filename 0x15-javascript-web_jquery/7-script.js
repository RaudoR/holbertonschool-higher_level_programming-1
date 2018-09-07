$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', (data, status) => {
    if (status === 'success') {
      $('div#character').text(data.name);
    }
  });
});
