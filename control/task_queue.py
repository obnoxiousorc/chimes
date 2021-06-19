from multiprocessing import Process, Queue
import logging
import time
from control import parser

q = Queue()
logger = logging.getLogger('django')

def play(note):
	logger.error(note)

def play_song(song):
	song = {
		'name': song.name,
		'data': parser.import_notes(song.data),
		'speed_mult': 1
	}

	# TODO: Make this not an error message
	logger.error(f"Playing song {song['name']}")
	time.sleep(3)
	for part in song['data']:
		for note in part['notes']:
			play(note)
		time.sleep(song['speed_mult'] * part['delay'])

def worker():
	while True:
		song = q.get()
		play_song(song)

p = Process(target=worker)
p.start()