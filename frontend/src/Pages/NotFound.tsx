import React from 'react';



function NotFound() {
    return (
        <div className="content-wrapper">
            <main className="mt-[100px] ml-[20px]">
                <h1 className="font-bold text-2xl">404</h1>
                <p>Page not found. <a className="text-sky-500" href="/">Go back to the home page</a></p>
            </main>
        </div>
    )
}

export default NotFound;