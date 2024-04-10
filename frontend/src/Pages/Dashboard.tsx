import React from 'react';
import { UserProfile } from '@clerk/clerk-react';


function Dashboard() {
    return (
        <div className="content-wrapper">
                <h1>My Account</h1>
                <div className="flex z-[0] flex-row mt-[100px] ml-[5%]">
                    <UserProfile />
                </div>
        </div>
    )
}

export default Dashboard;