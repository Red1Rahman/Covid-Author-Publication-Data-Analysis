import pandas as pd

covidAuthorData = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')

publlicationDictionary = {}
for index, row in covidAuthorData.iterrows():
    currentRowPublicationList = row["All Publications on Coronavirus"].split(';')
    for publicationId in currentRowPublicationList:
        publicationId = publicationId.replace('nan', '')
        if publicationId not in publlicationDictionary.keys():
            publlicationDictionary[publicationId] = []    
        publlicationDictionary[publicationId].append(row["Author ID"])


datasetOfEachPublicationAuthors = pd.DataFrame({'Publication': publlicationDictionary.keys(), 'Authors': publlicationDictionary.values()})
datasetOfEachPublicationAuthors.to_csv('./MinedDataset/datasetOfEachPublicationAuthors.csv')


