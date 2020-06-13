# FreeStyleLibre
In the conda-shell type:

`conda create -n Libre python=3.7`

Then install necessary packages such as pandas

`conda install -n Libre pandas requests`

Activate the environment by running `conda activate Libre` then run the code with `python app.py`

# Usability
The process is not very user friendly, however, the app is reliable and imports the csv to the cloud and saves the last imported data on the machine so that you do not upload already imported data.
The main hiccup on the way of usability was the captcha authentication on the LibreView cloud which prevents the automatic download from the website. Could possibly be mitigated with https://github.com/ecthros/uncaptcha2. However, due to time limitations it was not implemented.

# Images

![alt text](https://github.com/chbakardgiev/FreeStyleLibre/blob/master/2020-06-13-143153_1920x1080_scrot.png?raw=true)
![alt text](https://github.com/chbakardgiev/FreeStyleLibre/blob/master/2020-06-13-143149_1920x1080_scrot.png?raw=true)
