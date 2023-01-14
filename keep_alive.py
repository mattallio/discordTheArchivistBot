from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
  return "Hello, I'm alive"

host = os.environ['host']
port = os.environ['port']

def run():
  app.run(host=host, port=port)

def keep_alive():
  t = Thread(target=run)
  t.start()