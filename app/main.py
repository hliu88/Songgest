from flask import Flask
from flask_restx import Api, Resource
from app.import_playlist import playlist_imp
from app.is_playlist_valid import is_valid
from app.get_genre import get_gen
from app.display_genre import display_gen
from app.suggest import ML
import json
from os import path
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r'/*': {'origins': '*'}})
playlistInvalid_return = {'return': 'playlist url invalid'}
playlistNotImported_return = {'return': 'playlist not imported'}

# @api.route('/test')
# class importPlaylist(Resource):
#     """
#     ImportPlaylist from user input playlist URL
#     """
#     @api.expect()
#     def get(self):
#         return {'return': 'bonjour'}


@api.route('/importPlaylist/<path:playlistURL>')
class importPlaylist(Resource):
    """
    ImportPlaylist from user input playlist URL
    """
    @api.expect()
    def post(self, playlistURL):
        if not(is_valid(playlistURL)):
            return playlistInvalid_return
        if(path.exists("playlists/%s.csv" % playlistURL[34:56])):
            return {'return': 'playlists already imported,\
            can proceed or force import from /importPlaylist/F/{URL}'}
        else:
            playlist_imp(playlistURL)
            return {'playlist': playlistURL[34:56], 'return': 'imported'}


@api.route('/importPlaylist/F/<path:playlistURL>')
class importPlaylistF(Resource):
    """
    Force import playlist of url that was already imported previously
    Updates contents from previously imported playlist
    """
    @api.expect()
    def post(self, playlistURL):
        if not(is_valid(playlistURL)):
            return playlistInvalid_return
        playlist_imp(playlistURL)
        return {'playlist': playlistURL[34:56], 'return': 'imported'}


@api.route('/get_genre/<path:playlistURL>')
class get_genre(Resource):
    """
    Acquire genre of all songs in playlist for later ML
    """
    @api.expect()
    def put(self, playlistURL):
        if not(is_valid(playlistURL)):
            return playlistInvalid_return
        if not(path.exists("playlists/%s.csv" % playlistURL[34:56])):
            return playlistNotImported_return
        else:
            get_gen(playlistURL[34:56])
            return {'return': 'genres added'}


@api.route('/display_genre/<path:playlistURL>')
class display_genre(Resource):
    """
    Display all catagories of genres in the playlist
    """
    @api.expect()
    def get(self, playlistURL):
        if not(is_valid(playlistURL)):
            return playlistInvalid_return
        if not(path.exists("playlists/%s_ML.csv" % playlistURL[34:56])):
            return {'return': 'playlist not processed/imported'}
        else:
            output = json.dumps(display_gen(playlistURL[34:56]))
            return {'return': json.loads(output)}


@api.route('/suggest/<path:playlistURL>')
class suggest(Resource):
    """
    Suggests playlist from playlist that is imported and added genres
    """
    @api.expect()
    def get(self, playlistURL):
        if not(is_valid(playlistURL)):
            return playlistInvalid_return
        if not(path.exists("playlists/%s.csv" % playlistURL[34:56])):
            return playlistNotImported_return
        else:
            output = json.dumps(ML('playlist'))
            return {'return': output}


@api.route('/endpoints')
class Endpoints(Resource):
    def get(self):
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


# parameters = api.model('Name Model', {'feature':
#                                       fields.String(
#                                         required=True,
#                                         description="feature preference",
#                                         help="feature cannot be blank"),
#                                       'artist':
#                                       fields.String(
#                                         required=True,
#                                         description="artist preference",
#                                         help="artist cannot be blank")})


# @api.route('/analyse/<path:playlistURL>')
# class analyse(Resource):
#     @api.expect(parameters)
#     def put(self, playlistURL):
#         try:
#             return {'return': request.json['feature']}
#         except KeyError:
#             return {'return': "KeyError"}
