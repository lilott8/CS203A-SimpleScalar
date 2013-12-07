#!/bin/sh
#git pull
clear
rm -f *.o
make
make config-alpha
make sim-outorder
FILES=('./benchmarks/anagram.alpha ./benchmarks/words < ./benchmarks/anagram.in' './benchmarks/go.alpha 2 8 ./benchmarks/2stone9.in')
CACHE_BSIZE=('32' '64' '128' '256')
CACHE_REPLACE=('l')
#Should be ...8 512
ASSOC=('1' '4')
#Should be 512 128....
ASSOC_SETS=('64' '1')
L1='64:32:2:l'

COMPILERS=('anagram' 'go')

I=0
X=0
Y=0

PREFETCH=('0' '1' '2' '4')
BUFFERS=('0' '2' '4' '8')

#if [ ${#} -eq 3 ]
#then
#boolean
#STDOUT=$1
#0,1,2,4,8
#PREFETCH=$2
#int 0,2,4,8
#BUFFERS=$3
#else
#STDOUT=0
#PREFETCH=8
#BUFFERS=0
#fi

for var in "${FILES[@]}"
do
  X=0
  Y=0
  for pre in "${PREFETCH[@]}"
  do
    #Increment the prefetching
    P1="./sim-outorder -cache:buffer_il 0 -cache:buffer_dl 0 "
    P1="$P1 -cache:il2 dl2 -cache:dl2 ul2:${ASSOC_SETS[$I]}:32:${ASSOC[$I]}:l:$pre "
    P1="$P1 -cache:dl1 dl1:$L1 -cache:il1 il1:$L1 -redir:sim "
    P1="$P1 ./results/prefetch/${COMPILERS[$I]}-${PREFETCH[$X]}.stat $var "
    X=$((X+1))
    echo $P1
  done
  echo "=============================================="
  for buf in "${BUFFERS[@]}"
  do
    #increment the buffers
    P2="./sim-outorder -cache:buffer_il $buf -cache:buffer_dl $buf "
    P2="$P2 -cache:il2 dl2 -cache:dl2 ul2:${ASSOC_SETS[$I]}:32:${ASSOC[$I]}:l "
    P2="$P2 -cache:dl1 dl1:$L1 -cache:il1 il1:$L1 -redir:sim "
    P2="$P2 ./results/buffers/${COMPILERS[$I]}-${BUFFERS[$Y]}.stat $var "
    Y=$((Y+1))
    echo $P2
  done
  
  I=$((I+1))
done
