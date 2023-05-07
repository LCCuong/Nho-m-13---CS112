Best_Value = -2000000
Best_x = []

def CalWeight(w, x):
  W = 0
  for i in range(len(x)):
    W += w[i]*x[i]
  return W

def CalValue(v, x):
  V = 0
  for i in range(len(x)):
    V += v[i]*x[i]
  return V

def BackTracking(n, idx, curr_x, v, w, W):
  # When find a solution
  if idx >= n:
    global Best_Value
    global Best_x
    curr_val = CalValue(v, curr_x)
    if curr_val > Best_Value:
      Best_Value = curr_val
      Best_x = curr_x
    return
  
  # BackTracking
  for i in range(2):
    temp_x = curr_x + [i]
    # If sum of weights of current x_i (i = 1..m <= n) exceed W, 
    # skip searching on that branch in the search trê
    if CalWeight(w, temp_x) <= W: # prunning the search tree to reduce Time Complexity
      BackTracking(n, idx + 1, temp_x, v, w, W)

# Solve the homework
n = 4
v = [8, 11, 6, 4]
w = [5, 7, 4, 3]
W = 14
BackTracking(4, 0, [], v, w, W)

print(Best_Value)
print(Best_x)
