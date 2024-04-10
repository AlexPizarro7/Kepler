import React from 'react';
import { UserProfile } from '@clerk/clerk-react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';


function Dashboard() {
    return (
        <div>
            <Header />
            <body>
                <h1>My Account</h1>
                <div className="flex z-[0] flex-row mt-[100px] ml-[5%]">
                    <UserProfile />
                </div>
            </body>
            <Footer />
        </div>
    )
}

export default Dashboard;