#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""simple web server"""

from datetime import datetime
from bottle import route, run, template

@route('/')
def index():
    """index"""
    dt = datetime.now()
    time = "{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template('<b>Pi thinks the date/time is: {{t}}</b>', t=time)

def main() -> None:
    """main program"""
    index()

if __name__ == "__main__":
    main()
    run(host='0.0.0.0', port=80)
