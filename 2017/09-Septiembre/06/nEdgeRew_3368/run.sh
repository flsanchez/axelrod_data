#!/bin/bash

nEdgeRew=1684
m=110
prom=20

$HOME/tesis/axelrod/bin/./axelrod.e $nEdgeRew $m $prom
python Smax_vs_q.py
#python analisis_l_C.py
#python plot_l_c.py

