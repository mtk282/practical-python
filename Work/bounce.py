# bounce.py
#
# Exercise 1.5
height = 100
bounces = 1
while bounces <= 10:
    height = height * (3 / 5)
    print(bounces, height)
    bounces = bounces + 1
