from pprint import pprint

from py_youtube import Search
videos = Search("CHAINETVL-TVLibertes", limit = 6).videos()
pprint(videos)