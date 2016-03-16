#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp

class myapp (webapp.webApp):

	urls = {}
	seq = 0 

	head = '<html> <body>'
	foot = '</body> </html>'

	form = '<form method=POST>'
	form += 	'<input type=text name=Url value="">'
	form +=		'<input type=submit value=Submit>'
	form += '</form> '

	def URLAdded(self, URLtoshort , shortenedURL):
		out = '<h1> Your url:' + str(URLtoshort) + '  has been shortened as :' +  str(shortenedURL) + '</h1>'
		return out

	invalidURL = '<h1> Invalid URL, Please try with another one. </h1>'

	def parse(self, req) :
		aux = req.split(' ', 2) 
		method = aux[0] 
		reqURL = aux[1]
		postedURL = ""

		if (method == "POST"):
			aux = req.split('\r\n\r\n' , 2)[1]
			aux = aux.split('=' , 2)[1]
			postedURL = aux

		return (method, reqURL, postedURL)

	def process(self, parsedReq) :
		(method, reqURL , postedURL) = parsedReq

		print method
		print reqURL
		print postedURL

		if ((method == "GET") and ( reqURL == "/")):
			return ("200 OK" , self.head + self.form + self.foot)

		if (method == "GET"):
			try :
				shortUrl = int(reqURL[1:])
			except :
				return("404" , "Not Found")

			if (shortUrl in self.urls.keys()):
				print self.urls[shortUrl]
				return ("302 Found\nLocation: http://" + self.urls[shortUrl] , "" )

		if ((method == "POST") and (postedURL != "/" and postedURL != "" )) :
			self.seq += 1 
			self.urls[self.seq] = postedURL
			return ("200 OK" , self.head + self.URLAdded(postedURL , self.seq) + self.form + self.foot)
		else :
			return ("200 OK" , self.head + self.invalidURL + self.form + self.foot)

		return("404" , "Not Found")


if __name__ == "__main__":
	testWebApp = myapp("localhost", 1234)