import React, {useEffect, useState} from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import RequestAstronomy from '../AstronomyAPI';
import LocationSelector from '../Components/LocationSelector';



const Calendar = () =>  {
    const [data, setData] = useState({});
    
    useEffect(() => {
        RequestAstronomy("Tyler", "USA").then(data => setData(data))
        .catch(error => {
            console.error(error);
        });
    }, []);

    return (
        <div className="content-wrapper">
            <div className="">
                <h1>Calendar</h1>
                <div className="mb-10">  
                    <LocationSelector />
                </div>
                <CalendarInformation data={data}/>
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