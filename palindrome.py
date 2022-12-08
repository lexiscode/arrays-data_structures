'''
Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

"A palindrome is a string that reads the same forward and backward. For example, radar or madam.
'''

def palindrome(string):
  # the whole string is reverse (step is -1)
  # if string is palindrome, return True, else False
  if string == string[::-1]:
    return True
  else:
    return False


if __name__ == '__main__':
  print(palindrome('radar'))
  print(palindrome('madam'))
  print(palindrome('car'))
