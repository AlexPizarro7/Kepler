import React from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import LocationSelector from '../Components/LocationSelector';
import moment from 'moment';



const Calendar = () =>  {

    const sunrise = window.localStorage.getItem('Sunrise');
    const sunset = window.localStorage.getItem('Sunset');
    const culmination = window.localStorage.getItem('Culmination');

    console.log("Sunrise: " + sunrise);
    console.log("Sunset: " + sunset);

    const events = [
        {
            start: moment(sunrise).toDate(),
            end: moment(sunset).toDate(),
            title: "Sun"
        },
        {
            start: moment(culmination).toDate(),
            end: moment(culmination).toDate(),
            title: "Culmination"
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
                    <CalendarSelector events={events} />
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