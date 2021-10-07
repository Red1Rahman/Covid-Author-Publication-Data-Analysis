import pandas as pd, itertools

covidAuthorData = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')

publlicationDictionary = {}

for index, row in covidAuthorData.iterrows():
    currentRowPublicationList = row["All Publications on Coronavirus"].split(';')
    for publicationId in currentRowPublicationList:
        publicationId = publicationId.replace('nan', '')
        if publicationId not in publlicationDictionary.keys():
            publlicationDictionary[publicationId] = {}
        
        publlicationDictionary[publicationId][str(row["Author ID"])] = {'Name': row["Full Name"], 'Country' : row["Country"]}


datasetOfEachPublicationAuthors = pd.DataFrame({'Publication': publlicationDictionary.keys(), 'Authors': publlicationDictionary.values()})
datasetOfEachPublicationAuthors.to_csv('./MinedDataset/datasetOfEachPublicationAuthorsWithMoreInfo.csv')

coAuthorDictionary = {}

for publicationId in publlicationDictionary.keys():
    authorIdList = publlicationDictionary[publicationId].keys()
    for authorId in authorIdList:
        country = publlicationDictionary[publicationId].get(authorId).get('Country')
        name = publlicationDictionary[publicationId].get(authorId).get('Name')
        if authorId not in coAuthorDictionary.keys():
            coAuthorDictionary[authorId] = {'Name': name, 'Country' : country, 'CoAuthors': []}


        for coAuthorId in authorIdList:
            if(authorId!=coAuthorId and coAuthorId not in coAuthorDictionary[authorId]):
                coAuthorDictionary[authorId].get('CoAuthors').append(coAuthorId)

coAuthorNetworkDataSet = pd.DataFrame.from_dict(coAuthorDictionary, orient='index')
coAuthorNetworkDataSet.to_csv('./MinedDataset/coAuthorNetworkDataSetWithMoreInfo.csv')