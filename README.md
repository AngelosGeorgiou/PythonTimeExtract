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

## Todo:
- Set path as input
- Chose weekly or daily output
- Set when week starts
- Create and run test suite
- GUI