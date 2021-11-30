from unittest import TestCase, skip
from flask_restx import Resource, Api

import app.main as main
import app.is_playlist_valid as is_valid
import app.import_playlist as imp_ply
import app.display_genre as disp_gen
import app.suggest as sugg
playlistURL = 'https://open.spotify.com/playlist/0uWwYZ9XuQ3ed4X5xOLFP2?si=73916830bc0a487b'
PLName = '0uWwYZ9XuQ3ed4X5xOLFP2'
 
class mainTest(TestCase):
	def setUp(self):
		pass

	def tesarDown(self):
		pass

	def test_main(self):
		ret = main.importPlaylist(Resource).post(playlistURL)
		self.assertTrue(ret)

		ret = main.get_genre(Resource).put(playlistURL)
		self.assertTrue(ret)

		ret = main.display_genre(Resource).get(playlistURL)
		self.assertTrue(ret)

		# ret= main.suggest(Resource).get(playlistURL)
		# self.assertTrue(ret)
	
	# def test_is_valid(self):
	# 	self.assertEqual(is_valid.is_valid(playlistURL), True)
	# 	self.assertEqual(is_valid.is_valid(playlistURL[-1:0]), False)

	# def test_import_playlist_py(self):
	# 	self.assertGreater(imp_ply.playlist_imp(playlistURL),1)

	# def test_display_genre_py(self):
	# 	self.assertIsInstance(disp_gen.display_gen('master'), list)

	# def test_suggest_py(self):
	# 	self.assertIsInstance(sugg.ML(PLName), list or str)