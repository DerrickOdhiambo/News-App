from flask import render_template
from . import main


@main.errorhandler(404)
def error_handler():
  """
  Funtion to render error file
  """

  return render_template('error.html'),404