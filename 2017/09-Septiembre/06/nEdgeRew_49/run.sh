#!/bin/bash

nEdgeRew=49
m=8
prom=50

$HOME/tesis/axelrod/bin/./axelrod.e $nEdgeRew $m $prom
python Smax_vs_q.py
python analisis_l_C.py
python plot_l_c.py
