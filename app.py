# Import required libraries
from flask import Flask, render_template, request
import config  # Import configuration from the config.py file

# Define a custom error handler for 404 errors
def page_not_found(e):
  return render_template('404.html'), 4
