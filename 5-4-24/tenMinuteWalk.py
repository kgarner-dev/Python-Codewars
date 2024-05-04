def is_valid_walk(walk):
    x = 0
    y = 0
    
    for direction in walk:
        if direction == 'n':
            y += 1
        if direction == 's':
            y -= 1
        if direction == 'e':
            x += 1
        if direction == 'w':
            x -= 1
            
    if x == 0 and y == 0 and len(walk) == 10:
        return True
    else:
        return False