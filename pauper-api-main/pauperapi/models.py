from pauperapi import db
from datetime import datetime

deck_meta = db.Table('deck_meta',
    db.Column('deck_id', db.Integer, db.ForeignKey('deckcontent.id', ondelete = 'CASCADE')),
    db.Column('meta_id', db.Integer, db.ForeignKey('metadeck.id', ondelete = 'CASCADE')))

class DeckContent(db.Model):
    __tablename__='deckcontent'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)
    strategy=db.Column(db.Text)
    mana=db.Column(db.String(100))
    key_card1=db.Column(db.String(50))
    key_card2=db.Column(db.String(50))
    key_card3=db.Column(db.String(50))
    key_card4=db.Column(db.String(50))
    box=db.Column(db.String(50))
    tag_line=db.Column(db.String(100))
    author=db.Column(db.String(50))
    source=db.Column(db.String(200))
    price=db.Column(db.Float)
    rating=db.Column(db.Integer)
    core=db.Column(db.Boolean)
    match_wins=db.Column(db.Integer)
    match_losses=db.Column(db.Integer)
    game_wins=db.Column(db.Integer)
    game_losses=db.Column(db.Integer)


    @classmethod
    def from_dict(self,data):
        return DeckContent(
            name=data['name'],
            strategy=data['strategy'],
            mana=data['mana'],
            key_card1=data['key_card1'],
            key_card2=data['key_card2'],
            key_card3=data['key_card3'],
            key_card4=data['key_card4'],
            box=data['box'],
            tag_line=data['tag_line'],
            author=data['author'],
            source=data['source'],
            price=data['price'],
            rating=data['rating'],
            core=data['core'],
            match_wins=data['match_wins'],
            match_losses=data['match_losses'],
            game_wins=data['game_wins'],
            game_losses=data['game_losses'],
        )



class MetaDeck(db.Model):
    __tablename__='metadeck'
    id=db.Column(db.Integer,primary_key=True)
    meta_tag=db.Column(db.String(20))
    active=db.Column(db.Boolean)
    deck_id=db.Column(db.Integer)
    deck = db.relationship('DeckContent', secondary=deck_meta, backref=db.backref('meta',lazy='dynamic'), cascade='delete')

    @classmethod
    def from_dict(self,data):
        return MetaDeck(
            meta_tag = data['meta_tag'],
            active = data['active'],
            deck_id = data['deck_id']
        )

class MetaCard(db.Model):
    __tablename__='metacard'
    id=db.Column(db.Integer,primary_key=True)
    meta_tag=db.Column(db.String(20))
    active=db.Column(db.Boolean)
    card_id=db.Column(db.Integer)

card_meta = db.Table('card_meta',
    db.Column('card_id', db.Integer, db.ForeignKey('cards.id', ondelete = 'CASCADE')),
    db.Column('meta_id', db.Integer, db.ForeignKey('metacard.id', ondelete = 'CASCADE')))

class Cards(db.Model):
    __tablename__='cards'
    id=db.Column(db.Integer,primary_key=True)
    card_name=db.Column(db.String(50), unique=True)
    card_type=db.Column(db.String(20))
    mana_cost=db.Column(db.String(250))
    cs_id=db.Column(db.Integer)
    price=db.Column(db.Float)
    color_id=db.Column(db.String(20))
    cmc=db.Column(db.Integer)


    @classmethod
    def from_dict(self, data):
        return Cards(
            card_name=data['card_name'],
            card_type=data['card_type'],
            mana_cost=data['mana_cost'],
            cs_id=data['cs_id'],
            price=data['price'],
            color_id=data['color_id'],
            cmc=data['cmc']
        )

deck_cards = db.Table('deck_cards',
        db.Column('card_id', db.Integer, db.ForeignKey('cards.id', ondelete = 'CASCADE')),
        db.Column('decklist_id', db.Integer, db.ForeignKey('decklist.id', ondelete = 'CASCADE')))

class DeckList(db.Model):
    __tablename__='decklist'
    id=db.Column(db.Integer,primary_key=True)
    card_name=db.Column(db.String(50))
    card_qty=db.Column(db.Integer)
    active=db.Column(db.Boolean)
    deck_id=db.Column(db.Integer)
    cards = db.relationship('Cards', secondary=deck_cards, backref=db.backref('decks', lazy='dynamic'), cascade='delete')

    @classmethod
    def from_dict(self, data):
        return DeckList(
            card_name=data['card_name'],
            card_qty=data['card_qty'],
            active=data['active'],
            deck_id=data['deck_id']
        )

class NonCards(db.Model):
    __tablename__='noncards'
    id=db.Column(db.Integer,primary_key=True)
    card_name=db.Column(db.String(50))
