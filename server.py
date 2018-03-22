"""
This is a proxy server to use with my local Prometheus scrape target.

This is needed to target a specific Cloudflare POP and require "special"
network configuration / privilege that is, unfortunately, unavailable to
the public.

ONLY ON MY MACHINE, connecting to nrt.pop for example will connect to a Cloudflare
machine in NRT pop.
"""

import requests
from flask import Flask

PROBE_URL = 'http://{}.pop/worker/http_prober'
app = Flask(__name__)


@app.route('/probe/<colo>/<path:target>')
def probe(colo, target):
    url = PROBE_URL.format(colo)
    resp = requests.get(url,
                        headers={'Host': 'thisisbinh.me'},
                        params={'module': 'http_get_2xx', 'target': target})
    return resp.text
