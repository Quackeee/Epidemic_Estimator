#!/bin/bash

gnuplot plotscript.plot > /dev/null 2>&1
grep "m               =" fit.log | tail -1
grep "s               =" fit.log | tail -1