#!/usr/bin/python3

import matplotlib.pyplot as plt
from FitFunctions import FnctA, FnctB
from utilities import GenBinSeq, PlotBinFct, NormBinSeqToNum

# individual size:
IND_SIZE=8

PlotBinFct(GenBinSeq(IND_SIZE), FnctA)
PlotBinFct(GenBinSeq(IND_SIZE), FnctB, '--r')

plt.show()