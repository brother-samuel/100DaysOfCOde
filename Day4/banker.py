import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Variant 1
roulette = random.randint(0,4)
payer = friends[roulette]
print(f"Today\'s bill is covered by {payer}.")

# Variant 2
print(f"Today\'s bill is covered by {random.choice(friends)}.")

