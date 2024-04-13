import React from 'react';

export default function Hamburger() {
    return (
        <>
            <div className="hamburger">
                <div className="burger burger1 " />
                <div className="burger burger2" />
                <div className="burger burger3" />
            </div>
            <style>{`
                .hamburger {
                    width: 2rem;
                    height: 2rem;
                    display: flex;
                    justify-content: space-around;
                    flex-flow: column nowrap;
                    z-index: 10;
                }

                .burger{
                    width: 2rem;
                    height: 0.25rem;
                    background-color: #fff;
                    border-radius: 10px;
                    transform-origin: 1px;
                    transition: all 0.3s linear;
                }

                .hamburger:hover {
                    .burger{   
                        background-color: gray;
                    }
                }
        `}</style>
        </>
    )
}