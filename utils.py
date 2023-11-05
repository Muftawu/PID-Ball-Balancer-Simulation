import random 

def random_ball_points(width, height):
    return random.randint(100, width-50), random.randint(50, height-50)

if __name__ == "__main__":
    print(random_ball_points(400, 400))

