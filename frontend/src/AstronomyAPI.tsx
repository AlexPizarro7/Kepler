export default function RequestAstronomy(country, city, state, zip, date) {

  if (state === "") {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+date;
  }else if (zip === "") {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+date;
  }else {
    var url='http://localhost:8000/location-selector/'+country+'/'+city+'/'+state+'/'+zip+'/'+date;
  }

  // @TODO: Fetch an entire month and create a function to stringify an item into localstorage and another helper function to parse it so we can consolidate local storage.


    return fetch(url)
      .then(response=>response.json())
      .then(
        (result) => {
          window.localStorage.setItem("Latitude", result.Latitude);
          window.localStorage.setItem("Longitude", result.Longitude);
          window.localStorage.setItem("Sunrise", result.Sunrise.substring(0, result.Sunrise.length - 1));
          window.localStorage.setItem("Sunset", result.Sunset.substring(0, result.Sunset.length - 1));
          window.localStorage.setItem("SunCulmination", result.SunCulmination.substring(0, result.SunCulmination.length - 1));
          window.localStorage.setItem("TwilightEnd", result.SunTwilightEnd.substring(0, result.SunTwilightEnd.length - 1));
          window.localStorage.setItem("Moonrise", result.Moonrise.substring(0, result.Moonrise.length - 1));
          window.localStorage.setItem("Moonset", result.Moonset.substring(0, result.Moonset.length - 1));
          window.localStorage.setItem("MoonCulmination", result.MoonCulmination.substring(0, result.MoonCulmination.length - 1));
          window.localStorage.setItem("MercuryRise", result.MercuryRise.substring(0, result.MercuryRise.length - 1));
          window.localStorage.setItem("MercurySet", result.MercurySet.substring(0, result.MercurySet.length - 1));
          window.localStorage.setItem("MercuryCulmination", result.MercuryCulmination.substring(0, result.MercuryCulmination.length - 1));
          window.localStorage.setItem("VenusRise", result.VenusRise.substring(0, result.VenusRise.length - 1));
          window.localStorage.setItem("VenusSet", result.VenusSet.substring(0, result.VenusSet.length - 1));
          window.localStorage.setItem("VenusCulmination", result.VenusCulmination.substring(0, result.VenusCulmination.length - 1));
          window.localStorage.setItem("MarsRise", result.MarsRise.substring(0, result.MarsRise.length - 1));
          window.localStorage.setItem("MarsSet", result.MarsSet.substring(0, result.MarsSet.length - 1));
          window.localStorage.setItem("MarsCulmination", result.MarsCulmination.substring(0, result.MarsCulmination.length - 1));
          window.localStorage.setItem("JupiterRise", result.JupiterRise.substring(0, result.JupiterRise.length - 1));
          window.localStorage.setItem("JupiterSet", result.JupiterSet.substring(0, result.JupiterSet.length - 1));
          window.localStorage.setItem("JupiterCulmination", result.JupiterCulmination.substring(0, result.JupiterCulmination.length - 1));
          window.localStorage.setItem("SaturnRise", result.SaturnRise.substring(0, result.SaturnRise.length - 1));
          window.localStorage.setItem("SaturnSet", result.SaturnSet.substring(0, result.SaturnSet.length - 1));
          window.localStorage.setItem("SaturnCulmination", result.SaturnCulmination.substring(0, result.SaturnCulmination.length - 1));
          window.localStorage.setItem("NeptuneRise", result.NeptuneRise.substring(0, result.NeptuneRise.length - 1));
          window.localStorage.setItem("NeptuneSet", result.NeptuneSet.substring(0, result.NeptuneSet.length - 1));
          window.dispatchEvent(new Event('storage'))
          console.log(result); // This returns an object
          return result; // This returns undefined
        },
        (error) => {
          return error;
        }
      );
  }