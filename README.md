# Quebec-ER-Load-Prediction
Group project for the Data Lakes and Data Warehouse project.

# Research questions possibilities
- How does traffic and traffic incidents impact ER load in hospitals of Montréal and Québec ? Do the incidents types have an impact on the ER load ?
- How does the weather and the weekday/holiday impact ER load in hospitals of Montréeal and Québec ?
- Are there significant differences in hospitals ER loads within the same city at the same moment ? Can this difference be explained by the hospital ER capacity (hospital size) ? Or by the hospital's proximity with the current traffic incidents ?
- What are the daily (and seasonal) ER load patterns of hospitals in Québec ?
- Is it possible to predict with an accuray of 90% the overall ER load in the hospitals of Montréal and Québec for the next 1 to 24h given historical data, weather data, traffic data and calendar data ?

-> We have to keep in mind that we will at most have a few months of data. Some answers we find might be incomplete / not very precise.

# Accessible data 

## Québec ER load data
[API doc](https://sante.handled.tools/en/donnees)
Hourly load data for many hospitals. Data like hospital name, hospital id, belonging establishement, region code and name (interesting for data aggregation).
For each hospital with data, current number of waiting patients, number of functional stretcher capacity, number of occupied stretchers, stretcher occupancy rate, patients waiting 24+ hours on a stretcher (27), patients waiting 48+ hours on a stretcher, total patients currently in the ER, number of patients waiting to see a doctor, average stretcher stay, average ambulatory (non-stretcher) stay, timestamp of the reading (2026-09-25 14:00)
Only the last week of data is retrievable through the API, the rest is accessible through a csv file downloadable on the website [link](https://sante.handled.tools/archive-120-urgences-horaire.csv).

This service needs no authentification. The data is json-like (can be converted into (lists of) dictionnaries).

## Traffic data
[API doc](https://docs.tomtom.com/traffic-api/api-explorer/tomtom-orbis-maps-v2/traffic-orbis-v2)
Tomtom's API enables to gather data from traffic, like absolute and relative driving speed on each road, the road category, the road importance ranking, the road's coordinates ([doc](https://docs.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/v1/traffic-flow/vector-flow-tiles)). Another endpoint offers data about traffic incidents, like accident type, roadworks, lane closures, delay in seconds, average speed within the incident, number of user reports, incident descriptions ([doc](https://docs.tomtom.com/traffic-api/documentation/tomtom-orbis-maps/v2/traffic-incidents/vector-incident-tiles)).
The data is either geoJSON or JSON.

This service needs authentification.

In case this service is not satisfactory enough, the use of the HERE platform could be invastigated [doc](https://docs.here.com/traffic-api/docs/introduction-to-here-traffic-api-v7).

## Meteorological data
[API doc](https://open-meteo.com/en/docs)
Open-meteo is a service that offers meteo data given a latitude and longitude. One endpoint offers current data and another one offers historical data. Many measurements are retrievable (tmeperature, precipitations, snowfall, windspeed, humidity, ...).
This service needs no authentification.

## Calendar data
[API doc](https://www.abstractapi.com/api/holidays-api)
APi offering data about public holidays and weekday.
This service needs authentification.
