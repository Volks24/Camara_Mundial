import urllib.request
import urllib.parse
import re
import webbrowser
import time
import vlc
import pafy



lista = pafy.get_playlist("https://www.youtube.com/playlist?list=PLjFgPOyCviLdaQm59HR6ZP9KkMRi1zo-n") # Cargo la lista para el loop

while True:
	for k in range(0,len(lista["items"])):
		url = "http://www.youtube.com/watch?v=" + lista["items"][k]['pafy'].videoid
		video = pafy.new(url)
		best = video.getbest()
		#Duracion = video.length
		media = vlc.MediaPlayer(best.url)
		media.play()
		time.sleep(30)
		#time.sleep(Duracion)
		media.stop()
		if k == len(lista["items"]):
			k = 0


