import React from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import LocationSelector from '../Components/LocationSelector';
import moment from 'moment';
import { JsonReturnEvents } from '../utils/jsonParser';



const Calendar = () => {

    if (window.localStorage.getItem("selected_date") === null) {
        window.localStorage.setItem("selected_location", "");
        window.localStorage.setItem("selected_date", moment().format("MM-DD-YYYY"));
    }

    var it_date = window.localStorage.getItem("selected_date");

    const month = parseInt(it_date.substring(0, 2));
    const year = parseInt(it_date.substring(6, 10));
    var day = 1;
    var maxDay = new Date(year, month, 0).getDate();

    var events = [];

    for (var i = 0; i < maxDay; i++) {
        it_date = month + "-" + day + "-" + year;
        day = day + 1;
        events = JsonReturnEvents(events, it_date);
    }

    const passed_date = window.localStorage.getItem("selected_date");

    return (
        <div className="content-wrapper">
            <div className="">
                <h1>Calendar</h1>
                <div className="mb-10">
                    <LocationSelector />
                </div>
                <CalendarInformation date={ passed_date } />
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