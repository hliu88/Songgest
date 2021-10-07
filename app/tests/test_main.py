from unittest import TestCase, skip
from flask_restx import Resource, Api

import app.main as main

class mainTest(TestCase):
	def setUp(self):
		pass

	def tesarDown(self):
		pass

	def test_main(self):
		import_playlist = main.importPlaylist(Resource)
		# ret = import_playlist.put('https://open.spotify.com/playlist/114JM3RIWLBz7f4j1dTYjU?si=a084fb36f5004f6e')
		ret = import_playlist.put('https://open.spotify.com/playlist/114JM3RIWLBz7f4j1dTYjU')