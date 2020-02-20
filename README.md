# pyRHESSys (in progress)

The pyRHESSys is an Object-Oriented Python wrapper for the model input creation and manipulation, model execution, model output visualization and analysis of RHESSys model (The Regional Hydro-Ecologic Simulation System).

* [RHESSys Website at GitHub ](https://github.com/RHESSys)
* [RHESSys Website - Naomi Tague ](http://fiesta.bren.ucsb.edu/~rhessys/)

## The pyRHESSys is intended to provide

 - Get and set model input
 - Run RHESsys Model on local and Cloud 
 - Visualize RHESSys outputs
 - Use pyRHESSYS with jupyter notebook environment 
 - Interact Hydorshare to download RHESSys TestCases and upload the output of RHESSys 
 - Create model input using GRASS GIS (in progress)
 - Automate model calibration or sensitivity analysis (Future work)
 
## Installation and Usage

#### pyRHESSys requires Python 3.7 and following packages :

 - xarray : N-D labeled arrays and datasets in python
 - numpy : the fundamental package for scientific computing with Python
 - matplotlib : a Python 2D plotting library 
 - seaborn : statistical data visualization 
 - jupyterthemes : select and install a Jupyter notebook theme
 - hs-restclient : HydroShare REST API python client library
 - geopandas
 - shapely
 - pandas
 - distributed
 - fiona
 - hydroeval
     
## Download and Install pyRHESSys:

**1.)**  Download pyRHESSys
```python
~/Downloads$ git clone https://github.com/DavidChoi76/pyRHESSys.git
```
        
**2.)**  change directory into pyRHESSys folder same level with setup.py.
```python
~/Downloads/pyRHESSys pip install .
```

## Examples of manipulating and running pyRHESSys :

Refereed paper : RHESSys: Regional Hydro-Ecologic Simulation System—An ObjectOriented Approach to Spatially Distributed Modeling of Carbon, Water, and Nutrient Cycling (http://fiesta.bren.ucsb.edu/~rhessys/setup/downloads/files/RHESSysTagueEA2004.pdf.

**(Test Case)** [RHESSys input data at Coweeta subbasin18 test](https://www.hydroshare.org/resource/6e34c42af35a4f51b1642de70ed6af95/) 

**(Jupyter Notebook)** [RHESSys Jupyter Notebook at Coweeta subbasin18](https://www.hydroshare.org/resource/9c2c5df86f1a48c0a57c1d142b4dc9a4/)
         
## Bugs
  Our issue tracker is at https://github.com/DavidChoi76/pyRHESSys/issues.
  Please report any bugs that you find.  Or, even better, fork the repository on
  GitHub and create a pull request.  All changes are welcome, big or small, and we
  will help you make the pull request if you are new to git
  (just ask on the issue).

## License
  Distributed with a MIT license; see LICENSE.txt::

  Copyright (C) 2020 pyRHESSys Developers
  YoungDon Choi <yc5ef@virginia.edu>
 
