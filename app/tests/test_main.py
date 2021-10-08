from unittest import TestCase, skip
from flask_restx import Resource, Api

import app.main as main
import app.is_playlist_valid as is_valid
import app.import_playlist as imp_ply
playlistURL = 'https://open.spotify.com/playlist/0uWwYZ9XuQ3ed4X5xOLFP2?si=73916830bc0a487b'
 
class mainTest(TestCase):
	def setUp(self):
		pass

	def tesarDown(self):
		pass

	# def test_main(self):
	# 	import_playlist = main.importPlaylist(Resource)
	# 	ret = import_playlist.put(playlistURL)
	# 	self.assertAlmostEqual(ret, {'playlist': playlistURL[34:56], 'return': 'imported'})
	
	def test_is_valid(self):
		self.assertAlmostEqual(is_valid.is_valid(playlistURL), 'valid')
		self.assertAlmostEqual(is_valid.is_valid(playlistURL[-1:0]), 'invalid')

	def test_import_playlist_py(self):
		self.assertGreater(imp_ply.playlist_imp(playlistURL),1)