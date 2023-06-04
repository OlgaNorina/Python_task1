def zeros(n):
  factorial = 1

  for i in range(1, n+1):
    factorial = factorial * i

  count = 0
  fact_str = str(factorial)
  rev_fact_str = fact_str[::-1]
  for i in rev_fact_str:
        if(i != "0"):
            break
        else:
            count += 1
  return count

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
