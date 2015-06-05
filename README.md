BASE9_CMDs
================================

<h3>A plotting tool to produce a grid of CMDs using the results from BASE-9</h3>

<br />

<h4>Table of Contents</h4>
[Summary](#Summary)<br />
[Downloading and Installation](#Install)<br />
[Example of Use](#Use)<br />
[Documentation](#Doc)<br />
[Dependencies](#Deps)<br />
[Other Information](#Other)<br />
<br /><br />


<a name="Summary"/>
<h4>Summary</h4>

This repository houses a Python script that allows the user to plot a grid of color-magnitude diagrams (CMDs) from the output of BASE-N mutliple population Bayesian analysis with five filters. The [BASE-9 package](https://github.com/argiopetech/BASE) uses Bayesian analysis techniques to determine a best fit isochrone to a cluster of stellar photometry from a set of selected theoretical models. More information about the BASE-9 program package itself and its scientific motivation can be found at the BASE-9 GitHub page as well as in the user manual available via [arxiv](http://adsabs.harvard.edu/abs/2014arXiv1411.3786V).

The plotting function included allows the user to plot each combination of the CMD in the five filters, resulting in a 5-by-5 grid of CMDs. In each CMD, the full set of photometry can be plot, with overplotted points to indicate the subsample used in the actual run of the Bayesian analysis software. Additionally, the results of the Bayesian software "makeCMD" functionality can be used to plot the isochrone results of the two-population Bayesian analysis fit to the data.


<br /> <br /><br />





<a name="Install"/>
<h4>Downloading and Installation</h4>

The source code and necessary data files may all be downloaded as a zip, forked, or cloned on a local machine from the [BASE-9 Plotting Results](https://github.com/rwk506/BASE9_CMDs) repository.

The primary Python script included is **plotCMDs_2models.py**. The files included are:
- **Cluster.A.ms**: The resulting isochrone fit to "population A" in a simulated globular cluster
- **Cluster.B.ms**: The resulting isochrone fit to "population B" in a simulated globular cluster
- **Cluster.cleaned.phot**: The simulated five-filter HST photometry of a globular cluster 
- **Cluster.sample.phot**: The subsampled stars of the simulated globular cluster
- **outputCMD.png**: An example of an output plot from plotCMDs\_2models.py; this is produced by the plotCMDs\_example.py code.
- **plotCMDs_2models.py**: The primary Python code which creates the functionality to plot the CMD grid
- **plotCMDs_example.py**: An example of use of the code and corresponding files/data
- **README.md**: README file.

If the user has Python and the necessary packages installed, no further installation should be required to run the code. If scripted, code may be run from outside Python with the command-line call 'python example.py' (where example is the name of the script). If inside Python, the function plot\_cmds2() may be called following importing the necessary packages and:

    import plotCMDs_2models.py

Then the plotting function, plot\_cmds2(), may be called as per the documentation and example provided.



<br /> <br /><br />

<a name="Use"/>
<h4>Example of Use</h4>

The plotCMDs\_2models.py package houses the plot\_cmds2() function, which will plot the 5 by 5 grid of CMDs with resulting isochrones from the BASE-9 makeCMD function. The function requires the input of a 5D-array of magnitudes from an imported photometry file (designed for F275W, F336W, F438W, F606W, and F814W, but this could be user-edited for any desired filters). For those unfamiliar with python, a photometry file (e.g. the included file NGC1261.single.res) may be imported with the command:

    F275W, F336W, F438W, F606W, F814W = loadtxt('Cluster.cleaned.phot',skiprows=1,usecols=(1,2,3,4,5),unpack=True)

Resulting models generated from BASE-9 sampling and the makeCMD functionality can similarly be imported by:

    model1=loadtxt('Cluster.A.ms',skiprows=1,usecols=(18,19,20,14,17))


Where the first row is skipped as a header and columns 1 through 5 are the magnitudes for filters F275W through F814W. The results can then be plotted using the defaults simply by:

    plot_cmds2(F275W,F336W,F438W,F606W,F814W,model1,model2)

Other options can be included: whether to plot a subsample of photometry (loaded into Python separately), changing line styles and colors, etc. Full documentation is given in the function description. The resulting plot can either be saved:

    savefig('OutputCMD.png')

or shown on screen:

    plt.show()


<br /> <br /><br />






<a name="Doc"/>
<h4>Documentation</h4>

#####plot_cmds2()#####

This is a function that will take a single population output results file and plot the sampling history and resulting PDFs of the following, assuming that the results file is formatted as a matrix with columns of age, metallicity, distance, extinction, and helium. 

The python code creates a grid of all possible CMDs in combinations of five filters and overlplots 2 isochrone models from the user. It is optimized for use with HST filters F275W, F336W, F438W, F606W, and F814W; input is in order of increasing wavelength. It is also optimized for models generated by the BASE-9 makeCMD routine.

Call signature: plot_cmds2(F275W, F336W, F438W, F606W, F814W)
where the inputs are 1-D arrays of magnitudes loaded from a photometry file, typically loaded in a separate line as, e.g.: res=F275W, F336W, F438W, F606W, F814W = loadtxt('Cluster.cleaned.phot',skiprows=1,usecols=(1,2,3,4,5),unpack=True).

Optional keyword arguments:<br/>
    =========   =======================================================<br/>
    Keyword     Description<br/>
    =========   =======================================================<br/>
    Inputs:
    f275:        1-D array of magnitudes
    f336:        1-D array of magnitudes
    f438:        1-D array of magnitudes
    f606:        1-D array of magnitudes
    f814:        1-D array of magnitudes
    modelA:      5-D array, each of five dimensions defining an isochrone in one of the five filters
    modelB:      same as modelA for a second model (can set modelB=modelA to plot only one population if desired)
    selectphot:  a 5-D array formatted as [sub275,subf336,subf438,subf606,subf814]; if set to not 'None', this option will overplot the subsample of photometry.
    

Additional options for plotting colors, sizes, formats, etc. can be found in pyplot.plot() and related descriptions. Colors may take any standard HTML string descriptor (re: http://www.w3schools.com/html/html_colornames.asp).







<br /> <br /><br />

<a name="Deps"/>
<h4>Dependencies</h4>

This Python code was written using Python 2.6 and Numpy 1.5.1, but should be compatible with many other versions (though not Python 3.0 or higher). The user may have to install the matplotlib and pylab packages.

Compatible with iPython Notebook (use %run [name]).




<br /> <br /><br />

<a name="Other"/>
<h4>Other Information</h4>

Author: RWK <br />
License: None, free to use and edit as people wish. Contact for questions or requests for other functionalities. <br />
Contact: May be made through GitHub. <br />


