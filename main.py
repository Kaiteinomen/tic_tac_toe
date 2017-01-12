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
        position = int(data['number'])
        new_token = token[data['username']]

        def is_next_token(token):
            if map_start.count(1) == map_start.count(2) and token == 1:
                return True
            elif map_start.count(1) - map_start.count(2) == 1 and token == 2:
                return True
            else:
                return False

        if 9 >= position >= 1 and map_start[position - 1] == 0 and is_next_token(new_token):
            map_start[position - 1] = token[data['username']]
            resp.body = 'OK'
        else:
            resp.body = 'Fail'
        print repr(map_start)

r = Resource()
api = falcon.API()
api.add_route('/', r)
