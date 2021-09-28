import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import pycountry
from mpl_toolkits.axes_grid1 import make_axes_locatable


df = pd.read_csv('./MinedDataset/datasetForCovidAuthorConnectivityGraph.csv')
selectedColumns = ["Country", "centrality"]
df = df.dropna(axis=0, subset=['centrality']) #Ignoring all rows that do not have closeness values
df = df[(df['centrality']<=0.9)]
countryPercentageRanking = df[selectedColumns].groupby("Country").mean().sort_values(['centrality'], ascending=False).reset_index()
countryCodes = []
for index, row in countryPercentageRanking.iterrows():
    try:
        code=pycountry.countries.get(name=row["Country"]).alpha_3
        countryCodes.append(code)
    except:
        if row["Country"]=="Netherlands Antilles":
            code = "NLD"
        elif row["Country"]=="Macedonia":
            code = "MKD"
        elif row["Country"]=="Russia":
            code = "RUS"
        elif row["Country"]=="Tanzania":
            code = "TZA"
        elif row["Country"]=="Democratic Republic of the Congo":
            code = "COD"
        elif row["Country"]=="Venezuela":
            code = "VEN"
        elif row["Country"]=="Vietnam":
            code = "VNM"
        elif row["Country"]=="Syria":
            code = "SYR"
        elif row["Country"]=="United States of America":
            code = "USA"
        elif row["Country"]=="South Korea":
            code = "KOR"
        elif row["Country"]=="Taiwan":
            code = "TWN"
        elif row["Country"]=="Iran":
            code = "IRN"
        elif row["Country"]=="Bolivia":
            code = "BOL"
        elif row["Country"]=="Laos":
            code = "LAO"
        elif row["Country"]=="Brunei":
            code = "BRN"
        elif row["Country"]=="Moldova":
            code = "MDA"
        else:
            code="None"

        countryCodes.append(code)


countryPercentageRanking["iso_a3"] = countryCodes

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world_values_full = world.merge(countryPercentageRanking, how='inner',on='iso_a3',copy=True)
world_values = world_values_full[['iso_a3', 'geometry', 'centrality']]

fig, ax = plt.subplots(1, figsize=(16,8), facecolor='lightblue')

world_values.plot(column='centrality', ax=ax, cmap='Reds', edgecolors='black')
# set an axis for the color bar
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="3%", pad=0.05)
# color bar
vmax = world_values.centrality.max()
mappable = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=0, vmax=float(vmax)))
cbar = fig.colorbar(mappable, cax=cax)
cbar.set_ticks(np.arange(0, vmax, 40))
cbar.ax.tick_params(labelsize=18)
ax.axis('off')

plt.show()

countryPercentageRanking.to_csv('./MinedDataset/countryPercentageRanking.csv', index=True)