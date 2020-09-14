from flask import render_template
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_new,get_source_details

@main.route('/')
def index():

  sources = get_new()
  return render_template('index.html', sources = sources)


@main.route('/source/<source>')
def source(source):

  sources = get_new()
  top_headlines = get_source_details(source)
  title = f'{source.name}'

  return render_template('source.html', title=title, sources=sources,top_headlines = top_headlines)