import falcon
import json
map_start = [0,0,0,0,0,0,0,0,0]
token = {u'abc' : 1, u'def' : 2}
class Resource(object):
    def on_get(self, req, resp):
        resp.body = str(map_start)
        resp.status = falcon.HTTP_200
    def on_post(self, req, resp):
        
        data = json.load(req.stream)     
        print repr(data)
        print repr(data['username'])
        map_start[int(data['number']) - 1] = token[data['username']]
        print repr(map_start)
r = Resource()
api = falcon.API()
api.add_route('/', r)
