var form = document.querySelector('.pageclip-form')
Pageclip.form(form, {
  onSubmit: function (event) { },
  onResponse: function (error, response) { },
  successTemplate: '<span>Thank you!</span>'
})