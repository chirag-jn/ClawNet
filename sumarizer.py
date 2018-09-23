from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

'''text = """
I have begun preparing for the assignment a day in advance. The rationale behind this is to minimize the chance of inconveniencing myself or somebody else due my online unavailability through the duration of the forthcoming day. Keeping this in mind I have informed my parents, grand-parents and a few others I associate with on a day to day basis of the fact. I also rearranged my schedule such that I finish tasks having the possibility of necessitating exposure to the internet in any form the day prior to the assignment. 
I expect to find it challenging disconnecting my social ties with members of my individual social network as well as concurrently cutting out valuable information streams in the form of online news, telegram channels and blogs. 
Humans are both social and curious beings adept at adapting to change gradually not instantaneously. It would be technologically deterministic to say that disconnecting from all forms of new media for a day would lead to the challenges mentioned above, but rather the manner in which social ties are maintained and information assimilated will undergo a transformation. Since the day of the assignment would signify the nascent phase of this transformation, it will pose challenges associated with adjusting to change. Studying this budding transformation will help gain insights and experience to draw conclusions and arguments towards the end of this paper.
Consequently I would say that it would be most difficult to give up on personal messaging apps and community driven channels and forums. In light of the theory of network society, our society in recent times is becoming more and more networked. Institutions are transforming from a strict hierarchical to a more horizontal and networked form. This shift in the organization of institutions brings about a transformation in the social structures governing the individual agencies constituting it, bring more autonomy to the individual. Thus as individuals we are more networked with a greater autonomy to exercise the choice of being a partial members of several groups without having to constrain ourself to a single dense network, enabling becoming us to networked individuals. A large part of this transformation owes itself to the rise of IT as well as globalization(through global flows) in modern times. Messaging apps and public discussion forums, being a significant part of this new wave of innovation, would be difficult to suddenly disconnect owing to the large part they play in an communication.
On the flip-side to the prior discussion the easiest aspect of disconnecting will most likely be avoiding emails and Slack channels. Since to a large extent they carry unidirectional news and notifications which do not evoke the same desire to read as compared to personal messages on platforms like Whatsapp.
After disconnecting from all forms of new media, I can now compare my experience with my presumptions from the initial part of this essay. I found that it ended up being most difficult to give up technologies like Telegram, Stackoverflow, and Google Chrome(pertaining mostly to searches related to daily news) while it turned out to be quite easy disconnecting from Whatsapp, Slack and emails. Consequently the I found the most challenging aspect of disconnecting to be the lack of ease to accessing information in the form of the latest news updates as well as general queries sparked my the natural curiosity of the human mind form time to time. Conversely the easiest aspect turned out to be avoiding online message exchange be it in the form of emails and slack messages or Whatsapp messages.
The last realization(ease of avoiding using Whatsapp) was quite unexpected and surprising as I was under the notion that the lack of a means to communicate with my personal ties through my most often used medium would be quite challenging. But through the course of my disconnection I found that the use of technology in various spheres of life was not absolute. It was not the technology itself that mattered but rather the social system in which it as embedded. 
Interpersonal communication did not stop at Whatsapp and email, as I realized because while I remained disconnected from the internet, I remained in contact with my parents, grandparents and a few others, of which all of whom could be considered my strong ties, over the phone. This brought to light a few other important findings regarding the nature of the technologies in question. The online networking technologies provide affordances to enable us to maintain a large network of connections of both strong and weak ties by allowing the establishment and maintenance of a channel for connections between the agents involved. While enabling communication they themselves do not transform the nature of a tie, for transformation is the agency of the involved individuals and not the technology. 
Another key finding which dawned upon me from this entire exercise was that mobile phone were generally used to keep in touch with strong ties while online networking technologies connected me to both my strong and weak ties.Thus associating with their strong ties over a multitude of media. This is practical evidence of the validity of the theory of Media Multiplexity. By using a variety of media to communicate individuals have the autonomy of choosing which tie to maintain using which technology thus exercising greater agency in developing and maintaining there presence as partial participants in a variety of groups, clearly behaving like a networked individuals comprising a part of a societal network of networks.
Drawing from this experience I also realized the strong global flows of knowledge and media that exist as part of society as a consequence the society becoming more networked owing to globalization and growth in IT. New media has helped the near instantaneous circulation of news and information without biases, helping hasten the transformation to a networked society. Disconnecting from the internet truly highlighted this fact since though the same thing is achievable through other more primitive forms of media like televisions and newspapers, new media technologies afford data to spread and permeate geographic boundaries far more rapidly, while simultaneously retaining the capability of allowing individuals to explore specific areas of interest. 
The life as a student at IIIT Delhi can be neatly explained with the above discussion in mind. The very institution having been raised as a consequence of the growth of the IT industry as it the spread across the globe, channelizes knowledge and opportunity from across international borders. Thus providing us students a connection to the network of the outside world while exposing us to the global flows of knowledge which goes part and parcel with globalization. With the new found learnings in college we are able to widen our interest thereby participating in in variety of networked groups and actively being a part f a networked society.The opportunities afforded to us enable us to develop connections with people and place across geographies bridging distances through ties. Despite our constant interaction with technology and new media, our social ties are still developed and maintained through individual agency, while utilizing the greater autonomy afforded by new media to mediate and manage ties through personal discretion.
Disconnecting helped me look at technology from a new perspective while simultaneously gaining greater insights into their social affordances and realities. Had I to remake these technologies I would try to highlight the fact the technology is not the omnipotent and quintessential innovation it may seem to be at ties, but rather a tool at your disposal to help facilitate  
"""'''
subscription_key = "3ca06abc3220453e91c3cb580cb71e5f"

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text':text}
  ]}
headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(key_phrase_api_url , headers=headers, json=documents)
resp = response.json()
print resp
keywords = resp["documents"]
if len(keywords[0]["keyPhrases"])>10:
    arr=keywords[0]["keyPhrases"][:10]
else:
    arr=keywords[0]["keyPhrases"]

ret_arr=[]
for i in arr:
    ret_arr.append(i)


stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()

for word in ret_arr:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 2
	else:
		freqTable[word] = 2

for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)):
		summary += " " + sentence

print(summary)