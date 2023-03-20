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
from utils import parse_rocks, parse_returns, parse_file

# params = { 
#     'axes.labelsize': 25, 
#     'font.size': 20, 
#     'legend.fontsize': 20, 
#     'xtick.labelsize': 25, 
#     'ytick.labelsize': 25, 
#     'text.usetex': True,
#     'text.latex.unicode' : True,
#     'figure.figsize': [20, 16]
# }
params = { 
    'axes.labelsize': 30, 
    'font.size': 20, 
    'legend.fontsize': 20, 
    'xtick.labelsize': 25, 
    'ytick.labelsize': 25, 
    'text.usetex': True,
    'text.latex.unicode' : True,
    'figure.figsize': [20, 16]
}
FS=(4.9, 4.4)
rcParams.update(params)

parse_file("/home/gbyu/pomcp_exp/log/risk/pomcp_norisk.txt")
good_rocks_mean, good_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/good.txt")
bad_rocks_mean, bad_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/bad.txt")
undiscounted_return_mean, undiscounted_return_std = parse_returns("/home/gbyu/pomcp_exp/plot_pomcp_result/data/undiscounted_return.txt")
check_action_mean, check_action_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/check_action.txt")
print("-- Data Extraction Finished! --")

parse_file("/home/gbyu/pomcp_exp/log/risk/risk_log_beta_-0.05.txt")
rs1_good_rocks_mean, rs1_good_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/good.txt")
rs1_bad_rocks_mean, rs1_bad_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/bad.txt")
rs1_undiscounted_return_mean, rs1_undiscounted_return_std = parse_returns("/home/gbyu/pomcp_exp/plot_pomcp_result/data/undiscounted_return.txt")
rs1_check_action_mean, rs1_check_action_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/check_action.txt")
print("-- Data Extraction Finished! --")

parse_file("/home/gbyu/pomcp_exp/log/risk/risk_log_beta_-0.1.txt")
rs2_good_rocks_mean, rs2_good_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/good.txt")
rs2_bad_rocks_mean, rs2_bad_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/bad.txt")
rs2_undiscounted_return_mean, rs2_undiscounted_return_std = parse_returns("/home/gbyu/pomcp_exp/plot_pomcp_result/data/undiscounted_return.txt")
rs2_check_action_mean, rs2_check_action_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/check_action.txt")
print("-- Data Extraction Finished! --")

parse_file("/home/gbyu/pomcp_exp/log/risk/risk_log_beta_-0.2.txt")
rs3_good_rocks_mean, rs3_good_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/good.txt")
rs3_bad_rocks_mean, rs3_bad_rocks_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/bad.txt")
rs3_undiscounted_return_mean, rs3_undiscounted_return_std = parse_returns("/home/gbyu/pomcp_exp/plot_pomcp_result/data/undiscounted_return.txt")
rs3_check_action_mean, rs3_check_action_std = parse_rocks("/home/gbyu/pomcp_exp/plot_pomcp_result/data/check_action.txt")
print("-- Data Extraction Finished! --")

num_simulations = [(1 << i) for i in range(25)]

fig = figure()

ax1 = fig.add_subplot(221)
ax1.errorbar(num_simulations[:len(good_rocks_mean)], good_rocks_mean, yerr=good_rocks_std, marker='s', capsize=3, label="POMCP")
ax1.errorbar(num_simulations[:len(rs1_good_rocks_mean)], rs1_good_rocks_mean, yerr=rs1_good_rocks_std, marker='o', capsize=3, label=r"RS-POMCP, $\beta = -0.05$")
ax1.errorbar(num_simulations[:len(rs2_good_rocks_mean)], rs2_good_rocks_mean, yerr=rs2_good_rocks_std, marker='^', capsize=3, label=r"RS-POMCP, $\beta = -0.1$")
ax1.errorbar(num_simulations[:len(rs3_good_rocks_mean)], rs3_good_rocks_mean, yerr=rs3_good_rocks_std, marker='*', capsize=3, label=r"RS-POMCP, $\beta = -0.2$")
ax1.set_xlabel("Simulations")
ax1.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax1.set_xscale('log')
ax1.set_ylabel("Number of good rocks")
ax1.legend()
ax1.set_title("Collected good rocks")

