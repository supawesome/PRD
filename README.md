# Pseudo Random distribution

The aim of this repository is to show the concept of **Pseudo Random distribution** and highlight its distinction from true randomness.  
  
What is **Pseudo Random distribution**?
> Pseudo Random distribution is a statistical mechanism that affects the functionality of certain probability-based items and abilities (in games like Warcraft 3 or Dota 2). The PRD increases the probability of an event occurring each time it fails to occur, but compensates by starting with a lower probability. As a result, the effects are more consistent.  
\
The formula for calculating the probability of an effect occurring on the N-th trial after the last successful occurrence is $P(N) = C * N$. Each time the effect could occur but doesn't, the PRD raises the probability of it happening on the next attempt by a constant $C$. This constant, which is also the initial probability, is lower than the listed probability of the effect it represents. Once the effect takes place, the counter is reset.
  
    
### Repository content

- `prd.py` is a Puthon module which implements functions for generating (including calculation of constant $C$ from given probability) and analyzing pseudo-random distributions.
  
- `PRD-Analysis.ipynb` is a Jupyter notebook that explains the concept of Pseudo Random distribution and highlights its distinction from true randomness. The notebook includes an introduction to Pseudo Random distribution, a comparison between samples from Bernoulli distribution and Pseudo Random distributions, and an analysis of the resulting samples. The notebook also includes a histogram of both samples and a demonstration of the computation of the $C$ constants.  
The notebook uses the functions provided in `prd.py` to generate the samples and sequences used in the analysis.

