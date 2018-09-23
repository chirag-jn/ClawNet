import urllib.request
from bs4 import BeautifulSoup

web_page = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xoxhorn.TRS0&_nkw=oxhorn&_sacat=0&LH_TitleDesc=0&_sop=16&_osacat=0&_odkw=rhino+horn&LH_TitleDesc=0'
page = urllib.request.urlopen(web_page)
soup = BeautifulSoup(page, 'html.parser')
text = soup.get_text()
Keywords = {'Ox horn','Oxhorn','Ox Horn','Blogger','Ancient'}

allstringlist = []
totalcharacters = len(text)
#print(text)
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
for i in allstringlist:
	print(i)  