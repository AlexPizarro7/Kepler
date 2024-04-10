import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import reportWebVitals from './reportWebVitals';

import RootLayout from './Layouts/root-layout';
import DashboardLayout from './Layouts/dashboard-layout';

import Home from './Pages/Home';
import Calendar from './Pages/Calendar';
import FAQ from './Pages/FAQ';
import SignIn from './Pages/SignIn';
import SignUp from './Pages/SignUp';
import Dashboard from './Pages/Dashboard';
import DashboardInvoices from './Pages/DashboardInvoices';
import NotFound from './Pages/NotFound';


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
      { path: '*', element: <NotFound />},
      { 
        element: <DashboardLayout />,
        path: 'dashboard',
        children: [
        { path: "/dashboard", element: <Dashboard /> },
        { path: "/dashboard/invoices", element: <DashboardInvoices /> },
        { path: '*', element: <NotFound />},
        ]
       }
    ]
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
