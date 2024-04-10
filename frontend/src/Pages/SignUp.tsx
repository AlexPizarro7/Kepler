import React from 'react';
import { SignUp } from '@clerk/clerk-react';

function SignUpPage() {
    return (
        <div className="content-wrapper">
            <div className="flex flex-row mt-[100px] ml-[5%]">
                <SignUp signInUrl='/sign-in' />
            </div>
        </div>
    )
}

export default SignUpPage;