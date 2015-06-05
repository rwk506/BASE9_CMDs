from pylab import *
from numpy import *
from scipy import *
from matplotlib import *
import plotCMDs_2models
rcdefaults()
matplotlib.rc('font',family='Bitstream Vera Serif')


####### example

## load in photometry from BASE-9 formatted file
F275W,F336W,F438W,F606W,F814W = loadtxt('Cluster.cleaned.phot',skiprows=1,usecols=(1,2,3,4,5),unpack=True)
f275w,f336w,f438w,f606w,f814w = loadtxt('Cluster.sample.phot',skiprows=1, usecols=(1,2,3,4,5),unpack=True)

## load in models from BASE-9 makeCMD formatted file
model1=loadtxt('Cluster.A.ms',skiprows=1,usecols=(18,19,20,14,17))
model2=loadtxt('Cluster.B.ms',skiprows=1,usecols=(18,19,20,14,17))


plotCMDs_2models.plot_cmds2(F275W,F336W,F438W,F606W,F814W,model1,model2,selectphot=[f275w,f336w,f438w,f606w,f814w])
savefig('outputCMD.png',dpi=150)

plt.show()


