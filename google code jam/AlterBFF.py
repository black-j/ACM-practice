import itertools
# The F parameter is the list of BFF identifiers, but 0-based (subtracting 1 from the input).
open_file = open(input())
num_test = int(open_file.readline())

def store(open_file,friend_list):
    num = int(open_file.readline().strip())
    for i in open_file.readline().strip().split():
        friend_list.append(int(i)-1)

def cc(F):
  n = len(F)
  r = 0
  # Iterate over all possible orderings of the n kids.
  for O in itertools.permutations(range(n)):
    first = O[0]
    second = O[1]
    for i in range(1, n):  # Iterate over the permutation, skipping the first.
      # Check if i can be the last one by checking it and the first.
      prev = O[i - 1]
      cur = O[i]
      if ((F[cur] == first or F[cur] == prev) and
          (F[first] == cur or F[first] == second)):
        r = max(r, i + 1)
      # Check if i can be in the middle, and stop if it can't.
      if F[cur] != prev and (i == n - 1 or F[cur] != O[i + 1]):
        break
  return r

if __name__ == '__main__':
    for _ in range(num_test):
        largest = 1
        friend_list = []
        store(open_file,friend_list)
        largest = cc(friend_list)
        print("Case #" + str(_+1)+ ': ' + str(largest))
    open_file.close()
