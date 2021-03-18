from flask import request, Blueprint, jsonify, abort
from marshmallow.exceptions import ValidationError
from pauperapi import db
from pauperapi.models import DeckContent,DeckList,Cards,MetaDeck
from pauperapi.schemas import deck_content_schema, decks_content_schema, decklist_schema, decklists_schema, decklistcontent_schema, decklistscontent_schema, card_schema, metadeck_schema, metadecks_schema
from flask_cors import CORS
from pprint import pprint


decks=Blueprint('decks',__name__,template_folder='templates')

CORS(decks)


#ADD NEW DECK AND DECK CONTENT
@decks.route('/decks', methods = ['POST'])
def add_deck_content():
    json_data = request.get_json()

    try:
        deck = DeckContent.from_dict(deck_content_schema.load(json_data))
    except ValidationError as err:
        print(err)
        abort(400)

    db.session.add(deck)
    db.session.commit()

    return deck_content_schema.dump(deck)

#MODIFY DECK CONTENT
@decks.route('/decks/<id>', methods=['PUT'])
def modify_deck_content(id):
    json_data = request.get_json()

    try:
        deck_content_data = deck_content_schema.load(json_data, partial = True)
    except ValidationError as err:
        print(err)
        abort(400, err.messages)

    q = DeckContent.query.filter_by(id=id)
    update_count = q.update(deck_content_data)

    if update_count == 0:
        abort(404)

    updated_deck_content = q.first()

    db.session.commit()

    return deck_content_schema.dump(updated_deck_content)

#GET DECK CONTENT
@decks.route('/decks/<id>', methods = ['GET'])
def get_deck_content(id):
    deck = DeckContent.query.filter(DeckContent.id==id).first_or_404()
    result = deck_content_schema.dump(deck)
    return jsonify(result)

#GET ALL DECKS AND ALL CONTENT
@decks.route('/decks', methods = ['GET'])
def get_all_decks():
    decks = DeckContent.query.all()
    result = decks_content_schema.dump(decks)
    return jsonify(result)

#GET LIST OF ALL DECK IDS AND NAMES
@decks.route('/listofdecks', methods = ['GET'])
def get_list_of_decks():
    decks = DeckContent.query.with_entities(DeckContent.id,DeckContent.name).all()
    result = decks_content_schema.dump(decks)
    return jsonify(result)

#GET DECKLIST
@decks.route('/decks/decklist/<deck_id>', methods = ['GET'])
def get_decklist(deck_id):

    decklist = DeckList.query.filter(DeckList.deck_id==deck_id).order_by(DeckList.card_name).all()

    list = []
    dict = {}

    for i in decklist:
        dict['id'] = i.id
        dict['card_name'] = i.card_name
        dict['card_qty'] = i.card_qty
        dict['active'] = i.active
        dict['mana_cost'] = i.cards[0].mana_cost
        dict['cs_id'] = i.cards[0].cs_id
        dict['price'] = i.cards[0].price
        dict['color_id'] = i.cards[0].color_id
        dict['cmc'] = int(i.cards[0].cmc)
        list.append(dict)
        dict = {}

    return jsonify(list)

#ADD SINGLE CARD TO DECKLIST
@decks.route('/decks/decklist/single/<deck_id>', methods = ["POST"])
def add_card_to_decklist(deck_id):
    json_data = request.get_json()

    try:
        decklist = DeckList.from_dict(decklist_schema.load(json_data, partial = True))

    except ValidationError as err:
        print(err)
        abort(400, err.messages)

    q = DeckList.query.filter_by(deck_id=deck_id).first_or_404()
    q.card_qty = decklist.card_qty
    q.card_name = decklist.card_name
    q.active = decklist.active
    q.deck_id = decklist.deck_id

    db.session.add(q)
    db.session.commit()

    return "YOLO"

#MODIFY SINGLE CARD QTY, ACTIVE STATE IN DECKLIST
@decks.route('/decks/decklist/single/<deck_id>', methods = ["PUT"])
def modify_card_in_decklist(deck_id):
    json_data = request.get_json()
    

    try:
        decklist = DeckList.from_dict(decklist_schema.load(json_data, partial = True))

    except ValidationError as err:
        print(err)
        abort(400, err.messages)

    card_name = decklist.card_name
    

    q = DeckList.query.filter_by(deck_id=deck_id,card_name=decklist.card_name).first_or_404()
    q.card_qty = decklist.card_qty
    q.card_name = decklist.card_name
    q.active = decklist.active
    q.deck_id = decklist.deck_id

    db.session.commit()

    return decklist_schema.dump(q)

#ADD NEW DECKLIST
@decks.route('/decks/<deck_id>', methods = ['POST'])
def add_decklist(deck_id):
    deck = DeckContent.query.filter(DeckContent.id==deck_id).first_or_404()

    json_data = request.get_json()
    for i in json_data:
        try:
            new_card = DeckList.from_dict(decklist_schema.load(i))
            card_match = Cards.query.filter(Cards.card_name == new_card.card_name).first()
            card_match.decks.append(new_card)
        except ValidationError as err:
            pprint(err.messages)
            abort(400)
        db.session.add(new_card)

    db.session.commit()

    return decklist_schema.dump(deck)

#GET ALL META TAGS
@decks.route('/decks/meta/<deck_id>', methods = ['GET'])
def get_deck_meta(deck_id):
    meta = MetaDeck.query.filter(MetaDeck.deck_id == deck_id).with_entities(MetaDeck.meta_tag, MetaDeck.active).all()
    print(meta)
    result = metadecks_schema.dump(meta)
    return jsonify(result)

#GET ALL META TAGS FOR SELECTED DECKS
@decks.route('/decks/meta', methods = ['GET'])
def get_all_meta():
    meta = MetaDeck.query.with_entities(MetaDeck.meta_tag).distinct().all()
    print(meta)
    result = metadecks_schema.dump(meta)
    return jsonify(result)

#ADD META TAG TO DECK
@decks.route('/decks/meta', methods = ['POST'])
def add_deck_meta():

    json_data = request.get_json()

    try:
        meta = MetaDeck.from_dict(metadeck_schema.load(json_data))
    except ValidationError as err:
        print(err)
        abort(400)

    db.session.add(meta)
    db.session.commit()

    return deck_content_schema.dump(meta)

#MODIFY META TAG IN A DECK
@decks.route('/decks/meta/<deck_id>', methods = ['PUT'])
def modify_meta_tag_in_deck(deck_id):
    json_data = request.get_json()

    try:
        meta = MetaDeck.from_dict(metadeck_schema.load(json_data, partial = True))

    except ValidationError as err:
        print(err)
        abort(400, err.messages)


    q = MetaDeck.query.filter(MetaDeck.meta_tag == meta.meta_tag, MetaDeck.deck_id==deck_id).first_or_404()
    q.meta_tag = meta.meta_tag
    q.active = meta.active
    q.deck_id = meta.deck_id

    db.session.commit()

    return decklist_schema.dump(q)
