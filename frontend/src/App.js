import React from 'react';
import './App.css';
import Header from './Components/Header';
import Planetslider from './Components/Planetslider';

function App() {
  return (
    <div className="App">
      <Header />
      <Planetslider planet={"blue"} start={"6:00am"} end={"6:00pm"}/>
      <Planetslider />
      <Planetslider />
      <div className="bg-hero bg-cover bg-center pb-80">
        <h1 className="mt-20 ml-10 mr-10 text-6{xl font-bold text-left line-clamp-3 z-10">THE NEW AGE OF SPACE EXPLORATION</h1>
        <p className="ml-20 mt-8 text-2xl text-left z-10">Look up and look upon the stars.</p>
        <button className=" flex ml-20 mt-8 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg z-10">View the Calendar</button>
      </div>
      <div className="mt-20 bg-black pb-80">
        <h1 className="ml-20 text-8xl font-bold text-center">THE NEW AGE OF SPACE SIGHTSEEING</h1>
        <p className="ml-20 mt-8 text-2xl text-center underline">Look up and look upon the stars.</p>
        <button className=" ml-20 mt-8 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg">Signup Now</button>
      </div>
  </div>
  );
}

export default App;

