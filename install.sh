#!/bin/sh
git pull
make
make config-alpha
make sim-outorder
