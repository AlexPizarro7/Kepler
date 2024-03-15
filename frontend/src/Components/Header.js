import React from 'react';

function Header() {
return (
    <div className="Header-nav">
    <div className="flex flex-row p-5">
        <div className="basis-1/4">
            <a className="text-6xl font-bold" href="/">Kepler .</a>
        </div>
        <div className="basis-3/4"></div>
        <div className="p-2 ml-6 basis-1/4">
            <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 18L20 18" stroke="#FFFF" stroke-width="2" stroke-linecap="round"/>
                <path d="M4 12L20 12" stroke="#FFFF" stroke-width="2" stroke-linecap="round"/>
                <path d="M4 6L20 6" stroke="#FFFF" stroke-width="2" stroke-linecap="round"/>
            </svg>
        </div>
    </div>
    </div>
)
}

export default Header;