import React from 'react';
import Hamburger from './Hamburger';

function Header() {

    const [hamburgerOpen, setHamburgerOpen] = React.useState(false);

    const toggleHamburger = () => {
        setHamburgerOpen(!hamburgerOpen);
    }

    return (
        <div className="Header-nav">
            <div className="flex flex-row p-5">
                <div className="basis-1/4">
                    <a className="text-6xl font-bold" href="/">Kepler.</a>
                </div>
                <div className="navigation">
                    <ul>
                        <li>Home</li>
                        <li>Calendar</li>
                        <li>My Account</li>
                    </ul>
                </div>
                <div className="hamburger" onClick={toggleHamburger}>
                    <Hamburger />
                </div>
            </div>

            <style jsx>{`
        .navigation{
            width: 100%;
            height:50px;
        }
        .navigation ul{
            display: flex;
            flex-wrap: wrap;
            float: right;
            margin: 20 0px;
            padding: 0 25px;
        }

        .navigation ul {
            display: ${hamburgerOpen ? 'inline' : 'none'};
            background-color: black;
            height: 100vh;
            width: 50vw;
            margin-top: 50px;
            position: absolute;
        }

        .navigation ul li {
            list-style-type: none;
            padding-right: 10px;
        }
        .hamburger{
            display: flex;
            z-index: 10;
        }
    `}</style>
        </div>
    )
}

export default Header;