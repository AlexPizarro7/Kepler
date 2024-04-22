import moment from "moment";

type JsonType = {

    Latitude: number,
    Longitude: number,
    MoonPhase: string,
    LunarEclipse: string,
    Sunrise: string,
    Sunset: string,
    SunCulmination: string,
    MercuryRise: string,
    MercurySet: string,
    MercuryCulmination: string,
    VenusRise: string,
    VenusSet: string,
    VenusCulmination: string,
    MarsRise: string,
    MarsSet: string,
    MarsCulmination: string,
    JupiterRise: string,
    JupiterSet: string,
    JupiterCulmination: string,
    SaturnRise: string,
    SaturnSet: string,
    SaturnCulmination: string,
    NeptuneRise: string,
    NeptuneSet: string,
    NeptuneCulmination: string
}

export default function JsonParser(jsonObject: JsonType, date: string): void {
    var stringified = JSON.stringify(jsonObject);

    window.sessionStorage.setItem(date, stringified);
}

export function JsonParserRetriever(date: string): JsonType {
    const stringified = window.sessionStorage.getItem(date);

    if (stringified === null) {
        return null;
    }

    return JSON.parse(stringified);
}

export function JsonReturnEvents(EventList, date: string) {

    if (window.sessionStorage.getItem(date) != null) {
        var resultObject = JsonParserRetriever(date);
        EventList.push(
            {
                start: moment(resultObject.Sunrise).toDate(),
                end: moment(resultObject.Sunset).toDate(),
                title: "Sun"
            },
            {
                start: moment(resultObject.MercuryRise).toDate(),
                end: moment(resultObject.MercurySet).toDate(),
                title: "Mercury"
            },
            {
                start: moment(resultObject.VenusRise).toDate(),
                end: moment(resultObject.VenusSet).toDate(),
                title: "Venus"
            },
            {
                start: moment(resultObject.MarsRise).toDate(),
                end: moment(resultObject.MarsSet).toDate(),
                title: "Mars"
            },
            {
                start: moment(resultObject.JupiterRise).toDate(),
                end: moment(resultObject.JupiterSet).toDate(),
                title: "Jupiter"
            },
            {
                start: moment(resultObject.SaturnRise).toDate(),
                end: moment(resultObject.SaturnSet).toDate(),
                title: "Saturn"
            },
            {
                start: moment(resultObject.NeptuneRise).toDate(),
                end: moment(resultObject.NeptuneSet).toDate(),
                title: "Neptune"
            });
            
    }

    return EventList;

}