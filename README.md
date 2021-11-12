Departure timetables
===

This project processes timetables in GTFS format and then provides simple HTTP API to get departures for required lines.
Intended usage is for small, IoT devices which should display nearest departures from following stop, but they don't 
have enough resources to parse timetables itself.

TODO
---
- [ ] Process GTFS data and load them into database
- [ ] Stops and lines listing
- [ ] Departure times search API

Development
---
This project contains development bundle in docker-compose. To get it up and running, just run
```shell
docker-compose up --build
```
The app will then be available at http://localhost:8000

