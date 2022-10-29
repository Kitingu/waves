This is a simple flask application to server as a python refresher.

[![Build Status](https://app.travis-ci.com/Kitingu/waves.svg?branch=main)](https://app.travis-ci.com/Kitingu/waves)
[![Coverage Status](https://coveralls.io/repos/github/Kitingu/waves/badge.svg?branch=main)](https://coveralls.io/github/Kitingu/waves?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/336123c7e9aecf290d86/maintainability)](https://codeclimate.com/github/Kitingu/waves/maintainability)
## set up ##
 * Clone this repo to your device
 * change directory to the applications root folder
 * create a virtual env 
    * run ** virtualenv -p python3 venv for linux ** to create the virtual environment.
    * run ** source venv/bin/activate ** to activate the virtual environment
 * edit the sample.env file and rename it to .env
 * run ** source .env ** on terminal to use the environment variables defined in the .env file 
 * type python run.py  on terminal and press Enter. this will run the application.

## Endpoints:
    - Signup
    - Login
    - Get Users (Admin users only)
    - logout
    - Verify user
    - 