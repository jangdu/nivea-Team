const onClickSendEmailBtn = () => {
  location.href = "/sendEmail";
};
function onClick() {
  $.ajax({
    data: {
      query: $('input[name="query"]').val(),
      page: page,
    },
    type: "GET",
    url: "/list",
  });
}
