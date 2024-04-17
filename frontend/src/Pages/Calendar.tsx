import React, {useEffect, useState} from 'react';
import CalendarInformation from '../Components/CalendarInformation';
import CalendarSelector from '../Components/CalendarSelector';
import RequestAstronomy from '../AstronomyAPI';



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
                <CalendarInformation data={data}/>
                <div className="h-[95vh] m-10 bg-white text-black">
                <CalendarSelector />
                </div>
            </div>
        </div>
    )
}

export default Calendar;