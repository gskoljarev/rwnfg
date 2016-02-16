#!/usr/bin/python

import datetime
import requests
from rfeed import *

r = requests.get('https://api.patreon.com/campaigns/157274/posts?filter[is_by_creator]=true&page[count]=100')

patreon_posts =  r.json()

entry_list = []

for post in patreon_posts['data']:
    if post['post_type'] == 'audio_file':
	item = Item(
	    title = post['title'],
	    link = post['post_file']['url'], 
	    description = post['content'],
	    author = "Santiago L. Valdarrama",
	    guid = Guid(post['post_file']['url']),
	)
	entry_list.append(item)

feed = Feed(
    title = "Radio War Nerd",
    link = "http://www.example.com/rss",
    description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = entry_list
)

with open('radio_war_nerd.rss', 'w+') as the_file:
	the_file.write(feed.rss())
