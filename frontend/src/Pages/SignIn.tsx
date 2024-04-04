import React from 'react';
import Header from '../Components/Header';
import { SignIn } from '@clerk/clerk-react';

function SignInPage() {
    return (
        <div>
            <Header />
            <div className="flex flex-row mt-[100px] ml-[5%]">
                <SignIn signUpUrl='/sign-up'/>
            </div>
        </div>
    )
}

export default SignInPage;