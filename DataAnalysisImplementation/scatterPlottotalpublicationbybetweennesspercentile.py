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
countryset = ['United States of America', 'Italy', 'China', 'United Kingdom', 'France', 'Germany', 'Canada', 'Switzerland']

selectedColumnsScatterPlot = ['Country', 'betweenness', 'Total Publications on Coronavirus']
scatterplotData = df[selectedColumnsScatterPlot]
scatterplotData.loc[~scatterplotData['Country'].isin(countryset), 'Country'] = 'Other'

scatterplotData['Percentile_Rank'] = scatterplotData.betweenness.rank(pct = True)
scatterplotData = scatterplotData.sort_values(['Percentile_Rank'], ascending=False).reset_index()
scatterplotData.to_csv('./MinedDataset/scatterplotdata.csv')

sns.scatterplot(x="Total Publications on Coronavirus", y="Percentile_Rank",
hue_order=countryset, hue="Country", data=scatterplotData, palette=color_dict, legend='full')
plt.show()