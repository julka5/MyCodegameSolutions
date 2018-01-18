# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

# game loop

while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    ex = exit_pos - clone_pos

    if exit_floor == clone_floor and ex < 0 and direction == "RIGHT":
        print('BLOCK')
    elif exit_floor == clone_floor and ex > 0 and direction == "LEFT":
        print('BLOCK')
    elif clone_floor in elevators:
        ev = elevators[clone_floor] - clone_pos
        if ev < 0 and direction == "RIGHT":
            print('BLOCK')
        elif ev > 0 and direction == "LEFT":
            print('BLOCK')
        else:
            print('WAIT')
    else:
        print('WAIT')