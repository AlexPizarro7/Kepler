import React,  { useState } from "react";

const CalendarInformation = () => {

    return (

        <div className="ml-20 mr-20 bg-hero p-[20px] flex flex-col justify-center rounded">

            <h2>Today</h2>
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