

# game.py

class Board(): Game Board
 - do_move(self, move): each time do a move, find the move as a key in the dictionary states and set its value equals to current player
 - current_state(self): 4-level matrix
    - level0: current_player_moves
    - level1: current_opponent_moves
    - level2: last_moves
    - level3: all 3 are 1

class Game():
 - graphic
 - start_play
 - start_self_play

# human_play.py

class Human(object): Human player

class run(): Start game between human player and trained model
[Here we have to load the trained model by pickle]

> MAIN: run()

# mcts_alphaZero.py

class TreeNode():

class MCTS():
 - _playout(self,state): serves the get_move_probs
     - move to the leaf(): while True:...
     - if the game end:
         - expend, according to the self._policy(state)
     - else:
         - update_recursive()
 - get_move_probs(self, state, temp):
     - for n in self._n_playout: _self.playout
     - calc move probs based on the visit counts

class MCTSPlayer():
 - get_action(self, board, temp, return_prob):
     - if len(available_moves)>0:
        acts, prbs = self.mcts.get_move_probs(board, temp)
        move_probs[list(acts)] = probs


# policy_value_net_numpy
 - policy_value_fn(self, board):
    input: board
    output: a list of (action, probability) tuples for each available action and the score of the board state


# train.py
