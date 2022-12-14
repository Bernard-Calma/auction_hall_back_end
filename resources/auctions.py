import models

from flask import Blueprint, request, jsonify
from flask_login import current_user
from playhouse.shortcuts import model_to_dict

auctions = Blueprint('auctions', 'auctions')

# Index Route
@auctions.route('/', methods = ['GET'])
def auctions_index():
    """Show all auctions"""
    result = models.Auctions.select()
    # print('Auctions: ', result) #query
    all_acutions = [model_to_dict(auction) for auction in result]
    # remove unecessary user data to be sent back to client
    for auction in all_acutions:
        auction['user'].pop('password')
        if auction['winner']:
            auction['winner'].pop('password')
        # print("PHOTO ", auction['photo'])
        # print("Get all auctions initiated")
        # CHANGE THIS TO NOT BE IN MEMORY
        auction.update({'photo': bytes(auction['photo']).decode('utf-8')})

    # print("ALL AUCTIONS : " , all_acutions)
    return jsonify(
        data    = all_acutions,
        message = "Successfully retrieved all auctions",
        status  = 200,
    ), 200

# Create Route
@auctions.route('/', methods = ['POST'])
def auction_create():
    """Create an auction"""
    payload = request.get_json()
    # print("Payload: ", payload)
    # print("Current User: ", current_user)

    # Convert uploaded photo to binary
    # print("PHOTO", payload['photo'])
    # print("PHOTO DICT", [json.dumps(payload['photo'])])
    # print(payload['photo'], "PHOTO URI")
    # photo = model_to_dict(payload['photo'])
 
    new_auction = models.Auctions.create(
        user = current_user.id,
        auction_date = payload['auction_date'],
        title = payload['title'],
        description = payload['description'],
        price = payload['price'],
        price_increment = payload['price_increment'],
        # need to make user upload a photo
        photo = payload['photo'],
        # need to inintiate a list to hold foreign keys
        participants = [],
    )
    auction_dict = model_to_dict(new_auction)    
    # Remove uneccessary properties of current user to be added in auction
    auction_dict['user'].pop('password')
    # print(auction_dict['photo'])
    # print(auction_dict, "New auction")
    return jsonify(
        data   = auction_dict,
        status = {
            'code'      : 200,
            'message'   : "Successfully added a new auction",
        }
    ), 200

#Show Route
@auctions.route('/<id>', methods = ['GET'])
def acution_one(id):
    """Get one Auction"""
    print("Show Route Initiated")
    query = models.Auctions.select().where(models.Auctions.id == id)
    query.execute()
    auction_found = model_to_dict(models.Auctions.get_by_id(id))
    del auction_found['user']['password']
    if auction_found['winner']:
        del auction_found['winner']['password']
    auction_found.update({'photo': bytes(auction_found['photo']).decode('utf-8')})
    return jsonify(
        data = auction_found,
        status = {
            'code'      : 200,
            'message'   : f"Successfully found Auction with ID: {id}",
        }
    ), 200

# Edit Route
@auctions.route('/<id>', methods = ['PUT'])
def auction_edit(id):
    """Edit auction by auction_id"""
    payload = request.get_json()
    query = models.Auctions.update(**payload).where(models.Auctions.id == id)
    query.execute()
    auction_edited = model_to_dict(models.Auctions.get_by_id(id))
    del auction_edited['user']['password']
    if auction_edited['winner']:
        del auction_edited['winner']['password']
    auction_edited.update({'photo': bytes(auction_edited['photo']).decode('utf-8')})
    return jsonify(
        data = auction_edited,
        status = {
            'code'      : 200,
            'message'   : f"Successfully updated Auction ID: {id}",
        }
    ), 200

# DELETE ROUTE
@auctions.route('/<id>', methods = ['DELETE'])
def auction_delete(id):
    """Delete auction by ID"""
    query = models.Auctions.delete_by_id(id)
    return jsonify(
        data = {},
        status = {
            'code'      : 200,
            'message'   : f"Auction: {id} is sucessfully deleted"
        }
    )

#Start Auction Show Route
@auctions.route('/start/<id>', methods = ['GET'])
def acution_start(id):
    """Get one Auction"""
    print("Show Route Initiated")
    query = models.Auctions.select().where(models.Auctions.id == id)
    query.execute()
    auction_found = model_to_dict(models.Auctions.get_by_id(id))
    del auction_found['user']['password']
    if auction_found['winner']:
        del auction_found['winner']['password']
    auction_found.update({'photo': bytes(auction_found['photo']).decode('utf-8')})
    return jsonify(
        data = auction_found,
        status = {
            'code'      : 200,
            'message'   : f"Successfully found Auction with ID: {id}",
        }
    ), 200

 #Start Auction Edit Route
@auctions.route('/start/<id>', methods = ['POST'])
def acution_start_edit(id):
    """Get one Auction"""
    print("Edit Route Initiated")
    payload = request.get_json()
    print("BODY: ", payload)
    query = models.Auctions.update(**payload).where(models.Auctions.id == id)
    query.execute()
    auction_found = model_to_dict(models.Auctions.get_by_id(id))
    print(auction_found)
    del auction_found['user']['password']
    if auction_found['winner']:
        del auction_found['winner']['password']
    auction_found.update({'photo': bytes(auction_found['photo']).decode('utf-8')})
    # print(auction_found)
    return jsonify(
        data = auction_found,
        status = {
            'code'      : 200,
            'message'   : f"Successfully found Auction with ID: {id}",
        }
    ), 200   
# TO DO
# ADD ERROR HANDLING WHEN FOR ROUTES WHEN INVALID PARAMS ARE SENT OVER