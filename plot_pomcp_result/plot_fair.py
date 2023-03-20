import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pylab import figure
from pylab import rcParams
import glob
import os
from pathlib import Path
import configparser
import binascii
import scipy.stats
from utils import parse_cv_ggf, parse_cv, parse_ggf

# params = { 
#     'axes.labelsize': 20, 
#     'font.size': 20, 
#     'legend.fontsize': 20, 
#     'xtick.labelsize': 15, 
#     'ytick.labelsize': 15, 
#     'text.usetex': True,
#     'text.latex.unicode' : True,
#     'figure.figsize': [20, 8]
# }
params = { 
    'axes.labelsize': 30, 
    'font.size': 20, 
    'legend.fontsize': 20, 
    'xtick.labelsize': 25, 
    'ytick.labelsize': 25, 
    'text.usetex': True,
    'text.latex.unicode' : True,
    'figure.figsize': [20, 8]
}
FS=(4.9, 4.4)
rcParams.update(params)

parse_cv_ggf("/home/gbyu/pomcp_exp/log/fairness/mwa/cluster_exp/mwa-5_ggf_log.txt")
fair_cv_mean, fair_cv_std = parse_cv("/home/gbyu/pomcp_exp/plot_pomcp_result/data/cv.txt")
fair_ggfscore_mean, fair_ggfscore_std = parse_ggf("/home/gbyu/pomcp_exp/plot_pomcp_result/data/ggf.txt")

parse_cv_ggf("/home/gbyu/pomcp_exp/log/fairness/mwa/cluster_exp/mwa-5_ggf_without_past_log.txt")
fair_wopast_cv_mean, fair_wopast_cv_std = parse_cv("/home/gbyu/pomcp_exp/plot_pomcp_result/data/cv.txt")
fair_wopast_ggfscore_mean, fair_wopast_ggfscore_std = parse_ggf("/home/gbyu/pomcp_exp/plot_pomcp_result/data/ggf.txt")

parse_cv_ggf("/home/gbyu/pomcp_exp/log/fairness/mwa/cluster_exp/mwa-5_ws_log.txt")
ws_cv_mean, ws_cv_std = parse_cv("/home/gbyu/pomcp_exp/plot_pomcp_result/data/cv.txt")
ws_ggfscore_mean, ws_ggfscore_std = parse_ggf("/home/gbyu/pomcp_exp/plot_pomcp_result/data/ggf.txt")

parse_cv_ggf("/home/gbyu/pomcp_exp/log/fairness/mwa/cluster_exp/mwa-5_ws_without_past_log.txt")
ws_wopast_cv_mean, ws_wopast_cv_std = parse_cv("/home/gbyu/pomcp_exp/plot_pomcp_result/data/cv.txt")
ws_wopast_ggfscore_mean, ws_wopast_ggfscore_std = parse_ggf("/home/gbyu/pomcp_exp/plot_pomcp_result/data/ggf.txt")

print("-- Data Extraction Finished! --")

num_simulations = [(1 << i) for i in range(25)]

fig = figure()

ax1 = fig.add_subplot(121)
ax1.errorbar(num_simulations[:len(fair_cv_mean)], fair_cv_mean, yerr=fair_cv_std, marker='s', capsize=3, label="GGF-POMCP")
ax1.errorbar(num_simulations[:len(fair_cv_mean)], fair_wopast_cv_mean, yerr=fair_wopast_cv_std, marker='o', capsize=3, label="GGF-POMCP w/o past")
ax1.errorbar(num_simulations[:len(ws_cv_mean)], ws_cv_mean, yerr=ws_cv_std, marker='^', capsize=3, label="WS-POMCP")
ax1.errorbar(num_simulations[:len(ws_cv_mean)], ws_wopast_cv_mean, yerr=ws_wopast_cv_std, marker='*', capsize=3, label="WS-POMCP w/o past")

ax1.set_xlabel("Simulations")
ax1.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax1.set_xscale('log')
ax1.set_ylabel("CV of undiscounted return")
# ax1.set_ylim(0.0, 0.5)
ax1.legend()
ax1.set_title("CV")

ax2 = fig.add_subplot(122)
ax2.errorbar(num_simulations[:len(fair_cv_mean)], fair_ggfscore_mean, yerr=fair_ggfscore_std, marker='s', capsize=3, label="GGF-POMCP")
ax2.errorbar(num_simulations[:len(fair_cv_mean)], fair_wopast_ggfscore_mean, yerr=fair_wopast_ggfscore_std, marker='o', capsize=3, label="GGF-POMCP w/o past")
ax2.errorbar(num_simulations[:len(ws_cv_mean)], ws_ggfscore_mean, yerr=ws_ggfscore_std, marker='^', capsize=3, label="WS-POMCP")
ax2.errorbar(num_simulations[:len(ws_cv_mean)], ws_wopast_ggfscore_mean, yerr=ws_wopast_ggfscore_std, marker='*', capsize=3, label="WS-POMCP w/o past")

ax2.set_xlabel("Simulations")
ax2.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax2.set_xscale('log')
ax2.set_ylabel("GGF score of undiscounted return")
ax2.legend()
ax2.set_title("GGF score")

plt.tight_layout()
plt.savefig("/home/gbyu/pomcp_exp/plot_pomcp_result/figs/mwa5_cv_ggf.png")
