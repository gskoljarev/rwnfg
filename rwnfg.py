#!/usr/bin/python

import iso8601
import requests
from feedgen.feed import FeedGenerator


def insert_paris_attacks_episode(fg):
    fe = fg.add_entry()
    fe.id('http://exiledonline.com/wnradio/Radio-War-Nerd-Special-Paris-Attacks.mp3')
    fe.title('Radio War Nerd, Special Episode -November 16, 2015')
    fe.description('Special edition of Radio War Nerd on the Paris ISIS attacks')
    fe.enclosure('http://exiledonline.com/wnradio/Radio-War-Nerd-Special-Paris-Attacks.mp3', 0, 'audio/mpeg')
    fe.pubdate(iso8601.parse_date('2015-11-16T12:00:00+00:00'))


fg = FeedGenerator()
fg.load_extension('podcast')
fg.podcast.itunes_category('Technology', 'Podcasting')

r = requests.get('https://api.patreon.com/campaigns/157274/posts?filter[is_by_creator]=true&page[count]=100')

patreon_posts = r.json()

entry_list = []

for post in patreon_posts['data']:
    if post['post_type'] == 'audio_file' and post['post_file']is not None:
        # insert Paris attacks special episode
        if post['published_at'] == '2015-11-15T07:06:53+00:00':
            insert_paris_attacks_episode(fg)

        fe = fg.add_entry()
        fe.id(post['post_file']['url'])
        fe.title(post['title'])
        fe.description(post['content'])
        fe.enclosure(post['post_file']['url'], 0, 'audio/mpeg')
        fe.pubdate(iso8601.parse_date(post['published_at']))

fg.title('Radio War Nerd')
fg.podcast.itunes_author('Gary Brecher')
fg.link({'href': 'https://www.patreon.com/radiowarnerd'})
fg.description("The War Nerd Podcast")
fg.logo('http://s3-us-west-1.amazonaws.com/patreon.user/n4H3wobwI3jPQ5ZY5vPlYLmFgn7NZq6K6IbNEI5DvpFYMlozBQB33OZF1kHCjk4y_large_2.jpeg')

fg.rss_str(pretty=True)
fg.rss_file('rwn.xml')
