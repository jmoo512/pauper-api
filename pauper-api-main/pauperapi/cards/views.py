from flask import request, Blueprint, jsonify, abort
from marshmallow.exceptions import ValidationError
from pauperapi import db
from pauperapi.models import Cards
from pauperapi.schemas import card_schema, cards_schema
from flask_cors import CORS


cards=Blueprint('cards',__name__)

CORS(cards)

#GET SINGLE CARD DATA
@cards.route('/cards/<card_name>', methods=['GET'])
def get_card(card_name):
    card = Cards.query.filter(Cards.card_name==card_name).first_or_404()
    result = card_schema.dump(card)
    return jsonify(result)

#GET ALL CARDS AND CARD DATA IN DATABASE
@cards.route('/cards', methods = ['GET'])
def get_cards():
    cards = Cards.query.all()
    result = cards_schema.dump(cards)
    return jsonify(result)

#ADD NEW CARD AND DATA TO DATABASE
@cards.route('/cards', methods = ['POST'])
def add_card():
    json_data = request.get_json()

    try:
        card = Cards.from_dict(card_schema.load(json_data))
    except ValidationError as err:
        print(err)
        abort(400)

    db.session.add(card)
    db.session.commit()

    return card_schema.dump(card)
