import { SignIn } from '@clerk/clerk-react';

function SignInPage() {
    return (
        <div className="content-wrapper">
            <div className="flex flex-row mt-[100px] ml-[5%]">
                <SignIn signUpUrl='/sign-up' />
            </div>
        </div>
    )
}

export default SignInPage;