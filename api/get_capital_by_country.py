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
      if "country" in dic:
        base_url = "https://restcountries.com/v3.1/name/"
        query_string = dic["country"]
        full_url = base_url + query_string
        response = requests.get(full_url)
        country_data = response.json()
        capital_city = country_data[0]["capital"][0]
        message = f"The capital of {query_string} is {capital_city}"
      else:
        message = "Valid country required to discover the capital city."
    except(Exception):
      message = "Valid country required to discover the capital city."

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return