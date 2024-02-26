#!/usr/bin/python3
  2 """ Blueprint for API """
  3 
  4 from flask import Blueprint 
  5 
  6 from api.v1.views.index import *
  7 from api.v1.views.states import *
  8 from api.v1.views.places import *
  9 from api.v1.views.places_reviews import *
 10 from api.v1.views.cities import *
 11 from api.v1.views.amenities import *
 12 from api.v1.views.users import *
 13 from api.v1.views.places_amenities import *
 14 
 15 app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
