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

