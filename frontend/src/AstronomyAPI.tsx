import JsonParser from "./utils/jsonParser";

export default async function RequestAstronomy(country:string, city:string, state:string, zip:string, date:string) {

  const month = parseInt(date.substring(0,2));
  const year = parseInt(date.substring(6,10));
  var day = 1;
  var maxDay = new Date(year,month,0).getDate();

  if (window.localStorage.getItem("newLocation") === "true"){
    window.sessionStorage.clear();
  }

  for (var i = 0; i < maxDay; i++) {

    var inc_date = month + "-" + day + "-" + year;    

    day = day+ 1;

    if (state === "") {
      var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+inc_date;
    }else if (zip === "") {
      var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+inc_date;
    }else {
      var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+zip+'/'+inc_date;
    }
  
    if (window.sessionStorage.getItem(inc_date) === null){
      await fetch(url)
        .then(response=>response.json())
        .then(
          (result) => {
            JsonParser(result, inc_date);
            console.log(result); // This returns an object // This returns undefined
          },
          (error) => {
            return error;
          }
        );
      }

  }

  await window.location.reload();
  await window.localStorage.setItem("newLocation", "false");

}