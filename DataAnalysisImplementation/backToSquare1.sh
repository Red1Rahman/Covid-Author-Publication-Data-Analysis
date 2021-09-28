#!/bin/bash

rm -f CalculatedCentralityScore.csv
rm -f CovidAuthorsData.csv
rm -f lattitude-longitude_of_countries.csv

mkdir -p OriginalDataset
mkdir -p MinedDataset
cp ../OriginalDataset/lattitude-longitude_of_countries.csv ./OriginalDataset/lattitude-longitude_of_countries.csv
cp ../OriginalDataset/CovidAuthorsData.csv ./OriginalDataset/CovidAuthorsData.csv
cp ../OriginalDataset/CalculatedCentralityScore.csv ./OriginalDataset/CalculatedCentralityScore.csv

