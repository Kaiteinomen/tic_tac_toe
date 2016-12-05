import falcon
class Resource(object):
    def on_get(self, req, resp):
        resp.body = '{"message":"hello world"}'
        resp.status = falcon.HTTP_200
r = Resource()
api = falcon.API()
api.add_route('/', r)
