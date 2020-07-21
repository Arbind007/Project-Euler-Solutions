sum = 0
for i in range(1000):
  if i % 3 == 0 or i % 5 == 0:
    sum += i
print(sum)

# Answer: 233168
# Completed on Fri, 12 Jun 2020, 16:34

# Alternate Solution:
# sol = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
# print(sol)
