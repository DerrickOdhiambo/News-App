from flask import render_template
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_new,get_source_details,get_everything,get_sports,get_business

@main.route('/')
@main.route('/home/')
def index():

  sources = get_new()
  everything = get_everything()
  title = 'NewsPoint'
  return render_template('index.html',title = title, sources = sources, everything = everything)


@main.route('/source/<articles>')
def source(articles):

  sources = get_new()
  top_headlines = get_source_details(articles)
  print(top_headlines)
  title = 'NewsPoint Articles'

  return render_template('source.html',title=title, sources=sources,top_headlines = top_headlines)


@main.route('/sports')
def sports():

  sports = get_sports()
  title = 'NewsPoint Sports'

  return render_template('sports.html', title = title, sports = sports)


@main.route('/business')
def business():

  business = get_business()
  title = 'NewsPoint Business'

  return render_template('business.html', title = title, business = business)