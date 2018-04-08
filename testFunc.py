

# test for some functions used in AG

import numpy as np

# square_state=np.zeros((3,3,3))

# print(square_state)

# ava=list(range(5 * 5))

# print(ava)

# print(set(ava))

# newset=[0,1,2,3,4,5,6]

# print(list(set(ava) - set(newset)))
# # moved = list(set(range(width * height)) - set(self.availables)))

# states={1:9,2:8,3:7,4:6}

# if len(set(states.get(i, -1) for i in range(1, 10))) == 1:
#     print wtf
# else:
#     print set(states.get(i, -1) for i in range(1, 10))

# for i in range(1,10):
#     print(states.get(i, -1))

# print max(states.items(),key=lambda act_node: act_node[0])

randomArray=np.random.rand(5)
print(randomArray)

board=[1,2,3,4,5]
action_probs = np.ones(len(board))/len(board)
print(action_probs)