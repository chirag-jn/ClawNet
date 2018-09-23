from flask import Flask
from flask import request
from flask_cors import CORS,cross_origin

import urllib2
from bs4 import BeautifulSoup
import json
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def postdata():
    webpage = request.args.get('url')
    location = request.args.get('loc')
    
    #web_page = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xoxhorn.TRS0&_nkw=nintendo+switch&_sacat=0&LH_TitleDesc=0&_sop=16&_osacat=0&_odkw=rhino+horn&LH_TitleDesc=0'
	page = urllib2.urlopen(web_page)
	soup = BeautifulSoup(page, 'html.parser')
	text = soup.get_text()
	Keywords = {'Ox horn','Oxhorn','Ox Horn','Blogger','Ancient'}
	allstringlist = []
	totalcharacters = len(text)

	search_term = web_page[web_page.find("_nkw=")+5:web_page.find("&",web_page.find("_nkw="))]
	search_term.replace("+"," ")
	print(search_term)
	ebay_api(search_term)

	#for vid in soup.findAll(attrs={'class':'lvprice prc'}):
	#	print(vid)
	for word in Keywords:
		tfue = 1	
		start = 0
		while tfue==1:
			try:
				x = text.find(word,start)
				if x==-1:
					tfue = 0
				else:
					#print(word," ",flag)
					previndex = text.find('hipping', x-30) + 7
					finalindex = text.find('$',x) 
					#print(previndex, " " ,finalindex)
					newstr = text[previndex:finalindex]
					#newstr1 = text[previndex: previndex+10]
					#newstr2 = text[finalindex-10:finalindex]
					#print(newstr)
					
					if newstr.find('%')!=-1:
						ty = newstr.find('%')
						newstr = newstr[ty+1:]
					if newstr.find('off')!=-1:
						ty = newstr.find('off')
						newstr = newstr[ty+3:]	

					if newstr not in allstringlist:
						allstringlist.append(newstr)
					start = finalindex +10
					#print(newstr1)
					#print(newstr2)
			except Exception as e:
				print(e)

     return location


def ebay_api(search):
	try:
		api = Connection(appid='nyetmoi-zooccs-PRD-ef8fc7c73-6322fe73', config_file=None)
		response = api.execute('findItemsAdvanced', {'keywords': search})
		items = response.reply.searchResult.item
		avg = 0
		cost = 0
		urls = []
		flagged =[]
		for i in range(len(items)):
			cost += float(items[i].sellingStatus.currentPrice.value)
			urls.append(items[i].viewItemURL)
		avg = float(cost)/len(items)	
		print len(items)
		signed_variances = []
		for i in range(len(items)):
			signed_variances.append(float(items[i].sellingStatus.currentPrice.value)-avg)
		#signed_variances.sort()
		second_avg = sum(signed_variances)/len(items)
		signed_second_variances = []
		for i in range(len(items)):
			signed_second_variances.append(((signed_variances[i]-second_avg)/avg))
			if (signed_second_variances[-1]>7.5):
				flagged.append(items[i])
		signed_second_variances.sort()
		print len(flagged)
		#print signed_second_variances
		return flagged


	except ConnectionError as e:
	    print e
	    print e.response.dict()
	

if __name__ == "__main__":

    app.run(debug=True, threaded=True, port=8000)

#http://localhost:8000/?url=abc&loc=def