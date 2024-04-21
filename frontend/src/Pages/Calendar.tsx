import React from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import LocationSelector from '../Components/LocationSelector';
import moment from 'moment';



const Calendar = () =>  {

    if (window.localStorage.getItem("selected_date") === null) {
        window.localStorage.setItem("selected_location", "");
    }

    const sunrise = window.localStorage.getItem('Sunrise');
    const sunset = window.localStorage.getItem('Sunset');
    const moonrise = window.localStorage.getItem('Moonrise');
    const moonset = window.localStorage.getItem('Moonset');
    const marsrise = window.localStorage.getItem('MarsRise');
    const marsset = window.localStorage.getItem('MarsSet');
    const mercuryrise = window.localStorage.getItem('MercuryRise');
    const mercuryset = window.localStorage.getItem('MercurySet');
    const venusrise = window.localStorage.getItem('VenusRise');
    const venusset = window.localStorage.getItem('VenusSet');
    const neptunerise = window.localStorage.getItem('NeptuneRise');
    const neptuneset = window.localStorage.getItem('NeptuneSet');
    const jupiterrise = window.localStorage.getItem('JupiterRise');
    const jupiterset = window.localStorage.getItem('JupiterSet');
    const saturnrise = window.localStorage.getItem('SaturnRise');
    const saturnset = window.localStorage.getItem('SaturnSet');

    const events = [
        {
            start: moment(sunrise).toDate(),
            end: moment(sunset).toDate(),
            title: "Sun"
        },
        {
            start: moment(marsrise).toDate(),
            end: moment(marsset).toDate(),
            title: "Mars"
        },
        {
            start: moment(moonrise).toDate(),
            end: moment(moonset).toDate(),
            title: "Moon"
        },
        {
            start: moment(mercuryrise).toDate(),
            end: moment(mercuryset).toDate(),
            title: "Mercury"
        },
        {
            start: moment(neptunerise).toDate(),
            end: moment(neptuneset).toDate(),
            title: "Neptune"
        },
        {
            start: moment(jupiterrise).toDate(),
            end: moment(jupiterset).toDate(),
            title: "Jupiter"
        },
        {
            start: moment(saturnrise).toDate(),
            end: moment(saturnset).toDate(),
            title: "Saturn"
        },
        {
            start: moment(venusrise).toDate(),
            end: moment(venusset).toDate(),
            title: "Venus"
        }
    ]

    return (
        <div className="content-wrapper">
            <div className="">
                <h1>Calendar</h1>
                <div className="mb-10">  
                    <LocationSelector />
                </div>
                    <CalendarInformation />
                <div className="h-[95vh] m-10 bg-gradient-to-r from-slate-300 to-slate-500 text-black">
                    <CalendarSelector views={{ month: true, week: false, day: true, agenda: false }} events={events} />
                </div>
            </div>
            <style>
                {`
                    .rbc-calendar {
                        border: 1px solid #fff;
                    }
                    .rbc-today {
                        background-color:lightblue;
                    }
                    .rbc-off-range-bg {
                        background-color: #616283;
                    }
                `}
            </style>
        </div>
    )
}

export default Calendar;