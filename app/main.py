from flask import Flask, request, render_template, session, json, url_for, redirect, jsonify
from flask_restx import Api, Resource, fields
from flask_session import Session
from app.import_playlist import*
from flask_cors import CORS, cross_origin
import subprocess
import os.path
from os import path

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)
app.config["SECRET_KEY"] = '1239120312301'
app.config.from_object(__name__)
#Session(app)
Session()
response = ''

class userSession(object):
    def __init__(self, playlistLink):
        self.id = ''
        self.playlistName = playlistLink
    def get(self):
        # return json.dumps(self.playlistName, default=lambda o: o.__dict__, 
        #     sort_keys=True, indent=4)
        return self.playlistName
        # api.abort(404,"User with playlist % not exist".format(id))

@api.route('/importPlaylist/<path:playlistURL>')
class importPlaylist(Resource):
    @api.expect()
    def put(self, playlistURL):
        # print(playlistURL)
        if(path.exists("playlists/%s.csv"%playlistURL[-16:-1])):
            return {'return':'playlists already imported, can proceed or force import from /importPlaylist/F/{URL}'}
        else:
            playlist_imp(playlistURL)
            return {'playlist': playlistURL[-16:-1], 'return':'imported'}

@api.route('/importPlaylist/F/<path:playlistURL>')
class importPlaylistF(Resource):
    api.expect()
    def put(self, playlistURL):
        playlist_imp(playlistURL)
        return {'playlist': playlistURL[-16:-1], 'return':'imported'}
      
@api.route('/endpoints')
class Endpoints(Resource):
    def get(self):
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}

