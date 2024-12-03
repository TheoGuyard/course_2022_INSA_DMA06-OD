#!/bin/bash
array=( ch150.tsp d198.tsp eil101.tsp gr202.tsp kroA200.tsp lin105.tsp pr152.tsp rat99.tsp u159.tsp si175.tsp )
for i in "${array[@]}"
do
	python main.py $i ct
    echo ""
done