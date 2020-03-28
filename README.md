# Goal

Predict the needed medical equipment against the coronavirus for every canton of Switzerland.

Online demo: https://cantonal-prediction.herokuapp.com/

This app was developed during the [#CodeVsCOVID19 hackathon](https://www.codevscovid19.org/).


# Setup for Development

If you are using Python 3.6 or higher:
```bash
pip install streamlit
```

**Or** if you want to use `conda`:
```bash
# create a new conda environment in your current directory
conda create --prefix ./conda-env
conda activate conda-env/
conda config --env --add channels conda-forge

# use Python 3.8
conda install python=3.8
pip install streamlit
```


# Development

On your developer's PC, run this from the command line:
```bash
streamlit run cantonal_prediction.py
```

This will produce an URL that you can access in your web browser to use the app.


# Deployment (for future reference)

This web app will be deployed automatically
to https://cantonal-prediction.herokuapp.com/ with every code commit to this GitHub repository.

The automatic deployment was set up via the Heroku dashboard.

To configure the Heroku runtime, the files `Procfile`, `requirements.txt`, and `runtime.txt` of
this repository are used.

A basic tutorial for running streamlit on Heroku can be found
[here](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83).
