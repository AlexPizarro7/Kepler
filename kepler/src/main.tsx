import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom'

import RootLayout from './Layouts/root-layout';
import DashboardLayout from './Layouts/dashboard-layout';

import Home from './Pages/Home';
import Calendar from './Pages/Calendar';
import FAQ from './Pages/FAQ';
import SignIn from './Pages/SignIn';
import SignUp from './Pages/SignUp';
import Dashboard from './Pages/Dashboard';
import NotFound from './Pages/NotFound';
import Privacy from './Pages/Privacy';
import AboutUs from './Pages/AboutUs';
import TermsOfUse from './Pages/TermsOfUse';

// Import your publishable key
const PUBLISHABLE_KEY :string = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;


if (!PUBLISHABLE_KEY) {
  throw new Error("Missing Publishable Key")
}

const router = createBrowserRouter([
  {
    element: <RootLayout />,
    children: [
      { path: '/', element: <Home /> },
      { path: 'calendar', element: <Calendar /> },
      { path: 'faq', element: <FAQ /> },
      { path: 'sign-in', element: <SignIn /> },
      { path: 'sign-up', element: <SignUp /> },
      { path: 'privacy', element: <Privacy />},
      { path: 'terms-of-use', element: <TermsOfUse />},
      { path: 'about-us', element: <AboutUs />},
      { path: '*', element: <NotFound />},
      { 
        element: <DashboardLayout />,
        path: 'dashboard',
        children: [
        { path: "/dashboard", element: <Dashboard /> },
        { path: '*', element: <NotFound />},
        ]
       }
    ]
  }
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
