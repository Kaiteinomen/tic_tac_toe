import falcon
import json
from random import shuffle
board = [0,0,0,0,0,0,0,0,0]
players = []
next_player = None
status = 'Waiting'
# 'Waiting', 'Playing', 'Player 1 wins', 'Player 2 wins', 'Draw'

class PlayerResource(object):
    def on_get(self, req, resp):
        pass

    def on_post(self, req, resp):
        global status, next_player
        data = json.load(req.stream)
        print repr(data)
        resp.body = '{}'

        if len(players) == 0:
            players.append(data['username'])
        elif len(players) == 1:
            players.append(data['username'])
            shuffle(players)
            players.insert(0, None)
            status = 'Playing'
            next_player = 1
            print players

class Resource(object):
    def on_get(self, req, resp):
        resp.body = str(board)
        map_info = {u'board' : board, u'status': status}
        resp.body = json.dumps(map_info)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        global status, next_player
        data = json.load(req.stream)     
        print repr(data)
        print repr(data['username'])
        position = int(data['number'])

        def is_next_token(next_player):
            if board.count(1) == board.count(2) and next_player == 1:
                return True
            elif board.count(1) - board.count(2) == 1 and next_player == 2:
                return True
            else:
                return False

        if 9 >= position >= 1 and board[position - 1] == 0 and is_next_token(next_player) and status == 'Playing':
            board[position - 1] = next_player
            if next_player == 1:
                next_player = 2
            else:
               next_player = 1
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
               board[1] == board[4] == board[7] or \
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
        print repr(next_player)


r = Resource()
p = PlayerResource()
api = falcon.API()
api.add_route('/', r)
api.add_route('/player', p)
