import React, {useEffect, useState} from 'react';
import CalendarInformation from '../Components/CalendarInformation';
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
            <div className="h-[500px]">
                <h1>Calendar</h1>
                <CalendarInformation data={data}/>
            </div>
        </div>
    )
}

export default Calendar;