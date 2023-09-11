import re

upload_date = "2023-08-16T13:57:24+00:00"
duration = "PT18H12M15S"

s = duration
pattern = '\d{2}'

matches = re.findall(pattern,s)
print(type(matches))
duration_output = '{}:{}:{}'.format(matches[0], matches[1], matches[2])
print(duration_output)
