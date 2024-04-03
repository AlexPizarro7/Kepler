import './planetslider.css';
import mars from '../img/mars.png';
import saturn from '../img/saturn.png';

function Planetslider({planet,start,end}) {

    var color = "brown"
    var pimage = mars;

    switch (planet) {
        case "mars":
            pimage = mars;
            break;
        case "jupiter":
            color = "tan"
            break;
        case "saturn":
            pimage  = saturn;
            break;
        default:
            color = "brown"
            break;
    }

    console.log(start.split(":")[0])
    var visibility_from = 100*(parseInt(start.split(":")[0])/24);
    console.log(end.split(":")[0])
    var visibility_to = 100*(parseInt(end.split(":")[0])/24);
    const visible = visibility_to - visibility_from;
    visibility_to = 100 - visibility_to;

    console.log(start,visibility_from,visible,end,visibility_to);

    return (
    <div className='planet-slider-wrapper'>
        <div>
            <img className='planet' src={`${pimage}`} alt={`${planet}`} />
            <div className="planet-name">{planet}</div>
        </div>
        <div className="planet-slider flex flex-row">
            <div className={`visible-from visible-from-${planet}`} />
            <div className={`tip`}>
                <div className="time">{start}</div>
            </div>
            <div className={`visible visible-${planet}`} />
            <div className={`tip`}>
                <div className="time">{end}</div>
            </div>
            <div className={`visible-to visible-to-${planet}`} />
            
            <style jsx>{`

            .visible-from-${planet} {
                width: ${visibility_from}%;
            }

            .visible-to-${planet} {
                width: ${visibility_to}%;
            }

            .visible-${planet} {
                width: ${visible}%;
            }
            `}
            </style>
        </div>
    <div/>
    </div>
    );
}

export default Planetslider;