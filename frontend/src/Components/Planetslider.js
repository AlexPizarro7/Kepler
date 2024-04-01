import './planetslider.css';

function Planetslider({planet,start,end}) {

    return (
        <div className="planet-slider flex flex-row">
            <div className="visible-from" />
            <div className="planet" style={{ backgroundColor:planet}}>
                <div className="time">{start}</div>
            </div>
            <div className="visible" />
            <div className="planet" style={{ backgroundColor:planet}}>
                <div className="time">{end}</div>
            </div>
            <div className="visible-to" />
        </div>
    );
}

export default Planetslider;