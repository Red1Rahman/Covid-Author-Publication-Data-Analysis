import pandas as pd

df = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')
selectedColumns = ["Author ID", "Full Name", "Country", "betweenness"]
betweennessRanking = df[selectedColumns].sort_values(['betweenness'], ascending=False).reset_index()
betweennessRanking.to_csv('./MinedDataset/betweennessRanking.csv', index=True)
betweennessRanking.head(20).to_csv('top20.csv', index=True)
