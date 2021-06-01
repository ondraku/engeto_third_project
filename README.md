# Elections Scraper Project
---
Final project for the Engeto Academy.
---
This project let you extract results of the Czech parliament elections from 2017. 
The source URL for this project can be found [here](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

### Libraries
You can find the list of libraries needed for running this project in the file "requirements.txt".

### Running the Elections Scraper
You will need two arguments to run the Elections Scraper project (main.py):
- The URL of desired municipality ("Výběr okrsku");
- The name of the file;

The results will be downloaded and saved to a .csv file for you.

### Example
Elections Scraper will get you the results of municipality Chomutov:
- First argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4202
- Second argument: chomutov_results

The program will notify you once the process is finished:

> Process is now done!

> Your file chomutov_results.csv is ready for checking.

> Thank you for using the Elections Scraper app!

Export sample:
> ID	Name	Registered voters	Envelopes	Valid Votes

> 562980	Bílence	186	113	113	4	1	0	5	5	10	0	0	1	0	0	5	2	4	54	0	1	4	0	2	0	0	15	0

> 562998	Blatno	434	287	287	36	0	0	11	17	36	4	2	2	0	0	27	0	6	105	0	1	5	0	2	0	0	32	1

> 563005	Boleboř	223	150	150	20	0	0	7	13	20	0	5	2	0	0	10	0	5	47	0	0	1	0	0	0	2	17	1





