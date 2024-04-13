import React, { useState } from 'react';
import Accordion from './ui/accordion';

const FAQAccordion = () => {
  const [expanded, setExpanded] = useState(false);

  const accordionIds = [
    {
      title:"What is Kepler?",
      description:"Kepler's goal is to provide those interested in celestial events an easy tool to find events that are visible in their specific area any time of year."
   },
   {
      title:"How do I view the celestial calendar?",
      description:"Sign in or sign up to view the celestial calendar!"
   },
   {
    title:"How do I sign up?",
    description:"Click the sign in button in the navigation menu and use your email or your other accounts to sign up or sign in!"
   },
   {
    title:"How can I delete my account?",
    description:"After signing in either click your profile picture in the navigation menu and select manage account or select My Account and click the delete account button."
   }
  ];

  return (
    <div>
      <div className="faq-items">
        {accordionIds.map((item, i) => (
          <Accordion
            key={i}
            i={i}
            expanded={expanded}
            setExpanded={setExpanded}
            title={item.title}
            description={item.description}
          />
        ))}
      </div>
    </div>
  );
};

export default FAQAccordion;