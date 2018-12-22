import turtle as t
import random

### ch.1 Starting with Python ###

# pg.18 Using IDLE
# t.forward(200)
# t.left(90)
# t.forward(300)
# print('I am eleven')
# Keep Turtle window open
# t.mainloop()

# print(''.join(reversed('Time to code')))

# Turtle Challenge Round
# t.tracer(0, 0)  # speed up drawing
# t.speed('fastest')
# # loop through quadrants (starting top left and moving clockwise)
# for i in range(4):
#     # draw squares per quadrant
#     square_count = 0
#     for j in range(10):
#         square_side_length = random.randint(1, 201)
#         for k in range(4):
#             t.forward(square_side_length)
#             t.left(90)
#         square_count += 1
    
#     # draw spikes per quadrant
#     spike_count = 0
#     for l in range((i * 1)**i):
#         turn_degree = random.randint(0, 91)
#         line_length = square_side_length * random.random() * 2

#         t.left(turn_degree)
#         t.forward(line_length)
#         t.left(180)
#         t.forward(line_length)
#         t.right(turn_degree)

#         spike_count += 1

#     print('quadrant ' + str(i) + ', squares ' + str(square_count) + ', spikes ' + str(spike_count))
#     t.left(90)

# t.mainloop()

# pg.19 Using IDLE
# for counter in range(11):
#     if((counter % 2) == 0):
#         print(str(counter) + ' is even')
#     else:
#         print(str(counter) + ' is odd')

### ch.2 First Steps ###

# pg.22 Your First Program
# print('Hello World')
# person = input('What is your name? ').capitalize()
# print('Hello,', person)

# pg.24 Variables
# x = 10
# y = x * 7
# print(y)

# pg.26 Working with Strings
