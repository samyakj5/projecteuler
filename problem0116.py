# Let n be the number of grey square tiles.
# for red tiles, we have (n - i) C (i) ways of choosing
# for each i such that i <= floor(n / 2). We can sum these ways to get
# the desired result for red. Here, i is the number of red tiles

# for green tiles, we have (n - 2i) C (i) ways of choosing
# while i <= floor(n / 3)

# for blue tiles, we have (n - 3i) C (i) ways of choosing
# while i <= floor(n / 4)

# sum all of these ways for the final answer

