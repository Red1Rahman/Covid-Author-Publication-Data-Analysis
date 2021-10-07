import pandas as pd

coAuthorNetworkDataSet = pd.read_csv('./MinedDataset/coAuthorNetworkDataSetWithMoreInfo.csv')

coAuthorNetworkDataSetWithoutLonerNode = coAuthorNetworkDataSet[coAuthorNetworkDataSet['CoAuthors']!="[]"]
lonerNodeCount = len(coAuthorNetworkDataSet) - len(coAuthorNetworkDataSetWithoutLonerNode)
totalNodeInCoAUthorNetwork = len(coAuthorNetworkDataSetWithoutLonerNode)
print("Number of authors in the network: {}".format(totalNodeInCoAUthorNetwork))
print("Number of authors not in the network: {}".format(lonerNodeCount))

coAuthorNetworkDataSetWithoutLonerNode['Number of CoAuthors'] = coAuthorNetworkDataSetWithoutLonerNode['CoAuthors'].apply(lambda x: len(eval(x)))
totalNumberofEdge = coAuthorNetworkDataSetWithoutLonerNode['Number of CoAuthors'].sum()
print("Number of edges in the network: {}".format(totalNumberofEdge/2))

coAuthorNetworkDataSetWithoutLonerNode.to_csv('./MinedDataset/coAuthorNetworkDataSetWithoutLonerNode.csv')


