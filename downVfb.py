import os,re,requests,wget,sys

"""
		--------------------------- PaulNgei --------------------------------------
	> python pydownloadfb.py -u URL # This will save the video in default windows download folder.
	> python pydownloadfb.py -u URL -p PATH Recomeded path to save video
"""

class Fbdownloader() :
	def __init__(self,url,path) :
		self.url = url
		self.path = path
	def downloader(self):
		p = self.path
		u = self.url
		def check_url(url):
				try:
					req = requests.get(url)
					return True
				except Exception as E :
					return False	
		def check_path(path):
			if os.path.exists(path) == True :
				return True
			if os.path.exists(path) == False :
				return False
		if check_url(u) == True and check_path(p) == True :
			choose_reslution = input("Choose Normal/HD resolution : ")
			req = requests.get(u)
			if choose_reslution == "Normal" :
				try :
					search = re.search('sd_src:".+?"',req.text)
					sd_url01 = re.sub('sd_src:','',search.group())
					sd_url = re.sub('"','',sd_url01)
					wget.download(sd_url,p)
				except Exception as Err :
				    pass
			if choose_reslution == "HD" : 
				try : 
				    search02 = re.search('hd_src:".+?"',req.text)
				    hd_url01 = re.sub('hd_src:','',search02.group())
				    hd_url = re.sub('"','',hd_url01)
				    wget.download(hd_url,p)
				except Exception as Err02 :
					search = re.search('sd_src:".+?"',req.text)
					sd_url01 = re.sub('sd_src:','',search.group())
					sd_url = re.sub('"','',sd_url01)
					wget.download(sd_url,p)
		if check_url(u) == False and check_path(p) == False or check_url(u) == False and check_path(p) == True or check_url(u) == True and check_path(p) == False :
			print('''You have Problem Check this Thinks : - Conection\n\t\t- URL\n\t\t- Saving Path\n\t\t- Check if The URL Video is Privet or Not''')
if len(sys.argv) > 1 :
	try : 
		if sys.argv[1] == '-u' and sys.argv[2] and not sys.argv[3::] :
			url = sys.argv[2]
			path = os.popen(r"echo C:\Users\%username%\Downloads").read().strip()
		elif sys.argv[1] == '-u' and sys.argv[2] and sys.argv[3] == '-p' and sys.argv[4]:
			url = sys.argv[2]
			path = sys.argv[4]
		else : 
			print("Error")
	except Exception as Err : 
		print("Please Use -u URL -p PATH")
try :
	downloader = Fbdownloader(url,path)
	downloader.downloader()
except NameError :
	pass
