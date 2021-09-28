import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')
selectedColumnsforbetweenness = ["Country", "betweenness"]
selectedColumnsfortotalpublication = ["Country", "Total Publications on Coronavirus"]


df['Country'].replace('United States', 'United States of America', inplace=True)

df = df[(df['betweenness']>=0.1)] #Ignore all rows with betweenness centrality less than one

color_dict = dict({'United States of America':'brown',
                'Italy':'green',
                'China': 'orange',
                'United Kingdom': 'red',
                'France': 'dodgerblue',
                'Germany': 'DarkOrchid',
                'Canada': 'DarkRed',
                'Switzerland': 'DarkTurquoise',
                'Spain': 'Crimson',
                'Netherlands': 'yellow',
                'Other': 'grey'})

selectedColumnsViolinPlot = ['Country', 'betweenness', 'Total Publications on Coronavirus']
violinPlotData = df[selectedColumnsViolinPlot]
violinPlotData['Percentile_Rank'] = violinPlotData['Total Publications on Coronavirus'].rank(pct = True)

countryset = ['United States of America', 'Italy', 'China', 'United Kingdom', 'France', 'Germany', 'Canada', 'Switzerland']
violinPlotData = violinPlotData[(violinPlotData['Country'].isin(countryset))]
violinPlotData.to_csv('./MinedDataset/violinPlotData.csv')
fig, ax = plt.subplots(1, figsize=(25,16))
sns.violinplot(x="Country", y="Percentile_Rank", ax=ax, data=violinPlotData, palette=color_dict, hue_order=countryset)
plt.show()