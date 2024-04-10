import React from 'react';
import { SignedIn, SignedOut } from '@clerk/clerk-react';



function Footer() {
    return (
        <div className="footer bg-[#0C0C0C]">
            <div className="grid grid-cols-3 mt-[20px] mb-[50px]">
                <div className="grid grid-cols-1">
                    <h2>About Us</h2>
                    <a className="ml-[30px] text-sm" href="/faq">FAQ</a>
                    <a className="ml-[30px] text-sm" href="/">About us</a>
                </div>
                <div className="grid grid-cols-1">
                    <h2>Features</h2>
                    <SignedIn>
                        <a className="ml-[30px] text-sm" href="/dashboard">My Account</a>
                        <a className="ml-[30px] text-sm" href="/calendar">Calendar</a>
                    </SignedIn>
                    <SignedOut>
                        <a className="ml-[30px] text-sm" href="/sign-in">Sign In</a>
                        <a className="ml-[30px] text-sm" href="/sign-in">Calendar</a>
                    </SignedOut>
                </div>
                <div className="grid grid-cols-1">
                    <h2>Legal</h2>
                    <a className="ml-[30px] text-sm" href="/privacy">Privacy Policy</a>
                    <a className="ml-[30px] text-sm" href="/faq">Terms of Use</a>
                </div>
            </div>
        <p className="ml-[10px] mb-[20px] center text-xs">© 2024 Kepler. All rights reserved.</p>
        <style>{`
            .footer {
                position: absolute;
                bottom: 0;
                width: 100%;
            }
            `}
            </style>
        </div>
    )
}

export default Footer;