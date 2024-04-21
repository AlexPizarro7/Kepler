import React from "react";
import Planetslider from "./PlanetSlider";

function convert24to12(time) {
    var hour = parseInt(time.substring(0,2));
    var minute = time.substring(3,5);
    if (hour > 12) {
        return (hour - 12) + ":" + minute + " PM";
    }else{
        return hour + ":" + minute + " AM";
    }
}

const CalendarInformation = () => {

    if (window.localStorage.getItem("selected_date") === null) {
        const current_date = new Date();
        const year = current_date.getUTCFullYear();
        const month = current_date.getUTCMonth()+1;
        if (month < 10) {
            var monthStr = "0" + month;
        }else{
            monthStr = month.toString();
        }
        const day = current_date.getUTCDate();
        window.localStorage.setItem("selected_date", monthStr  +"-"+ day +"-"+ year);
    }

    var sunrise = window.localStorage.getItem("selected_date")+"00:00:00";
    var sunset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var marsrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var marsset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var moonrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var moonset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var mercuryrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var mercuryset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var venusrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var venusset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var neptunerise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var neptuneset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var jupiterrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var jupiterset =  window.localStorage.getItem("selected_date")+"00:00:00";
    var saturnrise =  window.localStorage.getItem("selected_date")+"00:00:00";
    var saturnset =  window.localStorage.getItem("selected_date")+"00:00:00";

    if (window.localStorage.getItem("Sunrise") != null){
        sunrise = window.localStorage.getItem("Sunrise").substring(11,window.localStorage.getItem('Sunrise').length-3);
    }
    if (window.localStorage.getItem("Sunset") != null){
        sunset = window.localStorage.getItem("Sunset").substring(11,window.localStorage.getItem('Sunset').length-3);
    }
    if (window.localStorage.getItem("MarsRise") != null){
        marsrise = window.localStorage.getItem("MarsRise").substring(11,window.localStorage.getItem('MarsRise').length-3);
    }
    if (window.localStorage.getItem("MarsSet") != null){
        marsset = window.localStorage.getItem("MarsSet").substring(11,window.localStorage.getItem('MarsSet').length-3);
    }
    if (window.localStorage.getItem("Moonrise") != null){
        moonrise = window.localStorage.getItem("Moonrise").substring(11,window.localStorage.getItem('Moonrise').length-3);
    }
    if (window.localStorage.getItem("Moonset") != null){
        moonset = window.localStorage.getItem("Moonset").substring(11,window.localStorage.getItem('Moonset').length-3);
    }
    if (window.localStorage.getItem("MercuryRise") != null){
        mercuryrise = window.localStorage.getItem("MercuryRise").substring(11,window.localStorage.getItem('MercuryRise').length-3);
    }
    if (window.localStorage.getItem("MercurySet") != null){
        mercuryset = window.localStorage.getItem("MercurySet").substring(11,window.localStorage.getItem('MercurySet').length-3);
    }
    if (window.localStorage.getItem("VenusRise") != null){
        venusrise = window.localStorage.getItem("VenusRise").substring(11,window.localStorage.getItem('VenusRise').length-3);
    }
    if (window.localStorage.getItem("VenusSet") != null){
        venusset = window.localStorage.getItem("VenusSet").substring(11,window.localStorage.getItem('VenusSet').length-3);
    }
    if (window.localStorage.getItem("NeptuneRise") != null){
        neptunerise = window.localStorage.getItem("NeptuneRise").substring(11,window.localStorage.getItem('NeptuneRise').length-3);
    }
    if (window.localStorage.getItem("NeptuneSet") != null){
        neptuneset = window.localStorage.getItem("NeptuneSet").substring(11,window.localStorage.getItem('NeptuneSet').length-3);
    }
    if (window.localStorage.getItem("JupiterRise") != null){
        jupiterrise = window.localStorage.getItem("JupiterRise").substring(11,window.localStorage.getItem('JupiterRise').length-3);
    }
    if (window.localStorage.getItem("JupiterSet") != null){
        jupiterset = window.localStorage.getItem("JupiterSet").substring(11,window.localStorage.getItem('JupiterSet').length-3);
    }
    if (window.localStorage.getItem("SaturnRise") != null){
        saturnrise = window.localStorage.getItem("SaturnRise").substring(11,window.localStorage.getItem('SaturnRise').length-3);
    }
    if (window.localStorage.getItem("SaturnSet") != null){
        saturnset = window.localStorage.getItem("SaturnSet").substring(11,window.localStorage.getItem('SaturnSet').length-3);
    }


    return (

        <div className="ml-20 mr-20 bg-hero p-[20px] flex flex-col justify-center rounded">

            <h2>Today</h2>
            <h3>Mars: </h3>
            <Planetslider planet={"red"} start={marsrise} end={marsset}/>
            <h3>Sun: </h3>
            <Planetslider planet={"yellow"} start={sunrise} end={sunset}/>
            <h3>Moon: </h3>
            <Planetslider planet={"white"} start={moonrise} end={moonset}/>
            <h3>Mercury: </h3>
            <Planetslider planet={"grey"} start={mercuryrise} end={mercuryset}/>
            <h3>Venus: </h3>
            <Planetslider planet={"organe"} start={venusrise} end={venusset}/>
            <h3>Neptune: </h3>
            <Planetslider planet={"blue"} start={neptunerise} end={neptuneset}/>
            <h3>Jupiter: </h3>
            <Planetslider planet={"brown"} start={jupiterrise} end={jupiterset}/>
            <h3>Saturn: </h3>
            <Planetslider planet={"tan"} start={saturnrise} end={saturnset}/>
            <p>Location Information:</p>
            <p>Latitude: {window.localStorage.getItem("Latitude")}</p>
            <p>Longitude: {window.localStorage.getItem("Longitude")}</p>
            <p>Sunrise: {window.localStorage.getItem("Sunrise")}</p>
            <p>Sunset: {window.localStorage.getItem("Sunset")}</p>
            <p>Culmination: {window.localStorage.getItem("Culmination")}</p>
            <p>Twilight End: {window.localStorage.getItem("TwilightEnd")}</p>
        </div>
    );

}

export default CalendarInformation;