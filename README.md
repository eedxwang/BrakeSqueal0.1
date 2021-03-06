BrakeSqueal: Python Implementation of Parametric Model Reduction in Disc Brake Modelling
Version: 0.1
========================================

Introduction
------------
The dynamical modelling of disc brake via finite element method using commercial packages usually results in a large scale quadratic eigen value problem (QEVP) with parameter dependent, non-symmetric coefficients. The parametric study of brake squeal requires the solution of QEVP for several choices of the parameters. The task was to implement a new parameter dependent subspace projection approach, where the subspaces are determined from non-symmetric problems evaluated at many different parameter values, where the dominant modes are calculated by performing a proper orthogonal decomposition (POD). The implementation was done in Python using interfaces to ATLAS LAPACK and BLAS libraries for LU factorization/solve and ARPACK for sparse eigen value problems. 

Useful link with references to different linear algebra libraries: http://www.netlib.org/utk/people/JackDongarra/la-sw.html

Requirements
------------
Standard Python Packages (docutils, matplotlib, numpy, scipy, sphinx, vtk)
texlive-full (for latex documentation generation using sphinx)


Getting Started
---------------
./infoPackages (for information related to python packages installed, plots generated in ./output/<date/>).

specify all the problem parameters in createBrakeClassObject.py including the logging level, input/output path.
Don't forget to pass logging level and reference omega when it is called example createBrakeClassObject.returnObject(20,1)
 
python analyseData.py (for data analysis)

python compareTraditionalPOD.py (for relative error plots comparing traditional approach and POD approach)

python plotEigsExactClassicalPOD.py (for eigenvalue plots comparing traditional approach and POD approach)



./cleanRepository (example for cleaning(.pyc, *~) from the current repository before pushing changes to bitbucket)


Installation
---------------
Install using `python setup.py install`
to create a source distribution for this module `python setup.py sdist`


Documentation
---------------
http://sphinx-doc.org/tutorial.html

To update the current documentation perform the following steps.

1. When documenting Python code, it is common to put a lot of documentation in the source files, 
in documentation strings. Sphinx supports the inclusion of docstrings from the modules with an 
extension called “autodoc”. The autodoc feature has already been activated in conf.py. 
To add suitable docstrings in the current python code follow
http://sphinx-doc.org/ext/autodoc.html#module-sphinx.ext.autodoc 

2. When adding a new module with docstrings update doc/index.rst

3. Update the git code repository.

4. Update documentation using `BrakeSqueal0.1/doc/ make html` (or make latexpdf, for more options check the inculded Makefile).

html documenation available in `BrakeSqueal0.1/doc/_build/html/index.html`
latex documenation available in `BrakeSqueal0.1/doc/_build/latex/BrakeSqueal.pdf`
