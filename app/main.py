from flask import Flask, request
from flask_restx import Api, Resource, fields
# from flask_session import Session
from app.import_playlist import playlist_imp
from app.is_playlist_valid import is_valid
from app.get_genre import get_gen
from app.display_genre import display_gen
from app.suggest import ML
# from flask_cors import CORS, cross_origin
# import subprocess
# import os.path
import json
from os import path

app = Flask(__name__)
api = Api(app)
# CORS(app, support_credentials=True)
# app.config["SECRET_KEY"] = '1239120312301'
# app.config.from_object(__name__)

parameters = api.model('Name Model', {'feature':
                                      fields.String(
                                        required=True,
                                        description="feature preference",
                                        help="feature cannot be blank"),
                                      'artist':
                                      fields.String(
                                        required=True,
                                        description="artist preference",
                                        help="artist cannot be blank")})


@api.route('/analyse/<path:playlistURL>')
class analyse(Resource):
    @api.expect(parameters)
    def put(self, playlistURL):
        try:
            return {'return': request.json['feature']}
        except KeyError:
            return {'return': "KeyError"}


@api.route('/importPlaylist/<path:playlistURL>')
class importPlaylist(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        if(path.exists("playlists/%s.csv" % playlistURL[34:56])):
            return {'return': 'playlists already imported,\
            can proceed or force import from /importPlaylist/F/{URL}'}
        else:
            playlist_imp(playlistURL)
            return {'playlist': playlistURL[34:56], 'return': 'imported'}


@api.route('/importPlaylist/F/<path:playlistURL>')
class importPlaylistF(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        playlist_imp(playlistURL)
        return {'playlist': playlistURL[34:56], 'return': 'imported'}


@api.route('/getStats/<path:playlistURL>')
class getStats(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        if not(path.exists("playlists/%s.csv" % playlistURL[34:56])):
            return {'return': 'playlist not imported'}
        # make function call for stats
        return {'return': 'playlist exists'}


@api.route('/get_genre/<path:playlistURL>')
class get_genre(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        if not(path.exists("playlist/%s.csv" % playlistURL[34:56])):
            return {'return': 'playlist not imported'}
        else:
            get_gen(playlistURL[34:56])
            return {'return': 'genre added'}


@api.route('/display_genre/<path:playlistURL>')
class display_genre(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        if not(path.exists("playlist/%s_ML.csv" % playlistURL[34:56])):
            return {'return': 'playlist not processed/imported'}
        else:
            output = json.dumps(display_gen(playlistURL[34:56]))
            return {'return': json.loads(output)}


@api.route('/suggest/<path:playlistURL>')
class suggest(Resource):
    @api.expect()
    def put(self, playlistURL):
        if(is_valid(playlistURL) == 'invalid'):
            return {'return': 'playlist url invalid'}
        if not(path.exists("playlist/%s.csv" % playlistURL[34:56])):
            return {'return': 'playlist not imported'}
        else:
            output = json.dumps(ML('playlist'))
            return {'Songs suggested': output}


@api.route('/endpoints')
class Endpoints(Resource):
    def get(self):
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}
