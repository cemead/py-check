def two_teams(sailors):
    # declare empty variables
    boat1 = []
    boat2 = []
    # go through the list of sailors
    for sailor in sailors:
        #  those who are elder than 40 y.o. or younger than 20, should be on the first ship
        if sailors[sailor] < 20 or sailors[sailor] > 40:
            # add them to the first boat
            boat1.append(sailor)
        # everyone else goes on the second
        else:
            boat2.append(sailor)
    return [
            # return the results in alphabetical order
            sorted(boat1),
            sorted(boat2)
            ]

if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
