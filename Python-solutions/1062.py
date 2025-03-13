def can_sort_with_stack(permutation, N):
  stack = []
  expected = N
  for number in reversed(permutation):
    stack.append(number)
    while stack and stack[-1] == expected:
      stack.pop()
      expected -= 1
  return 'Yes' if expected == 0 else 'No'

def main():
  while True:
    N = int(input())
    if N == 0:
      break
    while True:
      permutation = list(map(int, input().split()))
      if (permutation == [0]):
        print()
        break
      print(can_sort_with_stack(permutation, N))
      
if __name__ == '__main__':
  main()
  