from requests_html import HTMLSession
# import json
import codecs
import webbrowser

news = []

page = 1
while page <= 2:
	session = HTMLSession()
	r = session.get('https://shazoo.ru/tags/419?page=' + str(page))

	news_post = r.html.find('.flex.flex-col.gap-2.py-6')
	news_date = r.html.find('.flex.flex-col.gap-2.py-6 > .flex.items-center.gap-2 > time')
	news_header = r.html.find('.flex.flex-col.gap-2.py-6 > h4 > a')
	news_img = r.html.find('.flex.flex-col.gap-2.py-6 > .flex-shrink-0 > a > img')
	news_desc = r.html.find('.flex.flex-col.gap-2.py-6 > .break-words')

	i = 0
	while i < len(news_post):
		temp = {
				"header" : news_header[i].text,
				"date" : news_date[i].text,
				"link" : news_header[i].attrs["href"],
				"img" : news_img[i].attrs["src"],
				"desc" : news_desc[i].text
		}

		# json_temp = json.dumps(temp, indent = 2)
		# news.append(json_temp)
		# news.append('"p' + str(i) + '"' + " : " + temp)
		
		news.append(temp)
		i+=1
		
	page+=1

# news_out = '\n'.join(news)
# news_out = json.dumps(news, indent = 2)

# file operations
file = codecs.open('pars_result.js', 'w', 'utf-8')
file.write("let post = " + str(news))
file.close()

url = "index.html"
webbrowser.open_new_tab(url)