import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';



function NotFound() {
    return (
        <div>
            <Header />
            <body className="mt-[100px] ml-[20px]">
                <h1 className="font-bold text-2xl">404</h1>
                <p>Page not found. <a className="text-sky-500" href="/">Go back to the home page</a></p>
            </body>
            <Footer />
        </div>
    )
}

export default NotFound;