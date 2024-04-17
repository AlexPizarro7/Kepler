import React, {useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import BackgroundBeamsDemo from '../Components/BBTest';
import StarsTest from '../Components/Stars';
import FeatureSection from '../Components/FeatureSection';

function Home() {
    const navigate = useNavigate();

    const handleCalendarCTA = () => {

        if (document.cookie.match(/^(.*;)?\s*__session\s*=\s*[^;]+(.*)?$/) == null) {
            navigate('/sign-up')
        } else {
            navigate('/calendar')
        }
    }
    return (

        <div className="flex flex-col content-wrapper">
            <div className="bg-solar bg-cover bg-center pb-40">
                <h2 className="text-right pt-20 ml-10 mr-10 text-6xl font-bold text-left line-clamp-3 z-10 uppercase">View the <br /> Celestial Calendar</h2>
                <p className="text-right ml-20 mr-10 mt-8 text-2xl text-left z-10">Sign in to see the celesital events <br /> that are happening in your area.</p>
                <button onClick={handleCalendarCTA} className="float-right flex ml-20 mt-8 mr-10 bg-gray-700 text-white hover:bg-black text-xl font-bold p-4 rounded-lg z-10">View the Calendar </button>
            </div>
            <div>
            </div>
            <div className="bg-[linear-gradient(110deg,#000_0.6%,#000b3d)]"> 
                <StarsTest />
            </div>
            <BackgroundBeamsDemo />
            <div className="bg-[linear-gradient(70deg,#000_0.6%,#000b3d)] pt-20 pb-20">
                <FeatureSection />
            </div>
        </div>
    )
}

export default Home;