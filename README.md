# Goal

Predict the needed medical equipment against the coronavirus for every canton of Switzerland.

This app was developed during the [#CodeVsCOVID19 hackathon](https://www.codevscovid19.org/).


# Python Setup

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
