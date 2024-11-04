# TimeParser

## File format
Should contain in first line the date as YYYY-MM-HH.
Will check every line for at least two instances of the time with HH:MM format
The first will be the start time and the last, the end time
A file can have multiple lines with timestamps.
All of them will be added for the daily report
A weekly report can be generated

Example of date format
> "2024-10-29" 

Example of time format
> 21:35 - 22:09 

## Prerquisites
- `pip install pyqt5`
- path of the directory to extract time saved with quotes ("") in a file named "data3.txt"
- file under image folder named playas as background to UI

## Release Notes
- v0.1.1: Fix double printing last week with empty total hours
- v0.2.0: Introduced simple UI, Displays only Total for now
    - Based on https://medium.com/analytics-vidhya/how-to-build-your-first-desktop-application-in-python-7568c7d74311

## Todos:
- Set path as input
- Chose weekly or daily output
- Set when week starts
- Create and run test suite
- GUI 👈
