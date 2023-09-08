from pprint import pprint

from py_youtube import Data
data = Data("https://youtube.com/watch?v=ZFSXbofgBCo").data()
pprint(data)