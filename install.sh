#!/bin/sh
#git pull
clear
rm -f *.o
make
make config-alpha
make sim-outorder
FILES=('./benchmarks/anagram.alpha words < anagram.in' './benchmarks/go.alpha 2 8 2stone9.in')
CACHE_BSIZE=('32' '64' '128' '256')
CACHE_REPLACE=('l')
#Should be ...8 512
ASSOC=('1' '4')
#Should be 512 128....
ASSOC_SETS=('64' '1')
L1='64:32:2:l'

COMPILERS=('anagram', 'go')
I=0

if [ ${#} -eq 3 ]
then
#boolean
STDOUT=$1
#boolean
PREFETCH=$2
#int 1-8
BUFFERS=$3
else
STDOUT=1
PREFETCH=0
BUFFERS=4
fi

for var in "${FILES[@]}"
do
  P1="./sim-outorder -cache:buffer_il $BUFFERS -cache:buffer_dl $BUFFERS "
  P1="$P1 -cache:il2 dl2 -cache:dl2 ul2:${ASSOC_SETS[$I]}:32:${ASSOC[$I]}:l:$PREFETCH "
  P1="$P1 -cache:dl1 dl1:$L1 -cache:il1 il1:$L1 $var "
  if [ ${STDOUT} = 1 ]
  then
    P1="$P1 > STDOUT-$COMPILERS[$I]-OUTFILE.std 2> $COMPILERS[$I].stat"
  fi
  $P1
  I=$((I+1))
done
