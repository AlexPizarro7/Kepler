import React from 'react';
import Hamburger from './Hamburger';
import { Link } from 'react-router-dom';
import { RedirectToSignUp, SignedIn, SignedOut, UserButton } from '@clerk/clerk-react';

function Header() {

    const [hamburgerOpen, setHamburgerOpen] = React.useState(false);

    const toggleHamburger = () => {
        setHamburgerOpen(!hamburgerOpen);
    }

    return (
        <div className="header-nav Z-0">
            
            <div className=" navigation flex flex-row p-5 w-full h-20 bg-[#0C0C0C] fixed top-0">
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
                                <Link to="/sign-up">Sign In</Link>
                            </SignedOut>
                        </li>
                        <li>
                            <SignedIn>
                                <Link to="/calendar">Calendar</Link>
                            </SignedIn>
                            <SignedOut>
                                <Link to="/sign-up">Calendar</Link>
                            </SignedOut>
                        </li>
                        <li>
                            <Link to="/faq">FAQ</Link>
                        </li>
                    </ul>
                </div>
            </div>

            <style>{`

        .menu {
            display: ${hamburgerOpen ? 'inline' : 'none'};
            background-color: #0C0C0C;
            height: 100%;
            width: 30vw;
            margin-top: 40px;
            position: fixed;
            text-align: center;
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