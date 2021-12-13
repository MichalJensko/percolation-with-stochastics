# percolation-with-stochastics

Simple project aiming to evaluate how probability of percolation (geting from the "top" of the matrix to the "bottom" by jumping from cell to cell, 
diagonal movement not allowed) is affected by changes to probability of individual cell opening.

### Instruction/workflow:
1. Run percolation_main.py file
2. Series of txt files, each containging raw data ina form of number of sucesses for specyffic p, will be created in separate directory 
3. From the data generated in 2. programm will created series of plots in another directory (in directory with the programm itself). 

### Interpretation of plots

First 5 plots - each will present how probability of sucess changed witch change of p (which is a probability of individual cell opening) caluculated as average from 1000 matrices.
6th plot presents changes in chance of sucess calculated from a function. 7th Plot compares both methods and 8th presents average from first 5 plots. 
