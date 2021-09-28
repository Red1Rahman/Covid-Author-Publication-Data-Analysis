import sys, pandas as pd, json

# Receive and convert input
inputAuthorIdStringList = sys.stdin.read()
authorIdList = inputAuthorIdStringList.split(',')
authorIdList.pop()

# Convert dataset
covidAuthorData = pd.read_csv('./OriginalDataset/CovidAuthorsData.csv')
covidAuthorData["Author ID"] = authorIdList
covidAuthorData["Full Name"] = covidAuthorData["Last Name"] + ", " + covidAuthorData["First Name"]
covidAuthorData["Total Publications on Coronavirus"] = covidAuthorData["Covid-19 Publications"].apply(lambda x: len([t for t in str(x).split(';') if not pd.isnull(t) == True])) + covidAuthorData["Other Coronavirus Publications"].apply(lambda x: len([t for t in str(x).split(';') if not pd.isnull(t) == True])) - 1
selectedColumnsAuthorData = ["Author ID", "Full Name", "First Name", "Middle Name","Last Name", "Country", "Covid-19 Publications", "Other Coronavirus Publications", "Total Publications on Coronavirus"]
covidAuthorData["Author ID"] = pd.to_numeric(covidAuthorData["Author ID"])
covidAuthorData[selectedColumnsAuthorData].to_csv('./MinedDataset/covidAuthorData.csv', index=True)

# Convert calculates centrality
centralityDataWithDuplicate = pd.read_csv('./OriginalDataset/CalculatedCentralityScore.csv')
selectedColumnsCentralityData = ["Author ID", "betweenness", "centrality"]
cleanCentralityData = centralityDataWithDuplicate.drop_duplicates(subset = ['Author ID'],keep = 'last').reset_index(drop = True)
cleanCentralityData[selectedColumnsCentralityData].to_csv('./MinedDataset/cleanCentralityData.csv', index=True)

# Merge files
datasetForCovidAuthorConnectivityGraph = pd.merge(covidAuthorData[selectedColumnsAuthorData],
                                                cleanCentralityData[selectedColumnsCentralityData], 
                                                on='Author ID', 
                                                how='inner')

datasetForCovidAuthorConnectivityGraph.to_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv', index=True)