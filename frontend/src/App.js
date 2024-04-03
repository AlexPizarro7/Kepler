import React from 'react';
import {Routes, Route} from 'react-router-dom';
import Home from './Pages/Home';
import Calendar from './Pages/Calendar';
import FAQ from './Pages/FAQ';
import Login from './Pages/Login';


function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/calendar" element={<Calendar />} />
        <Route path="/faq" element={<FAQ />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}

export default App;

