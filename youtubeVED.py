from pafy import new
from pafy.backend_internal import get_video_info
import youtube_dl
import requests
import time
r = requests.session()
import os
os.system("rm -rf youtubeVED.py ;clear ;figlet Video Downloader")
time.sleep(1.2)
filza = 1

print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print(' ')



if filza == 1:
	url = input(' Video Link You Want To Download IT  :  ')
	
	try:
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	
		vedio = new(url)
		
		vedi = vedio.getbest()
		
		vedi.download()
		
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
		print("        \nDone Vedio ..")
	
	except ValueError:
		print(' Error Url ..!')
	
	except OSError:
		print(' Error Url ..!')
		
	except:
		print(' Error url ..!')
elif filza == '2356457':
	url2 = input('[1] Enter URL Vedio --> :\n')

	url3 = input('[2] Enter URL Vedio --> :\n')
	url4 = input('[3] Enter URL Vedio --> :\n')
	url5 = input('[4] Enter URL Vedio --> :\n')
	print('+++++++++++++++++++++++++\n')
	
	try:
	
		vedio2 = new(url2)
		
		vedi2 = vedio2.getbest()
		
		vedi2.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error Url ..!')
	
	except OSError:
		print(' Error Url ..!')
		
	except:
		print(' Error Url ..!') 
	
	
	
	
	try:
		
		vedio3 = new(url3)
		
		vedi3 = vedio3.getbest()
		
		vedi3.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error Url ..!')
	
	except OSError:
		print(' Error Url ..!')
		
	except:
		print(' Error Url ..!') 
	
	
	
	try:
		
		vedio4 = new(url4)
		
		vedi4 = vedio4.getbest()
		
		vedi4.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
	except ValueError:
		print(' Error Url ..!')
	
	except OSError:
		print(' Error Url ..!')
		
	except:
		print(' Error Url ..!') 
		
	
	
	
	try:
		vedio5 = new(url5)
		
		vedi5 = vedio5.getbest()
		
		vedi5.download()
		print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
		
		print("        \nDone Vedio ..")
	
	except ValueError:
		print(' Error Url ..!')
	
	except OSError:
		print(' Error Url ..!')
		
	except:
		print(' Error Url ..!') 




else:
	print('             [ Error ..! ]')
