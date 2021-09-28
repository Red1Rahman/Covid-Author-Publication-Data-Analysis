#!/bin/bash

./backToSquare1.sh
./seperateAuthorId.sh | python3 prepareDataset.py 
