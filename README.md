Taylor_diagram
==============

Taylor diagram in python based on Taylor (2001).


![ScreenShot](https://github.com/mabelcalim/Taylor_diagram/blob/master/example.png)

Installation
============

First: git clone git@github.com:mabelcalim/Taylor_diagram.git

Then ...

A local install can be done using the provided setup.py file:

    python setup.py install

The installation path can be changed using the **--prefix** switch, e.g.:

    python setup.py install --prefix $HOME/inst

Make sure to add the corresponding paths to your ``$PATH`` and ``$PYTHONPATH``
environment variables. Alternatively, if the **--user** switch can be used:

    export PYTHONUSERBASE=$HOME/inst/pip_installs
    export PYTHONPATH=$HOME/inst/pip_installs/lib/python2.7/\
        site-packages/:$PYTHONPATH
    export PATH=$HOME/inst/pip_installs/bin:$PATH
    python setup.py install --user

If you plan on modifying the code, use the **develop** target in combination
with the **--user** swich:

    export PYTHONUSERBASE=$HOME/inst/pip_installs
    export PYTHONPATH=$HOME/inst/pip_installs/lib/python2.7/\
        site-packages/:$PYTHONPATH
    export PATH=$HOME/inst/pip_installs/bin:$PATH
    python setup.py develop --user

The first three lines should also be included in the **$HOME/.bashrc** file.

Cookbook
=========

0) open a terminal:
	
	python 
or
	iptyhon

	In [1]: import taylor_diag
	
1) open netcdf data (file = archive.nc and var = variable from archive.nc):
	In [2]: data = taylor_diag.load_nc(file,'var')

2) create a dict of series:
	In [3]: series ={}
	In [4]: series[0] = data1 
	In [5]: series[1] = data2
	
note::
	series[0] is the reference data by default

3) create a Taylor diagram
	In [6]:taylor_diag.Taylor_diag(series)


Support Group
=============

Any doubt ... talk to me :
	https://groups.google.com/forum/?hl=en#!forum/taylor-diag-users-support


