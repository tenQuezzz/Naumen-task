"""
Task: https://www.codewars.com/kata/56fcc393c5957c666900024d
"""

def code(s):
  if not s:
    return ''
  n = find_n(s)
  s = insert_newline(append_chars(s, n * n), n)
  encoded = rotate(s)
  return encoded

def decode(s):
  if not s:
    return ''
  return rotate(s, order='counter-clockwise').replace('\n', '').strip()

def rotate(s, order='clockwise'):
  lines_matrix = list(map(lambda line: list(line), s.strip('\n').split('\n')))
  n = len(lines_matrix)
  result = [[0] * n for i in range(n)]
  for i in range(len(lines_matrix)):
    for j in range(len(lines_matrix[i])):
      if order == 'clockwise':
        result[j][n - i - 1] = lines_matrix[i][j]
      else:
        result[i][j] = lines_matrix[j][n - i - 1]
  return '\n'.join(word for word in [''.join(line) for line in result])

def insert_newline(s, step):
  res = ''
  for i in range(0, len(s) - step + 1, step):
    res += s[i: i + step] + '\n'
  return res

def find_n(s):
  n = 1
  while n * n < len(s):
    n += 1
  return n

def append_chars(s, length):
  while len(s) < length:
    s += chr(11)
  return s

if __name__ == '__main__':
  test = "I.was.going.fishing.that.morning.at.ten.o'clock"
  encoded = code(test)
  print(repr(encoded))
  decoded = decode(encoded)
  print(repr(decoded))
