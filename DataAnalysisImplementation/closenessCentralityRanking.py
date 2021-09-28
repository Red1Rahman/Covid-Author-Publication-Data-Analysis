import pandas as pd

df = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')
selectedColumns = ["Author ID", "Full Name", "Country", "centrality"]
betweennessRanking = df[selectedColumns].sort_values(['centrality'], ascending=False).reset_index()
betweennessRanking.to_csv('./MinedDataset/closenessRanking.csv', index=True)
