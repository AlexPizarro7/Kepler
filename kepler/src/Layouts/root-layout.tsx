import { Outlet, useNavigate } from 'react-router-dom';
import { ClerkProvider} from '@clerk/clerk-react';
import Header from '../Components/Header';
import Footer from '../Components/Footer';
 
const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
 
if (!PUBLISHABLE_KEY) {
  throw new Error("Missing Publishable Key")
}
 
export default function RootLayout() {
  const navigate = useNavigate();
  
  return (
    <ClerkProvider navigate={navigate} publishableKey={PUBLISHABLE_KEY}>
            <Header />
        <main>
            <Outlet />
        </main>
        <Footer />
    </ClerkProvider>
  )
}