from turtle import *
# forward(10)
# left(90)
# right(90)
# back(10)


# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# for i in range(4):
#     forward(100)
#     left(90)
# up()
# goto(-100, 200)
# down()
# for i in range(4):
#     forward(100)
#     left(90)

# tracer(False)
# for i in range(4):
#     forward(100)
#     left(90)
# up()
# goto(-200,200)
# down()
# for i in range(4):
#     forward(100)
#     left(90)
# update()


# screensize(5000,5000)
#
# tracer(False)
# left(90)
# m = 20
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(18*m)
#     right(90)
# up()
# forward(5*m)
# right(90)
# forward(7*m)
# left(90)
# down()
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(7*m)
#     right(90)
# up()
# for x in range(0,19):
#     for y in range(0,16):
#         goto(x*m,y*m)
#         dot(3, "green")
#
# update()


from turtle import *
screensize(5000,5000)
tracer(False)
left(90)
m = 5

for i in range(9):
    forward(22*m)
    right(90)
    forward(16*m)
    right(90)

up()

forward(1*m)
right(90)
forward(1*m)
left(90)

down()

for i in range(10):
    forward(72 *m)
    right(90)
    forward(79*m)
    right(90)

up()

for x in range(0,16):
     for y in range(0,22):
         goto(x*m,y*m)
         dot(3, "green")
print((16+22)*2)







update()

done()


