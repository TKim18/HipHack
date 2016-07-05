import requests

def address_to_geocode(address):
        value = { 'err': '', 'result': '' }

        if not address:
            value['err'] = "No address supplied"
            return value

        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address)
        json = r.json()

        if not json:
            value['err'] =  'No results returned'

        if not json.get('results'):
            value['err'] = "Empty results returned"

        if not json['results'][0]:
            value['err'] = "Empty results returned"

        if not json['results'][0].get('geometry'):
            value['err'] = "No geometry returned for that location"

        if not json['results'][0]['geometry'].get('location'):
            value['err'] =  "No location data returned for that location's geometry"

        if not value['err']:
            value['result'] = json['results'][0]['geometry']['location']

        return value
