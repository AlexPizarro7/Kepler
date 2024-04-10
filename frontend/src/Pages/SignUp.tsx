import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import { SignUp } from '@clerk/clerk-react';

function SignUpPage() {
    return (
        <div>
            <Header />
            <body className="flex flex-row mt-[100px] ml-[5%]">
                <SignUp signInUrl='/sign-in' />
            </body>
            <Footer />
        </div>
    )
}

export default SignUpPage;