from calendar import c
# 掛け算耐性
import functools
import operator

def foo(num):
  count = 0
  while True:
    lst = [int(i) for i in list(str(num))]
    if len(lst) == 1:
      return count
    num = functools.reduce(operator.mul, lst)
    count += 1

if __name__ == '__main__':
  print(len([i for i in range(1000001) if foo(i) == 6]))