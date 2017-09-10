#!/bin/bash

nEdgeRew=2500
m=85
prom=50

$HOME/tesis/axelrod/bin/./axelrod.e $nEdgeRew $m $prom
python Smax_vs_q.py
#python analisis_l_C.py
#python plot_l_c.py

