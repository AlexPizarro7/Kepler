import React from "react";
import Planetslider from "./PlanetSlider";
import { JsonParserRetriever } from "../utils/jsonParser";

const CalendarInformation = ({ date }) => {

    var selected_date = "";

    if (date == null) {
        const current_date = new Date();
        const year = current_date.getFullYear();
        const month = current_date.getMonth();
        if (month < 10) {
            var monthStr = "0" + month;
        } else {
            monthStr = month.toString();
        }
        const day = current_date.getDate();
        selected_date = monthStr + "-" + day + "-" + year;
    } else {
        selected_date = date.substring(1, date.length);
    }

    const selected_location = window.localStorage.getItem("selected_location");

    console.log("selected_date: " + selected_date);
    console.log("local selected_date object: " + window.localStorage.getItem(selected_date));

    if (window.sessionStorage.getItem(selected_date) == null) {
        var sunrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var sunset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var marsrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var marsset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var moonrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var moonset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var mercuryrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var mercuryset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var venusrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var venusset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var neptunerise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var neptuneset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var jupiterrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var jupiterset = window.localStorage.getItem("selected_date") + "T00:00:00";
        var saturnrise = window.localStorage.getItem("selected_date") + "T00:00:00";
        var saturnset = window.localStorage.getItem("selected_date") + "T00:00:00";
    } else {
        const resultObject = JsonParserRetriever(selected_date);
        sunrise = resultObject.Sunrise.substring(11,resultObject.Sunrise.length-3);
        console.log(sunrise);
        sunset = resultObject.Sunset.substring(11,resultObject.Sunset.length-3);
        marsrise = resultObject.MarsRise.substring(11,resultObject.MarsRise.length-3);
        marsset = resultObject.MarsSet.substring(11,resultObject.MarsSet.length-3);
        mercuryrise = resultObject.MercuryRise.substring(11,resultObject.MercuryRise.length-3);
        mercuryset = resultObject.MercurySet.substring(11,resultObject.MercurySet.length-3);
        venusrise = resultObject.VenusRise.substring(11,resultObject.VenusRise.length-3);
        venusset = resultObject.VenusSet.substring(11,resultObject.VenusSet.length-3);
        neptunerise = resultObject.NeptuneRise.substring(11,resultObject.NeptuneRise.length-3);
        neptuneset = resultObject.NeptuneSet.substring(11,resultObject.NeptuneSet.length-3);
        jupiterrise = resultObject.JupiterRise.substring(11,resultObject.JupiterRise.length-3);
        jupiterset = resultObject.JupiterSet.substring(11,resultObject.JupiterSet.length-3);
        saturnrise = resultObject.SaturnRise.substring(11,resultObject.SaturnRise.length-3);
        saturnset = resultObject.SaturnSet.substring(11,resultObject.SaturnSet.length-3);
    }

    console.log(sunrise);

    return (

        <div className="ml-20 mr-20 bg-hero p-[20px] flex flex-col justify-center rounded">

            <h2>{selected_date} {selected_location}</h2>
            <h3>Mars: </h3>
            <Planetslider planet={"red"} start={marsrise} end={marsset} />
            <h3>Sun: </h3>
            <Planetslider planet={"yellow"} start={sunrise} end={sunset} />
            <h3>Mercury: </h3>
            <Planetslider planet={"grey"} start={mercuryrise} end={mercuryset} />
            <h3>Venus: </h3>
            <Planetslider planet={"organe"} start={venusrise} end={venusset} />
            <h3>Neptune: </h3>
            <Planetslider planet={"blue"} start={neptunerise} end={neptuneset} />
            <h3>Jupiter: </h3>
            <Planetslider planet={"brown"} start={jupiterrise} end={jupiterset} />
            <h3>Saturn: </h3>
            <Planetslider planet={"tan"} start={saturnrise} end={saturnset} />
        </div>
    );

}

export default CalendarInformation;