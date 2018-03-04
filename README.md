# PDBAnalytics
Scripts and libraries for analysis on declassified PDB/PICL released by the CIA in 2015 and 2016.  

# The PDB or PICL: 
The President's Daily Brief (PDB), sometimes referred to as the President's Daily Briefing or the President's Daily Bulletin, is a top-secret document produced and given each morning to the President of the United States, and is also distributed to a small number of top-level US officials, and includes highly classified intelligence analysis, information about CIA covert operations and reports from the most sensitive US sources or those shared by allied intelligence agencies. The PDB is produced by the Director of National Intelligence,and involves fusing intelligence from the Central Intelligence Agency, the Defense Intelligence Agency, the National Security Agency, the Federal Bureau of Investigation and other members of the U.S. Intelligence Community.

All scripts in this repo are reliant on the FOIA releases by the CIA that are listed here: https://www.cia.gov/library/readingroom/presidents-daily-brief

# Intent: 
Provide an easy way to procure all publicly available PDB documents(currently these are from 1961-1977) in one location using simple Python 3.x scripts. In addition OCR will be added to convert the image based PDFs to a machine readable format for further analysis. Of particular interest is time series and frequency analysis using the lens of history to gain insight into the Cold War era Oval Office.

# Libraries used: 
BeautifulSoup4 : https://www.crummy.com/software/BeautifulSoup/
