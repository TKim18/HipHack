import os
from flask import Flask
from flask.ext import restful
from flask import make_response
from json import dumps
from hiphack import app

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import hiphack.api.resources
