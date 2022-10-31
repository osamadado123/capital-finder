from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #taking query string and parsing it into a useful dictionary
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    try:
      if "capital" in dic:
        base_url = "https://restcountries.com/v3.1/capital/"
        query_string = dic["capital"]
        full_url = base_url + query_string
        response = requests.get(full_url)
        country_data = response.json()

        country = country_data[0]["name"]["common"]
        message = f"{query_string} is the capital of {country}"
      else:
        message = "Valid capital city needed to find which country the city resides."
    except(Exception):
      message = "Valid capital city needed to find which country the city resides."


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return