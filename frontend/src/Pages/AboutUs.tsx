import React from 'react';



function AboutUs() {
    return (
        <div className="content-wrapper">
            <main className="mt-[100px] ml-[20px] mb-20">
                <h1 className="font-bold text-2xl">About Us</h1>
                <p>Kepler was developed as a project to bring exploring the stars to enthusiests and novices alike with an easy to use calendar to show all events in one easy place.</p>
                <h2>Meet the Team</h2>
                <p><strong>Josh Duda:</strong> Full-Stack Developer</p>
                <p><strong>Alex Pizarro:</strong> Back-End Developer</p>
                <p><strong>Benjamin Garrett:</strong> DB Architect & Business Analysit</p>
                <p><strong>Eduardo Mata:</strong> QA Analyist & System Designer</p>
                <p><strong>Andrew Alvarez:</strong> QA Analyist & System Designer</p>
                <p><strong>Jackson Baggett:</strong> UI/UX Designer</p>

                <h2>There's more to come!</h2>
                <p>
                    Our team is constently working to bring more features to further expand the offerings of Kepler. The only thing we require,<br>
                    </br>
                    sign up with Kepler to view the calendar and sign up for email updates to stay informed when our new features our launched!
                </p>
                <h3>Future Plans</h3>
                <p><strong>Polution Mapping overlay:</strong> Find the closest are of darkness around you for optimal star gazing experiences</p>
                <p><strong>Note Taking:</strong> Store rich text notes about your star gazing experiences with the ability to review the conditions and the events automatically added to your notes.</p>
                <p><strong>Customizable Event Reminders:</strong> Set reminders for the upcoming events that you want to see.</p>
            </main>
        </div>
    )
}

export default AboutUs;