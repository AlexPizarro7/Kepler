import React from 'react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
import { SignIn } from '@clerk/clerk-react';

function SignInPage() {
    return (
        <div>
            <Header />
            <body className="flex flex-row mt-[100px] ml-[5%]">
                <SignIn signUpUrl='/sign-up' />
            </body>
            <Footer />
        </div>
    )
}

export default SignInPage;