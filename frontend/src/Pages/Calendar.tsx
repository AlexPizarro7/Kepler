import React from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import LocationSelector from '../Components/LocationSelector';



const Calendar = () =>  {

    return (
        <div className="content-wrapper">
            <div className="">
                <h1>Calendar</h1>
                <div className="mb-10">  
                    <LocationSelector />
                </div>
                    <CalendarInformation />
                <div className="h-[95vh] m-10 bg-gradient-to-r from-slate-300 to-slate-500 text-black">
                    <CalendarSelector />
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