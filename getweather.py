import requests

cityCode = "420100"

r = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?key=f4fd5b287b6d7d51a3c60fee24e42002&city={}".format(

                cityCode))

data = r.json()['lives'][0]
print(data)
print(f"city:{data['city']},weather:{data['weather']},temperature:{data['temperature']}")
print('%s %s' % (data['city'] ,data['weather']) )