### Table with calculated $C$ constants
Where `P` is a theoretical probability, `C` is calculated constant for this `P`, `Experimental P` is experimantal probability obtained from `100000` simulations of PRD and `Percent change of P` is a percent change of probability after simulations.
| P    | C        | Experimental P | Percent change of P |
|------|----------|----------------|---------------------|
| 0.01 | 0.000156 | 0.010002       | 0.018033 %          |
| 0.02 | 0.000620 | 0.020009       | 0.046782 %          |
| 0.03 | 0.001386 | 0.030042       | 0.140848 %          |
| 0.04 | 0.002449 | 0.039986       | -0.035068 %         |
| 0.05 | 0.003802 | 0.050029       | 0.057833 %          |
| 0.06 | 0.005440 | 0.060057       | 0.095050 %          |
| 0.07 | 0.007359 | 0.070100       | 0.143526 %          |
| 0.08 | 0.009552 | 0.079949       | -0.063400 %         |
| 0.09 | 0.012016 | 0.089991       | -0.010159 %         |
| 0.10 | 0.014746 | 0.099919       | -0.080934 %         |
| 0.11 | 0.017736 | 0.109942       | -0.052672 %         |
| 0.12 | 0.020983 | 0.119726       | -0.228278 %         |
| 0.13 | 0.024482 | 0.130056       | 0.043149 %          |
| 0.14 | 0.028230 | 0.139757       | -0.173618 %         |
| 0.15 | 0.032221 | 0.150202       | 0.134832 %          |
| 0.16 | 0.036452 | 0.159994       | -0.004000 %         |
| 0.17 | 0.040920 | 0.170015       | 0.008551 %          |
| 0.18 | 0.045620 | 0.179801       | -0.110657 %         |
| 0.19 | 0.050549 | 0.190459       | 0.241462 %          |
| 0.20 | 0.055704 | 0.200087       | 0.043619 %          |
| 0.21 | 0.061081 | 0.209809       | -0.091167 %         |
| 0.22 | 0.066676 | 0.220133       | 0.060416 %          |
| 0.23 | 0.072488 | 0.229697       | -0.131706 %         |
| 0.24 | 0.078511 | 0.239718       | -0.117302 %         |
| 0.25 | 0.084744 | 0.249941       | -0.023494 %         |
| 0.26 | 0.091183 | 0.259523       | -0.183642 %         |
| 0.27 | 0.097826 | 0.269991       | -0.003410 %         |
| 0.28 | 0.104670 | 0.280054       | 0.019284 %          |
| 0.29 | 0.111712 | 0.289533       | -0.161100 %         |
| 0.30 | 0.118949 | 0.300399       | 0.132876 %          |
| 0.31 | 0.126379 | 0.309768       | -0.074764 %         |
| 0.32 | 0.134001 | 0.320276       | 0.086154 %          |
| 0.33 | 0.141805 | 0.330466       | 0.141209 %          |
| 0.34 | 0.149810 | 0.339714       | -0.084029 %         |
| 0.35 | 0.157983 | 0.349404       | -0.170409 %         |
| 0.36 | 0.166329 | 0.360940       | 0.261241 %          |
| 0.37 | 0.174909 | 0.369308       | -0.187139 %         |
| 0.38 | 0.183625 | 0.379834       | -0.043721 %         |
| 0.39 | 0.192486 | 0.390003       | 0.000880 %          |
| 0.40 | 0.201547 | 0.400134       | 0.033611 %          |
| 0.41 | 0.210920 | 0.410268       | 0.065413 %          |
| 0.42 | 0.220365 | 0.420242       | 0.057673 %          |
| 0.43 | 0.229899 | 0.429210       | -0.183642 %         |
| 0.44 | 0.239540 | 0.439061       | -0.213503 %         |
| 0.45 | 0.249307 | 0.450152       | 0.033861 %          |
| 0.46 | 0.259872 | 0.460054       | 0.011641 %          |
| 0.47 | 0.270453 | 0.469914       | -0.018347 %         |
| 0.48 | 0.281008 | 0.480134       | 0.028008 %          |
| 0.49 | 0.291552 | 0.490316       | 0.064542 %          |
| 0.50 | 0.302103 | 0.500556       | 0.111123 %          |
| 0.51 | 0.312677 | 0.509635       | -0.071639 %         |
| 0.52 | 0.323291 | 0.519610       | -0.074984 %         |
| 0.53 | 0.334120 | 0.529973       | -0.005170 %         |
| 0.54 | 0.347370 | 0.540298       | 0.055210 %          |
| 0.55 | 0.360398 | 0.549738       | -0.047727 %         |
| 0.56 | 0.373217 | 0.559553       | -0.079776 %         |
| 0.57 | 0.385840 | 0.569814       | -0.032709 %         |
| 0.58 | 0.398278 | 0.579163       | -0.144331 %         |
| 0.59 | 0.410545 | 0.587779       | -0.376457 %         |
| 0.60 | 0.422650 | 0.600886       | 0.147618 %          |
| 0.61 | 0.434604 | 0.609321       | -0.111246 %         |
| 0.62 | 0.446419 | 0.621238       | 0.199618 %          |
| 0.63 | 0.458104 | 0.630469       | 0.074495 %          |
| 0.64 | 0.469670 | 0.640160       | 0.024966 %          |
| 0.65 | 0.481125 | 0.649414       | -0.090169 %         |
| 0.66 | 0.492481 | 0.661109       | 0.168022 %          |
| 0.67 | 0.507463 | 0.670763       | 0.113849 %          |
| 0.68 | 0.529412 | 0.681129       | 0.166075 %          |
| 0.69 | 0.550725 | 0.689555       | -0.064448 %         |
| 0.70 | 0.571429 | 0.698841       | -0.165526 %         |
| 0.71 | 0.591549 | 0.709129       | -0.122629 %         |
| 0.72 | 0.611111 | 0.720181       | 0.025126 %          |
| 0.73 | 0.630137 | 0.730055       | 0.007521 %          |
| 0.74 | 0.648649 | 0.740949       | 0.128284 %          |
| 0.75 | 0.666667 | 0.748425       | -0.210058 %         |
| 0.76 | 0.684211 | 0.760213       | 0.028088 %          |
| 0.77 | 0.701299 | 0.769811       | -0.024534 %         |
| 0.78 | 0.717949 | 0.780153       | 0.019604 %          |
| 0.79 | 0.734177 | 0.789883       | -0.014788 %         |
| 0.80 | 0.750000 | 0.800493       | 0.061638 %          |
| 0.81 | 0.765432 | 0.810340       | 0.041968 %          |
| 0.82 | 0.780488 | 0.819142       | -0.104670 %         |
| 0.83 | 0.795181 | 0.830117       | 0.014052 %          |
| 0.84 | 0.809524 | 0.840364       | 0.043379 %          |
| 0.85 | 0.823529 | 0.850818       | 0.096192 %          |
| 0.86 | 0.837209 | 0.858605       | -0.162216 %         |
| 0.87 | 0.850575 | 0.870618       | 0.070980 %          |
| 0.88 | 0.863636 | 0.879871       | -0.014638 %         |
| 0.89 | 0.876404 | 0.890758       | 0.085112 %          |
| 0.90 | 0.888889 | 0.899936       | -0.007099 %         |
| 0.91 | 0.901099 | 0.911270       | 0.139524 %          |
| 0.92 | 0.913043 | 0.918974       | -0.111516 %         |
| 0.93 | 0.924731 | 0.930051       | 0.005470 %          |
| 0.94 | 0.936170 | 0.940247       | 0.026307 %          |
| 0.95 | 0.947368 | 0.949857       | -0.015048 %         |
| 0.96 | 0.958333 | 0.959076       | -0.096227 %         |
| 0.97 | 0.969072 | 0.969866       | -0.013788 %         |
| 0.98 | 0.979592 | 0.980075       | 0.007661 %          |
| 0.99 | 0.989899 | 0.989727       | -0.027612 %         |