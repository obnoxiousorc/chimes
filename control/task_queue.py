from multiprocessing import Process, Queue
import logging
import time

q = Queue()
logger = logging.getLogger('django')

def play_song(song):
	time.sleep(5)
	# TODO: Make this not an error message
	logger.error(f'Playing song {song.name}')

def worker():
	while True:
		song = q.get()
		play_song(song)

p = Process(target=worker)
p.start()