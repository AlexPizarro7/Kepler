import React from "react";

const CalendarInformation = ({data}) => {

    return (
        <>
            <h2>Today:</h2>
            <p>Sunrise: {data.sunrise}</p>
            <p>Sunset: {data.sunset}</p>
            <p>Culmination: {data.culmination}</p>
            <p>Twilight End: {data.twilight_end}</p>
        </>
    );

}

export default CalendarInformation;