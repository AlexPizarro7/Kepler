import React from 'react';
import Hamburger from './Hamburger';
import { Link } from 'react-router-dom';
import { SignedIn, SignedOut, UserButton } from '@clerk/clerk-react';

function Header() {

    const [hamburgerOpen, setHamburgerOpen] = React.useState(false);

    const toggleHamburger = () => {
        setHamburgerOpen(!hamburgerOpen);
    }

    return (
        <div className="header-nav">
            
            <div className=" navigation flex flex-row p-5 w-full h-20 bg-[#0C0C0C] fixed top-0  z-[10]">
                <Link to="/" className="text-6xl h-20 font-bold fixed top-0">Kepler.</Link>
                <div className="hamburger mt-5 right-10 top-0" onClick={toggleHamburger}>
                    <Hamburger />
                </div>
                <div className="menu end-0">
                    <ul>
                        <li>
                            <SignedIn>
                                <div className="ml-[45%]">
                                    <UserButton afterSignOutUrl='/sign-in' />
                                </div>
                            </SignedIn>
                            <SignedOut>
                                <Link className="hover:text-gray-300 text-lg" to="/sign-in">Sign In</Link>
                            </SignedOut>
                        </li>
                        <li>
                            <SignedIn>
                                <Link className="hover:text-gray-300 text-lg" to="/dashboard">My Account</Link>
                            </SignedIn>
                        </li>
                        <li>
                            <SignedIn>
                                <Link className="hover:text-gray-300 text-lg" to="/calendar">Calendar</Link>
                            </SignedIn>
                            <SignedOut>
                                <Link className="hover:text-gray-300 text-lg" to="/sign-in">Calendar</Link>
                            </SignedOut>
                        </li>
                        <li>
                            <Link className="hover:text-gray-300 text-lg" to="/faq">FAQ</Link>
                        </li>
                    </ul>
                </div>
            </div>

            <style>{`

        .menu {
            display: ${hamburgerOpen ? 'inline' : 'none'};
            background-color: #0C0C0C;
            height: 25%;
            min-height: 200px;
            width: 30vw;
            margin-top: 40px;
            padding-top: 40px;
            position: fixed;
            text-align: center;
            border-radius: 10% 0% 0% 10%;
            box-shadow: 0 0 10px 0 rgba(0,0,0,1);
        }

        .menu li {
            list-style-type: none;
        }

        .hamburger{
            position: fixed;
            .burger {
                background-color: ${hamburgerOpen ? 'grey' : 'white'};
            }
        }
    `}
            </style>
        </div>
    )
}

export default Header;