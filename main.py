import falcon
import json
board = [0,0,0,0,0,0,0,0,0]
token = {u'abc' : 1, u'def' : 2}
status = 'Playing'
# 'Playing', 'Player 1 wins', 'Player 2 wins', 'Draw' 

class Resource(object):
    def on_get(self, req, resp):
        resp.body = str(board)
        map_info = {u'board' : board, u'status': status}
        resp.body = json.dumps(map_info)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        global status
        data = json.load(req.stream)     
        print repr(data)
        print repr(data['username'])
        position = int(data['number'])
        new_token = token[data['username']]

        def is_next_token(token):
            if board.count(1) == board.count(2) and token == 1:
                return True
            elif board.count(1) - board.count(2) == 1 and token == 2:
                return True
            else:
                return False

        if 9 >= position >= 1 and board[position - 1] == 0 and is_next_token(new_token) and status == 'Playing':
            board[position - 1] = token[data['username']]
            resp.body = 'OK'

            if board[0] == board[1] == board[2] or board[0] == board[3] == board[6]:
                if board[0] == 1:
                    status = 'Player 1 wins'
                if board[0] == 2:
                    status = 'Player 2 wins'
                else:
                    pass
            if board[2] == board[5] == board[8] or board[6] == board[7] == board[8]:
                if board[8] == 1:
                    status = 'Player 1 wins'
                if board[8] == 2:
                    status = 'Player 2 wins'
                else:
                    pass
            if board[3] == board[4] == board[5] or \
               board[0] == board[4] == board[8] or \
               board[2] == board[4] == board[6]:
                if board[4] == 1:
                    status = 'Player 1 wins'
                if board[4] == 2:
                    status = 'Player 2 wins'
                else:
                    pass
            elif board.count(0) == 0:
                status = 'Draw'
            else:
                pass
        else:
            resp.body = 'Fail'
        print repr(board)
        print repr(status)


r = Resource()
api = falcon.API()
api.add_route('/', r)
