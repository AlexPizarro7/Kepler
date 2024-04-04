import React from 'react';
import Header from '../Components/Header';
import { SignUp } from '@clerk/clerk-react';

function SignUpPage() {
    return (
        <div>
            <Header />
            <div className="flex flex-row mt-[100px] ml-[5%]">
                <SignUp signInUrl='/sign-in'/>
            </div>
        </div>
    )
}

export default SignUpPage;