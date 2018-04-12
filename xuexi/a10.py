import json,datetime
import urllib
from urllib import request

# url='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
# response = urllib.request.urlopen(url)
# buff = response.read()
# html = buff.decode("utf8")
#
# g=open("earthquake.json","w")
# g.write(html)
fp=open("earthquake.json","r")
earthquakes=json.load(fp)

print("过去7天全球发生的重大地震信息：")
for eq in earthquakes['features']:
    print("地点：{}".format(eq['properties']['place']))
    print("震级：{}".format(eq['properties']['mag']))
    et=float(eq['properties']['time'])/1000.0
    d=datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H:%M:%S')
    print("时间：{}".format(d))
    print("详情：{}".format(eq['properties']['detail']))