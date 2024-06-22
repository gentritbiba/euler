def main(limit):
  arr = []
  for i in range(1, limit + 1):
    for j in range(i + 1, limit + 1):
      arr.append(i/j)
  print(len(list(set(filter(lambda x: x>1/3 and x<1/2, arr)))))

main(12000)
