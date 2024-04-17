// @ts-ignore
const CalendarInformation = ({data}) => {

    return (
        <div className="ml-20 mr-20 bg-hero p-[20px] flex flex-col justify-center rounded">
            <h2>Today</h2>
            <p>Sunrise: {data.sunrise}</p>
            <p>Sunset: {data.sunset}</p>
            <p>Culmination: {data.culmination}</p>
            <p>Twilight End: {data.twilight_end}</p>
        </div>
    );

}

export default CalendarInformation;