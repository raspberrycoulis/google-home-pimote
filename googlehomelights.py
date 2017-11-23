#!/usr/bin/env python

import web
import os


urls = (
    '/', 'index'
)

class index:
    def POST(self):
        data = web.data()
        if data == "lightsoff":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning lights off!'
        elif data =="lightson":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning lights on!'
        elif data =="smallon":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning small light on!'
        elif data =="smalloff":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning small light off!'
        elif data =="bigon":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning big light on!'
        elif data =="bigoff":
            os.system('curl -s "http://URL-TO-TRIGGER-ACTION/" > /dev/null')
            print 'Turning big light off!'
        else:
            print 'There seems to be a problem...'
            return 'OK'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
