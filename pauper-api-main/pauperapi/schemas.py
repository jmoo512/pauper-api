
from marshmallow import Schema, fields

class AuthorsSchema(Schema):
    id = fields.Int()
    name = fields.String()
    mtgo_name = fields.String()
    mtga_name = fields.String()
    twitter = fields.String()
    youtube = fields.String()
    twitch = fields.String()
    bio = fields.String()
    tag_line = fields.String()

author_schema = AuthorsSchema()
authors_schema = AuthorsSchema(many=True)

class BoxSchema(Schema):
    id = fields.Int()
    name = fields.String()
    deck = fields.String()
    desc = fields.String()

box_schema = BoxSchema()
boxes_schema = BoxSchema(many=True)

class CardSchema(Schema):
    id = fields.Int()
    card_name = fields.String()
    card_type = fields.String()
    mana_cost = fields.String()
    cs_id = fields.Integer()
    price = fields.Float()
    color_id = fields.String()
    cmc = fields.String()

card_schema = CardSchema()
cards_schema = CardSchema(many=True)

class ContentSchema(Schema):
    id = fields.Int()
    date = fields.Date()
    title = fields.String()
    text = fields.String()
    tag = fields.String()
    tag_line = fields.String()
    #related_deck = fields.String()
    #related_box = fields.String()
    #related_card = fields.String()
    #related_set = fields.String()
    published = fields.Boolean()
    league_id = fields.Int()
    tournament_id = fields.Int()
    author_id = fields.Int()

content_schema = ContentSchema()
contents_schema = ContentSchema(many=True)

class DeckContentSchema(Schema):
    id = fields.Int()
    name = fields.String()
    strategy = fields.String()
    mana = fields.String()
    key_card1 = fields.String()
    key_card2 = fields.String()
    key_card3 = fields.String()
    key_card4 = fields.String()
    box = fields.String()
    tag_line = fields.String()
    author = fields.String()
    source = fields.String()
    price = fields.Float()
    rating = fields.Integer()
    core = fields.Boolean()
    match_wins = fields.Int()
    match_losses = fields.Int()
    game_wins = fields.Int()
    game_losses = fields.Int()


deck_content_schema = DeckContentSchema()
decks_content_schema = DeckContentSchema(many=True)

class DeckListSchema(Schema):
    id = fields.Int()
    card_name = fields.String()
    card_qty = fields.Integer()
    active = fields.Boolean()
    deck_id = fields.Integer()

decklist_schema = DeckListSchema()
decklists_schema = DeckListSchema(many=True)

class DeckListContentSchema(Schema):
    id = fields.Int()
    card_name = fields.String()
    card_qty = fields.Int()
    card_type = fields.String()
    mana_cost = fields.String()
    cs_id = fields.Int()
    price = fields.Float()
    color_id = fields.String()
    cmc = fields.Int()

decklistcontent_schema = DeckListContentSchema()
decklistscontent_schema = DeckListContentSchema(many=True)

class LeagueSchema(Schema):
    id = fields.Int()
    league_id = fields.Int()
    tournament_id = fields.Int()
    match_id = fields.Int()
    deck1 = fields.String()
    deck2 = fields.String()
    deck1_points = fields.Int()
    deck2_points = fields.Int()
    notes = fields.String()

league_schema = LeagueSchema()
leagues_schema = LeagueSchema(many=True)

class MetaDeckSchema(Schema):
    id = fields.Int()
    meta_tag = fields.String()
    active = fields.Boolean()
    deck_id = fields.Int()

metadeck_schema = MetaDeckSchema()
metadecks_schema = MetaDeckSchema(many=True)

class ResourcesSchema(Schema):
    id = fields.Int()
    deck_name = fields.String()
    resource = fields.String()
    published_date = fields.Date()

resoure_schema = ResourcesSchema()
resources_schema = ResourcesSchema(many=True)

class SideBoardSchema(Schema):
    id = fields.Int()
    deck_name = fields.String()
    card_name = fields.String()
    card_qty = fields.Int()
    active = fields.Boolean()

sideboard_schema = SideBoardSchema()
sideboards_schema = SideBoardSchema(many=True)

class SpiceRackSchema(Schema):
    id = fields.Int()
    deck_name = fields.String()
    card_name = fields.String()

spicerack_schema = SpiceRackSchema()
