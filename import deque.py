from collections import deque


deque = deque([",meja","sofa","lemari ","sapu","wastafel"])

deque.append("kursi")
print(list(deque))

deque.popleft()
print(list(deque))
