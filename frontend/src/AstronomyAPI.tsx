export default function RequestAstronomy(country, city, state, zip, date) {

  if (state === "") {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+date;
  }else if (zip === "") {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+date;
  }else {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+zip+'/'+date;
  }


    return fetch(url)
      .then(response=>response.json())
      .then(
        (result) => {
          window.localStorage.setItem("Latitude", result.Latitude);
          window.localStorage.setItem("Longitude", result.Longitude);
          window.localStorage.setItem("Sunrise", result.Sunrise);
          window.localStorage.setItem("Sunset", result.Sunset);
          window.localStorage.setItem("Culmination", result.Culmination);
          window.localStorage.setItem("TwilightEnd", result.TwilightEnd);
          window.dispatchEvent(new Event('storage'))
          console.log(result); // This returns an object
          return result; // This returns undefined
        },
        (error) => {
          return error;
        }
      );
  }