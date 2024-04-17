import {
    Calendar as BigCalendar,
    CalendarProps,
    momentLocalizer,
} from "react-big-calendar";
import React from "react";
import moment from "moment";

const localizer = momentLocalizer(moment);

export default function CalendarSelector(props: Omit<CalendarProps, "localizer">) {  
    return <BigCalendar {...props} localizer={localizer} />;
}