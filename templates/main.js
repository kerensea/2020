$( document ).ready(function() {
$("#address-search").on( "click", function() {
  var encodedaddress = encodeURIComponent($("#address").val());
  $.getJSON( "https://www.googleapis.com/civicinfo/v2/voterinfo?address="+encodedaddress+"enter API here",
  function( json ) {
    var name  = json.pollingLocations[0].address.locationName;
    var street  = json.pollingLocations[0].address.line1;
    var city  = json.pollingLocations[0].address.city;
    var state  = json.pollingLocations[0].address.state;
    var zip  = json.pollingLocations[0].address.zip;
    var hours  = json.pollingLocations[0].pollingHours;
    $("#search-result").text(name + " " + street + " " +  city + " " + state + " " +  zip + " " +  hours);
 });
});
});
