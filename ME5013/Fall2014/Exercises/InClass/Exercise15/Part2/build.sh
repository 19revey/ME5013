#!/usr/bin/env bash

module() { eval `/share/apps//Modules/$MODULE_VERSION/bin/modulecmd bash $*`; }

PYTHONPATH=/share/apps/python/2.7.3

BASENAME=quad

swig -python $BASENAME.i

if [ "$1" == "intel" ]; then
    module load intel/13/64bit
    echo "Building with Intel Compiler"
    icc -fPIC -O3 -c $BASENAME*.c -I$PYTHONPATH/include/python2.7 -I/$PYTHONPATH/lib/python2.7/site-packages/numpy/core/include
    icc -shared $BASENAME*.o -o _$BASENAME.so
else
    gcc -fPIC -O3 -c $BASENAME*.c -I$PYTHONPATH/include/python2.7 -I/$PYTHONPATH/lib/python2.7/site-packages/numpy/core/include
    gcc -shared $BASENAME*.o -o _$BASENAME.so
fi


rm -f $BASENAME*.o
