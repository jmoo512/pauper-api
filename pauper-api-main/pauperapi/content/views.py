from flask import Blueprint, request, jsonify, abort
from marshmallow.exceptions import ValidationError
from pauperapi import db, cache
#from pauperapi.models import Content
from pauperapi.schemas import content_schema
from sqlalchemy import func, or_, and_

content = Blueprint('content',__name__)

@content.route('/content', methods=['GET'])
def get_content():
    return {}

@content.route('/content', methods=['POST'])
def add_content():
    return {}
