angle = float(input('enter angle: '))
def equal_angle(angle):
    if angle > 0:
        angle = angle
    else:
        angle = 360 - abs(angle)
    print(int(angle))
equal_angle(angle)
