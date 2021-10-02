import pandas as pd, itertools

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

coAuthorDictionary = {}

for publicationId in publlicationDictionary.keys():
    authorIdList = publlicationDictionary[publicationId]
    for authorId in authorIdList:
        if authorId not in coAuthorDictionary.keys():
            coAuthorDictionary[authorId] = []
        for coAuthorId in authorIdList:
            if(authorId!=coAuthorId and coAuthorId not in coAuthorDictionary[authorId]):
                coAuthorDictionary[authorId].append(coAuthorId)

coAuthorNetworkDataSet = pd.DataFrame({'AuthorId': coAuthorDictionary.keys(), 'Co-Authors': coAuthorDictionary.values()})
coAuthorNetworkDataSet.to_csv('./MinedDataset/coAuthorNetworkDataSet.csv')

