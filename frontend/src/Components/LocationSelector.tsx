import React, { useState } from "react";
import {
    CitySelect,
    CountrySelect,
    StateSelect
} from "react-country-state-city";
import "react-country-state-city/dist/react-country-state-city.css";
import RequestAstronomy from "../AstronomyAPI";

const queryCelestialEvents = (country, city, state, zip) => {

    var local_date = window.localStorage.getItem("selected_date");

    if (local_date === null) {
        const current_date = new Date();
        const year = current_date.getUTCFullYear();
        const month = current_date.getUTCMonth();
        if (month < 10) {
            var monthStr = "0" + month;
        }else{
            monthStr = month.toString();
        }
        const day = current_date.getUTCDate();
        window.localStorage.setItem("selected_date", monthStr  +"-"+ day +"-"+ year);
    }

    local_date = window.localStorage.getItem("selected_date");

    if (window.localStorage.getItem("selected_location") === city+", "+state+" "+country) {
        window.localStorage.setItem("newLocation", "false");
    }else {
        window.localStorage.setItem("newLocation", "true");
    }

    if (state === "") {  
        window.localStorage.setItem("selected_location", city+" "+ country);
    } else {
        window.localStorage.setItem("selected_location", city+", "+ state +" "+ country);
    }
    
    if (state === "") {
        RequestAstronomy(country, city, "", "", local_date);
    } else if (zip === "") {
        RequestAstronomy(country, city, state, "", local_date);
    } else {
        RequestAstronomy(country, city, state, zip, local_date);
    }

}


const LocationSelector = () => {
    const [countryid, setCountryid] = useState(0);
    const [stateid, setStateid] = useState(0);
    const [country, setCountry] = useState("");
    const [state, setState] = useState(""); 
    const [city, setCity] = useState("");

    return (
        <form className="ml-20 mr-20 bg-gradient-to-r from-slate-900 to-slate-700 p-[20px] flex flex-col justify-center rounded">
            <label className="font-bold">Country</label>
            <div className="text-black bg-gradient-to-r from-slate-500 to-slate-800">
                <CountrySelect
                    onChange={(e) => {
                        setCountryid(e.id);
                        setCountry(e.iso3);
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
                            setStateid(e.id);
                            setState(e.name);
                        }}
                        placeHolder="Select State"
                    />
                </div>
                <label className="city ml-10 mr-10 font-bold">City</label>
                <div className="text-black w-[50vw] bg-gradient-to-r from-slate-500 to-slate-800">
                    <CitySelect
                        countryid={countryid}
                        stateid={stateid}
                        onChange={(e) => {
                            setCity(e.name);
                        }}
                        placeHolder="Select City"
                    />
                </div>
            </div>
            <button type="button" onClick={()=>queryCelestialEvents(country,city,state,"")} className="bg-gray-900 text-white hover:bg-blue-900 text-xl font-bold p-4 rounded-lg mt-4">Get Celestial Events</button>
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