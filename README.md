# FlaskTestingApp

Starting from Basics:

Setting Virtual Environment with anaconda:

#Checking conda version ( also test if anaconda is installed )
```
conda -V
```
#Updating anaconda
```
conda update conda
```
#Creating virtual environment with the name venv and python version 2.7.11
```
conda create -n venv python=2.7.11 anaconda
```
#Activate venv
```
source activate venv
```
#Installing a package in the virtual environment
```
conda install -n venv [packageName]
```
#DeActivate venv 
```
source deactivate
```
#Remove venv with all its properties if it no longer required ( Don't do this )
```
conda remove -n venv -all
```
