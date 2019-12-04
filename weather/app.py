import requests, json

url_base = "https://wis.qq.com/weather/common?source=pc&weather_type=observe\
%7Cforecast_1h%7Cforecast_24h%7Cindex%7Calarm%7Climit%7Ctips%7Crise&province={}&city={}"

def get_weather(province, city):
  url = url_base.format(province, city)
  response = requests.get(url)
  content = response.content
  content_json = json.loads(content)
  data = content_json.get('data')
  observe = data.get('observe')
  tips = data.get('tips')
  return observe, tips