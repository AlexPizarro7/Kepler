import React from 'react';
import './App.css';
import Header from './Components/Header';

function App() {
  return (
    <div className="App">
      <div className="bg-hero bg-cover bg-center pb-80">
        <Header />
        <h1 className="mt-20 ml-10 mr-10 text-6xl font-bold text-left line-clamp-3">THE NEW AGE OF SPACE EXPLORATION</h1>
        <p className="ml-20 mt-8 text-2xl text-left">Look up and look upon the stars.</p>
        <button className=" flex ml-20 mt-8 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg ">View the Calendar</button>
      </div>
      <div className="mt-20 bg-black pb-80">
        <h1 className="ml-20 text-8xl font-bold text-center">THE NEW AGE OF SPACE SIGHTSEEING</h1>
        <p className="ml-20 mt-8 text-2xl text-center underline">Look up and look upon the stars.</p>
        <button className=" ml-20 mt-8 bg-orange-600 text-black hover:bg-orange-300 text-xl font-bold p-4 rounded-lg ">Signup Now</button>
      </div>
  </div>
  );
}

export default App;

