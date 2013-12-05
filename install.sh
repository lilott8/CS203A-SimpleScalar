#!/bin/sh
#git pull
make
make config-alpha
make sim-outorder
./sim-outorder ./benchmarks/anagram.alpha -fetch:ifqsize 1 -commit:width 4 -decoder:width 2 -issue:width 1 
