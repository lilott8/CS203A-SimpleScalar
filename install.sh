#!/bin/sh
#git pull origin Part2_DVFS
make clean
make
make config-alpha
make sim-outorder
#./sim-outorder ./benchmarks/anagram.alpha -fetch:ifqsize 1 -commit:width 1 -decoder:width 1 -issue:width 1
#./sim-outorder ./benchmarks/anagram.alpha -fetch:ifqsize 1 -commit:width 1 -decoder:width 1 -issue:width 1 -DVFSTargetPower 53.865 -DVFSInterval 100
./sim-outorder -DVFSTargetPower 19.8835 -DVFSInterval 1000 ./benchmarks/anagram.alpha < ./benchmarks/anagram.in

#./sim-outorder -DVFSTargetPower 60.8711 -DVFSInterval 1000 ./benchmarks/go.alpha 2 8 2stone9.in
