fbStateKeys = [{key: 1, name: "Alabama", country_code: "US"},
{key: 2, name: "Alaska", country_code: "US"},
{key: 5, name: "Arkansas", country_code: "US"},
{key: 4, name: "Arizona", country_code: "US"},
{key: 8, name: "Colorado", country_code: "US"},
{key: 9, name: "Connecticut", country_code: "US"},
{key: 10, name: "Delaware", country_code: "US"},
{key: 12, name: "Florida", country_code: "US"},
{key: 13, name: "Georgia", country_code: "US"},
{key: 17, name: "Illinois", country_code: "US"},
{key: 23, name: "Maine", country_code: "US"},
{key: 27, name: "Minnesota", country_code: "US"},
{key: 15, name: "Hawaii", country_code: "US"},
{key: 29, name: "Missouri", country_code: "US"},
{key: 16, name: "Idaho", country_code: "US"},
{key: 21, name: "Kentucky", country_code: "US"},
{key: 22, name: "Louisiana", country_code: "US"},
{key: 38, name: "North Dakota", country_code: "US"},
{key: 18, name: "Indiana", country_code: "US"},
{key: 30, name: "Montana", country_code: "US"},
{key: 28, name: "Mississippi", country_code: "US"},
{key: 24, name: "Maryland", country_code: "US"},
{key: 37, name: "North Carolina", country_code: "US"},
{key: 33, name: "New Hampshire", country_code: "US"},
{key: 36, name: "New York", country_code: "US"},
{key: 35, name: "New Mexico", country_code: "US"},
{key: 25, name: "Massachusetts", country_code: "US"},
{key: 39, name: "Ohio", country_code: "US"},
{key: 40, name: "Oklahoma", country_code: "US"},
{key: 44, name: "Rhode Island", country_code: "US"},
{key: 42, name: "Pennsylvania", country_code: "US"},
{key: 41, name: "Oregon", country_code: "US"},
{key: 45, name: "South Carolina", country_code: "US"},
{key: 46, name: "South Dakota", country_code: "US"},
{key: 32, name: "Nevada", country_code: "US"},
{key: 20, name: "Kansas", country_code: "US"},
{key: 34, name: "New Jersey", country_code: "US"},
{key: 53, name: "Washington", country_code: "US"},
{key: 55, name: "Wisconsin", country_code: "US"},
{key: 51, name: "Virginia", country_code: "US"},
{key: 56, name: "Wyoming", country_code: "US"},
{key: 54, name: "West Virginia", country_code: "US"},
{key: 31, name: "Nebraska", country_code: "US"},
{key: 50, name: "Vermont", country_code: "US"},
{key: 48, name: "Texas", country_code: "US"},
{key: 47, name: "Tennessee", country_code: "US"},
{key: 49, name: "Utah", country_code: "US"},
{key: 19, name: "Iowa", country_code: "US"},
{key: 26, name: "Michigan", country_code: "US"},
{key: 6, name: "California", country_code: "US"}]

var account_number = "act_101592370392629"

var state_user_count = []


function fetchStatesReach(){
  $.get("https://franzsoftware.com/api/data")
    .done(function(data){
      console.log(data)
    })

}

function fetchDeliverEstimates(){
  var req_params = {
      "access_token" : "EAAFU8vfMnN0BADHVI1cODIDtJuoFLNmJEZAU7MPM3xXPWpZBZA4gcLAd3sEFLPromXixgN10zhybhNq4weRxm9lZBmkpT0ZApvSZCXbUHbTfG0z1h9x8WU971A09Du9viuMc1aETIvZCY4eOc0cZAtye0BSulLFHx0H5XDvUC35jOr1vIeGBzZAYFdO03jFlpNOIZChaOQr7HGJfmdTvwXlv3E",
      "optimize_for":"POST_ENGAGEMENT",
      "targeting_spec" : {
        "geo_locations" : {
          "regions":[{"key":47,"name":"Tennessee"}]
        }
      }
  }
  //console.log(req_params)
  $.get("https://franzsoftware.com/")
      .done(function(data){
        console.log(data)
      })

}

function extraStuff(obj){
  return function(data, textStatus, jqXHR){
    console.log(data)
    //state_user_count.push({"name":obj.targeting_spec.geo_locations.regions[0].name, "users":data.data.users})
  }
}




function tsvJSON(tsv){
  var lines = tsv.split("\n");

  var result = []

  var headers = lines[0].split("\t")

  for (var i = 1; i < lines.length; i++){
    var obj = {};
    var currentLine = lines[i].split("\t")

    for (var j = 0; j < headers.length; j++){
      obj[headers[j]] = currentLine[j];
    }

    result.push(obj)
  }

  return result
}
