import React from 'react';
import {useNavigate} from 'react-router-dom';
import Header from '../Components/Header';

function Home() {
    const navigate = useNavigate();

    const handleCalendarCTA = () => {
        navigate('/calendar');
    }

    return (
    <div className="flex flex-col">
        <Header />
        <div className="bg-solar bg-cover bg-center pb-40 mt-[50px]">
            <h2 className="text-right pt-20 ml-10 mr-10 text-6xl font-bold text-left line-clamp-3 z-10 uppercase">Want to see the April 8th total eclipse?</h2>
            <p className="text-right ml-20 mr-10 mt-8 text-2xl text-left z-10">Check where and when to see it!</p>
            <button  onClick={handleCalendarCTA} className="float-right flex ml-20 mt-8 mr-10 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg z-10">View the Calendar </button>
        </div>
        <div className="mt-20 bg-black pb-80">
            <h2 className="ml-20 text-8xl font-bold text-center">THE NEW AGE OF SPACE SIGHTSEEING</h2>
            <p className="ml-20 mt-8 text-2xl text-center underline">Look up and look upon the stars.</p>
            <button className=" ml-20 mt-8 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg">Signup Now</button>
        </div>
    </div>
    )
}

export default Home;