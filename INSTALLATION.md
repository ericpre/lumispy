## Installation

### 1) Creating a conda environment

LumiSpy requires Python 3 and conda -- we suggest using the Python 3 version 
of [Miniconda](https://conda.io/miniconda.html).

We recommend creating a new environment for the lumispy package (or installing 
it in the hyperspy environment, if you have one already). To create a new 
environment:

1. Load the anaconda prompt.
2. Run the following command:

```
    $ conda create -n lumispy
```

### 2) Installing the package in the new environment

Now that you have created a new environment, install the package:

1. Download the [source code](https://github.com/lumispy/lumispy) and put it 
in a directory on your computer (by default, GitHub saves it in 
`Username\Documents\GitHub\lumispy`).
2. Load the anaconda prompt.
3. Change current working directory to the folder where you downloaded the 
source code.
4. Activate the lumispy environment.
5. Install the package running:

```
    $ cd PATH_TO_SOURCE_CODE
    $ conda activate lumispy
    $ pip install .
```

Installation is completed! To start using it, check the next section.

#### OPTIONAL: Working with eV instead of wavelength units

In order to convert your signal luminescence axes (normally in wavelength in nanometers) to energy units, you will need to reinstall the `hyperspy` package to its developing branch `non-uniform-axes`. **If you skip this, all lumispy function will work, except the energy conversion functions.**

To do that, follow these steps:

1. Download the [development hyperspy source code](https://github.com/hyperspy/hyperspy/tree/non_uniform_axes) and put it 
in a directory on your computer (by default, GitHub saves it in 
`Username\Documents\GitHub\hyperspy`).
2. Load the anaconda prompt.
3. Change current working directory to the folder where you downloaded the 
source code (using `cd path`).
4. Activate the lumispy environment using `conda activate lumispy`).
5. Reinstall the hyperspy package running:

```
    $ cd PATH_TO_HYPERSPY_DEV_SOURCE_CODE
    $ conda activate lumispy
    $ pip install -e ./
```

Now you are ready to use all the functionalites of lumispy.

### 3) Getting Started

To get started using LumiSpy, especially if you are unfamiliar with Python, we 
recommend using [Jupyter notebooks](https://jupyter.org/). Having installed 
lumispy as above, a Jupyter notebook can be opened using the following commands 
entered into an anaconda prompt (from scratch):

```
    $ conda activate lumispy
    $ jupyter lab
```