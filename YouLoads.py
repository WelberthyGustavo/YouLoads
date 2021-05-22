import pytube
import time

from pathlib import Path
from tqdm import tqdm
from pytube import Playlist

#banner
def banner():
	print("""
	                   /\**/\\
	     🆈🅾🆄        ( o_o  )_)
	     🅻🅾🅰🅳🆂    ,(u  u  ,),
	     ~ by Welberthy Gustavo
	""")
	print("\n ♫ YouTube Video downloads and Playlist’s!\n")

#Insert url method
def insert():
	url = str(input("\n► Video or Playlist URL: "))
	return url


#Download video method
def download(url):
	yt = pytube.YouTube(url)
	
	try:
		print("\nDownloading video: ",yt.title)
	except:
		pass
	
	#c == Download attempts to
	c = 0
	while True:
		try:
			yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('YourVideos/')
			
			#progressbar
			for i in tqdm(range(100)):
					time.sleep(0.03)
					
			print("Completed Download!")
			break
		
		except:
			c += 1
		if c == 5:
			break

	return yt


#Playlist download method
def playlistDownload(url):
	playList = Playlist(url)
	
	try:
		print("\n Playlist Download: ",playList.title)
	except:
		pass
		
	#Create directory with Playlist name
	directT = Path('YourPlaylists/',playList.title)
	if Path.is_dir(directT):
		pass
	else:
		Path.mkdir(directT)
	
	#Start Download videos from playlist
	for video in playList.videos:
		#c == Download attempts to
		c = 0
		while True:
			time.sleep(1)
			try:
				try:
					print("\nDownloading video: ", video.title)
				except:
					pass
				video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download(directT)
				
				#progressbar
				for i in tqdm(range(100)):
					time.sleep(0.03)
				print("Completed!")
				break
			except:
				c += 1
			if c == 5:
				break

	
#Main method 
def main():
	banner()
	while True:
		link = insert()
		
		#if playlist
		if 'playlist' in link:
			
			#Create directory YourPlaylists
			directP = Path("YourPlaylists")
			if Path.is_dir(directP):
				pass
			else:
				Path.mkdir(directP)
			
			#Downloading
			try:
				playlistDownload(link)
				time.sleep(1)
				print("\n ♪ Videos saved in YourPlaylists!")
				break
			except:
				time.sleep(0.3)
				print("\nCouldn't download, check your link and try again!")
				time.sleep(2.5)
				pass
		
		#if video
		else:
			direct = Path("YourVideos")
			if Path.is_dir(direct):
				pass
			else:
				Path.mkdir(direct)
				
			try:
				download(link)
				time.sleep(1)
				print("\n ♪ Video saved in YourVideos!")
				break
			except:
				time.sleep(0.3)
				print("\nCouldn't download, check your link and try again!")
				time.sleep(2.5)
				pass
		
	time.sleep(1)
	print("\n ♪ Bye ...")



#Run it
if __name__ == '__main__':
	main()

#end
#By Welberthy Gustavo Copyright © 2021!


