Simple Flask app for Heroku.

Because Bo is awesome. :heart_eyes_cat: :dance:

###Setup
Create a Strava application
https://www.strava.com/developers

Ensure you have a nice python environment with virtualenv
```bash
which python
python -v # Test with 2.7
which virtualenv # If it's not there install with;
# pip install virtualenv
```

Setup a .config file for virtualenv which'll set some environment variables
```bash
cp .config.example .config # Edit accordingly
```

```bash
make  # set up virtual env
. env/bin/activate  # activate env
make run  # start dev server
```
