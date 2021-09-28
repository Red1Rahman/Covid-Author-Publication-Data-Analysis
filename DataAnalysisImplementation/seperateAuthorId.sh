#!/bin/bash

cut -d "," -f 1 ./OriginalDataset/CovidAuthorsData.csv | grep -oE "/[0-9]+" | tr -d // | tr '\n' ','