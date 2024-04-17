export default function RequestAstronomy(city, country) {
    var url='http://localhost:8000/astronomy-data/'+city+'/'+country;

    return fetch(url)
      .then(response=>response.json())
      .then(
        (result) => {
          console.log(result); // This returns an object
          return result; // This returns undefined
        },
        (error) => {
          return error;
        }
      );
  }