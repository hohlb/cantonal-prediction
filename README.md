# Goal

Predict the needed medical equipment against the coronavirus for every canton of Switzerland.

Online demo: https://cantonal-prediction.herokuapp.com/

This app was developed during the [#CodeVsCOVID19 hackathon](https://www.codevscovid19.org/).


# Technologies Used

* Web framework: [Streamlit](https://www.streamlit.io)
* Data wrangling: [Pandas](https://pandas.pydata.org)
* Dataset: [COVID19 case numbers Cantons of Switzerland](https://github.com/openZH/covid_19)


# Setup for Development

First, download or `git clone` this repository to your PC.

Then, install the Python dependencies:

If you are using Python 3.6 or higher:
```bash
# change to this codebase directory that you just downloaded
cd cantonal-prediction

# create a virtual Python environment named ".venv" in this directory
python3 -m venv .venv

# activate the virtual Python environment we just created
source .venv/bin/activate

# update the package manager
python3 -m pip install --upgrade pip

# install the Python packages
python3 -m pip install -r requirements.txt
```

**Or** if you want to use `conda`:
```bash
# change to this codebase directory that you just downloaded
cd cantonal-prediction

# update the package (and environment) manager
conda update conda

# create a new conda environment in this directory
conda create --prefix ./.venv
conda activate .venv/
conda config --env --add channels conda-forge

# use Python 3.8
conda install python=3.8

# install the Python packages
python3 -m pip install -r requirements.txt
```


# Development

On your developer's PC, run this from the command line:
```bash
# change to this codebase directory
cd cantonal-prediction

# activate the virtual Python environment
#
# if you used "venv" in the previous step:
source .venv/bin/activate
# or alternatively, if you used "conda":
conda activate .venv/

# run the streamlit development web server
streamlit run cantonal_prediction.py
```

This will produce an URL that you can access in your web browser to use the app.


# Deployment (for future reference)

This web app will be deployed automatically
to https://cantonal-prediction.herokuapp.com/ with every code commit to this GitHub repository.

The automatic deployment was set up via the Heroku dashboard.
This works even using Heroku's free tier ✨

To configure the Heroku runtime, the files `Procfile`, `requirements.txt`, and `runtime.txt` of
this repository are used.

A basic tutorial for running streamlit on Heroku can be found
[here](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83).
