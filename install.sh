#!/bin/sh
#git pull origin Part2_DVFS
make clean
make
make config-alpha
make sim-outorder
#./sim-outorder ./benchmarks/anagram.alpha -fetch:ifqsize 1 -commit:width 1 -decoder:width 1 -issue:width 1
#./sim-outorder ./benchmarks/anagram.alpha -fetch:ifqsize 1 -commit:width 1 -decoder:width 1 -issue:width 1 -DVFSTargetPower 53.865 -DVFSInterval 100
./sim-outorder ./benchmarks/anagram.alpha -DVFSTargetPower 53.865 -DVFSInterval 100
