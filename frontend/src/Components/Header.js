import React from 'react';
import Hamburger from './Hamburger';

function Header() {

    const [hamburgerOpen, setHamburgerOpen] = React.useState(false);

    const toggleHamburger = () => {
        setHamburgerOpen(!hamburgerOpen);
    }

    //@TODO: https://www.codevertiser.com/reactjs-responsive-navbar/

    return (
        <div className="header-nav Z-[50] h-[80px]">
            <div className=" navigation flex flex-row p-5 w-full h-20 bg-black fixed top-0">
                <a className="text-6xl h-20 font-bold fixed top-0" href="/">Kepler.</a>
                <div className="hamburger mt-5 right-10 top-0" onClick={toggleHamburger}>
                    <Hamburger />
                </div>
                <div className="menu end-0">
                    <ul>
                        <li>
                            <a href="/">Calendar</a>
                        </li>
                        <li>
                            <a href="/faq">FAQ</a>
                        </li>
                        <li>
                            <a href="/logi">Login/Signup</a>
                        </li>
                    </ul>
                </div>
            </div>

            <style jsx>{`

            @media (min-width:768px){
                .hamburger{
                    position: fixed;
                    .burger {
                        background-color: ${hamburgerOpen ? 'grey' : 'white'};
                    }
                }
            }

        .menu {
            display: ${hamburgerOpen ? 'inline' : 'none'};
            background-color: black;
            height: 100%;
            width: 40vw;
            margin-top: 40px;
            position: fixed;
        }

        .menu li {
            list-style-type: none;
        }
    `}
            </style>
        </div>
    )
}

export default Header;