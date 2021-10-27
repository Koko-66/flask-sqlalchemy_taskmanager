  $(document).ready(function(){
    // sidenav initialisation
    $('.sidenav').sidenav();
    // datepicker initialisation
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      i18in: {done: "Select"}
    });
    // select initialization
    $('select').formSelect();
  });