ax2 = fig.add_subplot(222)
ax2.errorbar(num_simulations[:len(bad_rocks_mean)], bad_rocks_mean, yerr=bad_rocks_std, marker='s', capsize=3, label="POMCP")
ax2.errorbar(num_simulations[:len(rs1_bad_rocks_mean)], rs1_bad_rocks_mean, yerr=rs1_bad_rocks_std, marker='o', capsize=3, label=r"RS-POMCP, $\beta = -0.05$")
ax2.errorbar(num_simulations[:len(rs2_bad_rocks_mean)], rs2_bad_rocks_mean, yerr=rs2_bad_rocks_std, marker='^', capsize=3, label=r"RS-POMCP, $\beta = -0.1$")
ax2.errorbar(num_simulations[:len(rs3_bad_rocks_mean)], rs3_bad_rocks_mean, yerr=rs3_bad_rocks_std, marker='*', capsize=3, label=r"RS-POMCP, $\beta = -0.2$")
ax2.set_xlabel("Simulations")
ax2.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax2.set_xscale('log')
ax2.set_ylabel("Number of bad rocks")
ax2.legend()
ax2.set_title("Collected bad rocks")

ax3 = fig.add_subplot(223)
ax3.errorbar(num_simulations[:len(check_action_mean)], check_action_mean, yerr=check_action_std, marker='s', capsize=3, label="POMCP")
ax3.errorbar(num_simulations[:len(rs1_check_action_mean)], rs1_check_action_mean, yerr=rs1_check_action_std, marker='o', capsize=3, label=r"RS-POMCP, $\beta = -0.05$")
ax3.errorbar(num_simulations[:len(rs2_check_action_mean)], rs2_check_action_mean, yerr=rs2_check_action_std, marker='^', capsize=3, label=r"RS-POMCP, $\beta = -0.1$")
ax3.errorbar(num_simulations[:len(rs3_check_action_mean)], rs3_check_action_mean, yerr=rs3_check_action_std, marker='*', capsize=3, label=r"RS-POMCP, $\beta = -0.2$")
ax3.set_xlabel("Simulations")
ax3.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax3.set_xscale('log')
ax3.set_ylabel("Count of action [CHECK]")
ax3.legend()
ax3.set_title("Count of action [CHECK]")

ax4 = fig.add_subplot(224)
ax4.errorbar(num_simulations[:len(undiscounted_return_mean)], undiscounted_return_mean, yerr=undiscounted_return_std, marker='s', capsize=3, label="POMCP")
ax4.errorbar(num_simulations[:len(rs1_undiscounted_return_mean)], rs1_undiscounted_return_mean, yerr=rs1_undiscounted_return_std, marker='o', capsize=3, label=r"RS-POMCP, $\beta = -0.05$")
ax4.errorbar(num_simulations[:len(rs2_undiscounted_return_mean)], rs2_undiscounted_return_mean, yerr=rs2_undiscounted_return_std, marker='^', capsize=3, label=r"RS-POMCP, $\beta = -0.1$")
ax4.errorbar(num_simulations[:len(rs3_undiscounted_return_mean)], rs3_undiscounted_return_mean, yerr=rs3_undiscounted_return_std, marker='*', capsize=3, label=r"RS-POMCP, $\beta = -0.2$")
ax4.set_xlabel("Simulations")
ax4.xaxis.set_minor_formatter(mticker.ScalarFormatter())
ax4.set_xscale('log')
ax4.set_ylabel("Averaged undiscounted return")
ax4.legend()
ax4.set_title("Undiscounted return")

plt.tight_layout()
plt.savefig("/home/gbyu/pomcp_exp/plot_pomcp_result/figs/rocksample_varied_beta.pdf")
