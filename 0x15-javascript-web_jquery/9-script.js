$.get("https://fourtonfish.com/hellosalut/?lang=fr", function (data, response) {
  $("#hello").html(`${data.hello}`);
});
