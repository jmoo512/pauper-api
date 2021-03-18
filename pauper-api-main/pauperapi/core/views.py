from flask import render_template,request,Blueprint,redirect,url_for
from pauperapi import db, cache
#from pauperapi.models import DeckList,Box,DeckContent,Content,Cards,Core
from datetime import datetime

core = Blueprint('core',__name__)

@core.route('/')
def index():

    return {}
