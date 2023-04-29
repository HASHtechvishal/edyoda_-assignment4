#Write a Python program to square the elements of a list using map() function.

def seq_num(n):
  return n * n
num = [4, 5, 2, 9]
result = map(seq_num, num)
print("Square the elements of the list:")
print(list(result))
