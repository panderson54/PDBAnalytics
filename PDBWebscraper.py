import urllib.request 
import re
import sys
from bs4 import BeautifulSoup


def downloadPDBTitlesAndDocIds(baseUrl, urlLogFileName, pages):
    for i in range (0, pages +1):
        url = baseUrl + str(i)
        print(url)
        website = urllib.request.urlopen(url)
        html = website.read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        links=[]
        titles = soup.find_all('h4', {"class": "field-content"})
        docs = soup.find_all('span', {"class": "field-content"})
        titleDocList = []
        for item in docs:
            if item.text == "":
                docs.remove(item)
        for k in range(len(titles)):
            titleDocList.append(titles[k].text + " ? " + docs[k].text + "\n")
            print(titleDocList[-1])
        with open(urlLogFileName, "a") as myfile:
            for item in titleDocList:
                myfile.write(item)
        print("Finished Writing Page: " + str(i + 1))
    
def downloadPDFsFromPDBLog(urlLogFile, baseUrl, filePath):
    with open(urlLogFile) as f:
        initList = [line.rstrip('\n') for line in open(urlLogFile)]
    for line in initList:
        temp = line.replace(" ", "").replace("'","").split("?")
        docNum = temp[1]
        fileName = temp[0].replace("THEPRESIDENTSINTELLIGENCECHECKLIST","PICL-").replace("THEPRESIDENTSDAILYBRIEF","PDB-")+ ".pdf"
    
        print('Downloading: ' +fileName +' ...')
        url = baseUrl + "DOC_" + docNum + ".pdf"
        print('From: ' +url +' ...')
        urllib.request.urlretrieve(url, filePath + fileName)  
        print('Finished: ' + fileName)

def getAllPDBs(urlLogFileName, filePath):
    #urlLogFileName = "PDBLinks.txt"
    #filePath = 'F:\Desktop\Programming\Projects\Python\PDB\PDBArchive\\'
    pdb1969To1977 = "https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1969-1977?page="
    pdb1961To1969 = "https://www.cia.gov/library/readingroom/collection/presidents-daily-brief-1961-1969?page="
    pdfUrl= "https://www.cia.gov/library/readingroom/docs/"
    
    downloadPDBTitlesAndDocIds(pdb1961To1969, urlLogFileName, 124)
    downloadPDBTitlesAndDocIds(pdb1969To1977, urlLogFileName, 126)
    downloadPDFsFromPDBLog(urlLogFileName, pdfUrl, filePath)
