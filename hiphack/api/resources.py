import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from hiphack.api import api

from address_to_geocode import address_to_geocode

class Root(restful.Resource):
    def get(self):
        return {
            'result': 'OK'
        }

class Geolocate(restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('address', type=str, location='args', required=False)
        args = parser.parse_args()

        lookup = address_to_geocode(args.get('address'))

        if lookup.get('err'):
            return {
                'error': lookup['err']
            }

        return lookup['result']

class HipChatGeolocate(restful.Resource):
    def post(self):
        args = json.loads(request.data)

        print(args)
        address = args['item']['message']['message'].replace('/inspire ', '')

        print(address)
        lookup = address_to_geocode(address)

        print(lookup)

        message = "Something went wrong. Try again later."
        color = "green"
        if lookup.get('err'):
            color = "red"
            message = "Failed lookup: " + lookup['err']
        else:
            print("formatting message")
            message = "hi"
            #message = "Found at (lat, long) of (%.4f, %.4f)" % (lookup['result']['lat'], lookup['result']['lng'])

        return {
            "color": color,
            "message": message,
            "notify": False,
            "message_format": "text"
        }

api.add_resource(Root, '/')
api.add_resource(Geolocate, '/geo')
api.add_resource(HipChatGeolocate, '/hipchat/geo')
