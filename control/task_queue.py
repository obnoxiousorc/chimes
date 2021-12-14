from multiprocessing import Process, Queue
import logging
import time
from control import parser
from control.models import ChimesSet

q = Queue()
logger = logging.getLogger('django')

chimes = {}
for chime in Chime.objects.filter(chimes_set_id=1):
	chimes[chime.note_name] = chime

DING_DISTANCE = 20
DING_DELAY = 0.1

def play_chord(chord):
	for note in chord['notes']:
		location = chimes[note].kit_location
		home = chimes[note].home_position
		logger.error(f"Playing note {note}, position {location}, home {home}")
		kit.servo[location].angle = home + DING_DISTANCE

	time.sleep(DING_DELAY)

	for note in chord['notes']:
		location = chimes[note].kit_location
		home = chimes[note].home_position
		kit.servo[location].angle = home


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
		play_chord(part)
		time.sleep(song['speed_mult'] * part['delay'])


def worker():
	while True:
		song = q.get()
		play_song(song)


p = Process(target=worker)
p.start()
