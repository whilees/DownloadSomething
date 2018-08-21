# -*- coding: utf-8 -*-  
import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
#
# from openpyxl import Workbook
#
class Ziroom(object):

	""" docstring for ClassName
	accessing url and save xls files what u need
	"""
	def __init__(self, header):
		pass
		#super(ClassName, self).__init__()
		self.opener = self.getOpener(header)
		self.idf = 0
		# self.url = kwarg['url']
		# self.post = kwarg['post']
		# self.filename = kwarg['filename']

	def getUrllist(self,url,post):
		file = self.access(url,post)
		data = str(file['data'])
		urllist = re.findall(r"/configuration/supplierDispatchOrderCheckOnline!detail.action\?orderId=(.+?)\"",data)
		print(urllist,len(urllist))
		return urllist

	def DownloadFiles(self,url,post,local):
		urllist = self.getUrllist(url,post)
		for id in urllist:
			url = "http://vendor.ziroom.com/configuration/supplierDispatchOrderCheckOnline!export.action?orderId=" + id
			self.DownloadFile(url,local)
			self.idf = self.idf+1
			print(self.idf)

	"""
		url- is source
		filename- is local station where u want to save
	"""
	def DownloadFile(self,url,local):
		file = self.access(url)
		filename = local + str(self.idf)+'-' + file['filename']
		savefile = open(filename, 'wb')
		savefile.write(file['data'])
		savefile.close()

	"""
		to get shortname
	"""
	def getbasename(self,filename):
		pattern = r'filename=\"(.*)\"'
		basename = re.findall(pattern,filename)
		return basename[0]

	def access(self,url,post={}):
		html = self.opener.open(url,self.CreatePost(post))
		#print(html.headers['Content-Disposition'])
		try:
			filename = html.headers['Content-Disposition']
			basename = self.getbasename(filename)
		except:
			basename = ''
		data = self.ungzip(html.read())
		file = {
			'filename':basename,
			'data':data
		}
		return file
		
	def CreatePost(self,post):
		return urllib.parse.urlencode(post).encode()

	def ungzip(self,data):
	    try:        # 尝试解压
	        #print('正在解压.....')
	        data = gzip.decompress(data)
	        #print('解压完毕!')
	    except:
	        pass
	        #print('未经压缩, 无需解压')
	    return data

	def getOpener(self,head):
	    # deal with the Cookies
	    cj = http.cookiejar.CookieJar()
	    pro = urllib.request.HTTPCookieProcessor(cj)
	    opener = urllib.request.build_opener(pro)
	    header = []
	    for key, value in head.items():
	        elem = (key, value)
	        header.append(elem)
	    opener.addheaders = header
	    return opener

	def getID(self,html):
		return re.findall(r"/configuration/supplierDispatchOrderCheckOnline!detail.action\?orderId=(.+?)\"",html)