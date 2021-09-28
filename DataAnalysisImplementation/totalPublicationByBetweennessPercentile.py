import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import pycountry
from mpl_toolkits.axes_grid1 import make_axes_locatable
# https://www.kaggle.com/paultimothymooney/latitude-and-longitude-for-every-country-and-state

def getUnmatchedCountryCodes(countryName):
    if countryName=="Netherlands Antilles":
            return ["NLD", "AN"]
    elif countryName=="Macedonia":
        return ["MKD", "MK"]
    elif countryName=="Russia":
        return ["RUS", "RU"]
    elif countryName=="Tanzania":
        return ["TZA", "TZ"]
    elif countryName=="Democratic Republic of the Congo":
        return ["COD", "CD"]
    elif countryName=="Venezuela":
        return ["VEN", "VE"]
    elif countryName=="Vietnam":
        return ["VNM", "VN"]
    elif countryName=="Syria":
        return ["SYR", "SY"]
    elif countryName=="United States of America":
        return ["USA", "US"]
    elif countryName=="South Korea":
        return ["KOR", "KR"]
    elif countryName=="Taiwan":
        return ["TWN", "TW"]
    elif countryName=="Iran":
        return ["IRN", "IR"]
    elif countryName=="Bolivia":
        return ["BOL", "BO"]
    elif countryName=="Laos":
        return ["LAO", "LA"]
    elif countryName=="Brunei":
        return ["BRN", "None"]
    elif countryName=="Moldova":
        return ["MDA", "MD"]
    else:
        return ["None", "None"]

df = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')
selectedColumnsforbetweenness = ["Country", "betweenness"]
selectedColumnsfortotalpublication = ["Country", "Total Publications on Coronavirus"]


df['Country'].replace('United States', 'United States of America', inplace=True)

df = df[(df['betweenness']>=0.1)] #Ignore all rows with betweenness centrality less than one
sumOfbetweennessScore = float(df['betweenness'].sum())
countrybetweennessSum = pd.DataFrame({'betweennessSum' : df[selectedColumnsforbetweenness].groupby("Country")['betweenness'].sum() }).sort_values(['betweennessSum'], ascending=False).reset_index()
countrybetweennessSum['Percentile_Rank'] = countrybetweennessSum.betweennessSum.rank(pct = True)
countryTotalPublication = pd.DataFrame({'Total_Publication_in_Country' :df[selectedColumnsfortotalpublication].groupby("Country")['Total Publications on Coronavirus'].sum() })
countryPercentileRanking = countrybetweennessSum.merge(countryTotalPublication, how='inner',on='Country',copy=True)

alpha3countryCodes, alpha2countryCodes, betweennessPercentileList = [], [], []
for index, row in countryPercentileRanking.iterrows():
    countryName = row["Country"]
    betweennessPercentileList.append(row["betweennessSum"] * 100 / sumOfbetweennessScore)
    try:
        alpha3code=pycountry.countries.get(name=countryName).alpha_3
        alpha2code=pycountry.countries.get(name=countryName).alpha_2
        alpha3countryCodes.append(alpha3code)
        alpha2countryCodes.append(alpha2code)
    except:
        alpha3code, alpha2code = getUnmatchedCountryCodes(countryName)
        alpha3countryCodes.append(alpha3code)
        alpha2countryCodes.append(alpha2code)


countryPercentileRanking["iso_a3"] = alpha3countryCodes
countryPercentileRanking["country_code"] = alpha2countryCodes
countryPercentileRanking['betweennessPercentile'] = betweennessPercentileList

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
latitudelongitudeDataset = pd.read_csv('./OriginalDataset/lattitude-longitude_of_countries.csv')
world_values_full = world.merge(countryPercentileRanking, how='inner',on='iso_a3',copy=True)
world_values_full_with_coordinate = world_values_full.merge(latitudelongitudeDataset, how='inner',on='country_code',copy=True).sort_values(['Percentile_Rank'], ascending=False).reset_index()
selectedWorldDataColumns = ['Country', 'betweennessPercentile', 'Total_Publication_in_Country', 'Percentile_Rank', 'geometry', 'latitude', 'longitude']
world_values = world_values_full_with_coordinate[selectedWorldDataColumns]
world_values.to_csv('./MinedDataset/world_values.csv')

fig, ax = plt.subplots(1, figsize=(25,16), facecolor='lightblue')

world_values.dropna().plot(column='Percentile_Rank', ax=ax, cmap='Reds', edgecolors='black', label='Country')
# set an axis for the color bar
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.05)
# color bar
vmax = 1.0
mappable = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=0, vmax=1.0))
cbar = fig.colorbar(mappable, cax=cax)
cbar.set_ticks([0.0,0.2,0.4,0.6,0.8,1.0])
cbar.ax.tick_params(labelsize=18)
ax.axis('off')

for i in range(0,7):
    ax.text(float(world_values.longitude[i]),
    float(world_values.latitude[i]),
    '{}'.format(world_values.Country[i]),fontsize=5, color='White')

ax.set_title('Betweenness Centrality Percentile by Country')
plt.show()

countryPercentileRanking.to_csv('./MinedDataset/countryPercentileRanking.csv', index=True)