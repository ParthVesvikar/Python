def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_n():    

    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if  wall_in_front():
        move_n()
    else:
        move()
