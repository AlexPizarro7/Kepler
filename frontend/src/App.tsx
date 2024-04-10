import React from 'react';
import {Routes, Route} from 'react-router-dom';
import Home from './Pages/Home';
import Calendar from './Pages/Calendar';
import FAQ from './Pages/FAQ';
import SignIn from './Pages/SignIn';
import NotFound from './Pages/NotFound';


function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/calendar" element={<Calendar />} />
        <Route path="/faq" element={<FAQ />} />
        <Route path="/sign-in" element={<SignIn />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;

