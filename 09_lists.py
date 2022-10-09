emojis = ['😎', '⚡', '🚀', '✅', '⚠️']

emojis[2] = '🚫'

print(emojis)
print(emojis[1:3])


# List comprehension

even = [x for x in range(10) if x % 2 == 0]
print(even)

power = [2**i for i in range(10)]
print(power)
