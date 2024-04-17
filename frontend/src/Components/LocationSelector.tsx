import React, { useState } from "react";
import {
    CitySelect,
    CountrySelect,
    StateSelect,
    LanguageSelect,
} from "react-country-state-city";
import "react-country-state-city/dist/react-country-state-city.css";


const LocationSelector = () => {
    const [countryid, setCountryid] = useState(0);
    const [stateid, setstateid] = useState(0);

    return (
        <form className="ml-20 mr-20 bg-gradient-to-r from-slate-900 to-slate-700 p-[20px] flex flex-col justify-center rounded">
            <label className="font-bold">Country</label>
            <div className="text-black bg-gradient-to-r from-slate-500 to-slate-800">
                <CountrySelect
                    onChange={(e) => {
                        setCountryid(e.id);
                    }}
                    placeHolder="Select Country"
                />
            </div>
            <div className="state-city mt-10 flex  w-[80%]">
                <label className="mr-10 font-bold">State</label>
                <div className="text-black w-[50vw] bg-gradient-to-r from-slate-500 to-slate-800">
                    <StateSelect
                        countryid={countryid}
                        onChange={(e) => {
                            setstateid(e.id);
                        }}
                        placeHolder="Select State"
                    />
                </div>
                <label className="city ml-10 mr-10 font-bold">City</label>
                <input className="text-black rounded p-[5px] w-[80%]" type="text" placeholder="City" />
            </div>

            <button className="bg-gray-900 text-white hover:bg-blue-900 text-xl font-bold p-4 rounded-lg mt-4">Get Celestial Events</button>
            <style>
                {`
                    @media (max-width: 768px) {
                        .state-city {
                            flex-direction: column;
                        }
                        .city {
                            margin-top: 10px;
                            margin-left: 0px;
                        }
                    }
                    .stdropdown-menu:empty {
                        display: none;
                    }
                `}
            </style>
        </form>
    );

}

export default LocationSelector;