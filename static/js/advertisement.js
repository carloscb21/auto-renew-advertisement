String.prototype.toNum = function(){
    return parseInt(this, 10);
}
$(document).ready(function(){
  $("#start").click(function(){ $.get("/start"); });
  $("#reset").click(function(){ $.get("/pause"); });
  $("#startAdvertisement").click(function(){
    var timming = $('#timming').val().toNum();

    if (Number.isInteger(timming)){
        $.get("/startAdvertisement?timming="+timming);
    } else {
        console.log("Error en timming");
    }
  });

});