import React from 'react';
import './planetslider.css';

function convert24to12(time) {
    var hour = parseInt(time.substring(0,2));
    var minute = time.substring(3,5);
    if (hour > 12) {
        return (hour - 12) + ":" + minute + " PM";
    }else{
        return hour + ":" + minute + " AM";
    }
}

function calculateTimeScale(start, end) {
    var startHour = parseInt(start.substring(0,2));
    var endHour = parseInt(end.substring(0,2));
    var betweenHour = endHour - startHour;
    var startPercent = Math.round(startHour / 24 * 100);
    var betweenPercent = (betweenHour / 24 * 100);
    var endPercent = 100 - betweenPercent - startPercent;

    const result = [
            startPercent + "%",
            betweenPercent + "%",
            endPercent + "%"]
        
    return result;
}

function Planetslider({planet,start,end}) {


    return (
        <div className="planet-slider flex flex-row">
            <div className="visible-from" style={{width:calculateTimeScale(start,end)[0]}}/>
            <div className="planet" style={{ backgroundColor:planet}}>
                <div className="time">{convert24to12(start)}</div>
            </div>
            <div className="visible" style={{width:calculateTimeScale(start,end)[1]}} />
            <div className="planet" style={{ backgroundColor:planet}}>
                <div className="time">{convert24to12(end)}</div>
            </div>
            <div className="visible-to" style={{width:calculateTimeScale(start,end)[2]}}/>
        </div>
    );
}

export default Planetslider;