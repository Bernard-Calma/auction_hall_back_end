import models
import datetime

from flask import Blueprint, request, jsonify
from flask_login import current_user

from playhouse.shortcuts import model_to_dict


auctions = Blueprint('auctions', 'auctions')

# Index Route
@auctions.route('/', methods = ['GET'])
def auctions_index():
    """Show all auctions"""
    result = models.Auctions.select()
    print('Auctions: ', result)

# Create Route
@auctions.route('/', methods = ['POST'])
def auction_create():
    """Create an auction"""
    payload = request.get_json()
    print("Payload: ", payload)
    print("Current User: ", current_user)
    new_auction = models.Auctions.create(
        user = current_user.id,
        auction_date = payload['auction_date'],
        title = payload['title'],
        description = payload['description'],
        price = payload['price'],
        price_increment = payload['price_increment'],
        # need to make user upload a photo
        # photo = "No Photo",
        # need to inintiate a list to hold foreign keys
        # participants = [],
    )
    auction_dict = model_to_dict(new_auction)    
    # Remove uneccessary properties of current user to be added in auction
    auction_dict['user'].pop('password')
    print(auction_dict, "New auction")
    return auction_dict