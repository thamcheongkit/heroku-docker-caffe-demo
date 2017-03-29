import time

from gevent import monkey; monkey.patch_all()
import bottle

from bottle import response

import caffe
import numpy as np
from json import dumps
import os
import optparse

DEPLOY_FILE = 'deploy.prototxt'
MODEL_FILE = 'finetune_flickr_style.caffemodel'

# load caffe_net
net = caffe.Classifier(
  DEPLOY_FILE,
  MODEL_FILE,
  channel_swap=(2, 1, 0), input_scale=255
)

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
    if bottle.request.method != 'OPTIONS':
      # actual request; reply with the actual response
      return fn(*args, **kwargs)
  return _enable_cors

@bottle.route('/classify', method=['POST', 'OPTIONS'])
@enable_cors
def classify():
  json_request = bottle.request.json
  img_urls = json_request['urls']
  preds = [extract(img_url) for img_url in img_urls]

  json_response = {'predictions': preds}
  return dumps(json_response)


def extract(img_url):
  return net.predict([caffe.io.load_image(img_url)]).argmax()

def main():
  """
  Parse command line options and start the serverself.
  """
  parser = optparse.OptionParser()
  parser.add_option(
    '-d', '--debug',
    help="enable debug mode",
    action="store_true", default=False)

  opts, args = parser.parse_args()

  if opts.debug:
    bottle.run(port=8080, server="gevent", debug=True, reloader=True, host='0.0.0.0')
  else:
    bottle.run(port=int(os.environ.get("PORT", 5000)), server="gevent", host='0.0.0.0')


if __name__ == '__main__':
  main()
