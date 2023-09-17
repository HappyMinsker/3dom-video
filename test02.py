import json
from posixpath import basename, dirname
from urllib.parse import urlparse

i = """{
            "@context": "http://schema.org",
            "@type": "VideoObject",
            "name": "🗺 L’ÉCHIQUIER MONDIAL 🗺 BEN SALMANE, LE PRINCE REFORMATEUR",
            "playerType": "HTML5",
            "description": "Depuis que Mohammed ben Salmane est devenu le successeur désigné de la couronne saoudienne, il a initié une multitude de transformations tant sur le plan national qu’international. MBS a des aspiratio",
            "thumbnailUrl": "https://sp.rmbl.ws/s8/1/A/n/q/B/AnqBm.qR4e-small--LCHIQUIER-MONDIAL-BEN-SALM.jpg",
            "uploadDate": "2023-09-09T01:13:53+00:00",
            "duration": "PT00H27M51S",
            "embedUrl": "https://rumble.com/embed/v3diuwc/",
            "url": "https://rumble.com/v3g495m--lchiquier-mondial-ben-salmane-le-prince-reformateur.html",
            "interactionStatistic": {
                "@type": "InteractionCounter",
                "interactionType": {
                    "@type": "http://schema.org/WatchAction"
                },
                "userInteractionCount": 3230
            },
            "width": 1280,
            "height": 720,
            "videoQuality": "Full HD"
        }"""

js = json.loads(i)

print(js['name'])
print(js['description'])
print(js['thumbnailUrl'])
print(js['uploadDate'])
print(js['duration'])
print(js['embedUrl'])
print(js['url'])
print('*' * 60)
parse_object = urlparse(js['url'])
l_embed = basename(parse_object.path)
print(l_embed)
print('*' * 60)
# v3g495m--lchiquier-mondial-ben-salmane-le-prince-reformateur.html
print(l_embed.split('-')[0])  # OKKKKK



# v1q4yvj




