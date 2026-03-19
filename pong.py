import pgzrun

WIDTH = 600
HEIGHT = 400

# Where Actors Are Made
paddle_left = Rect((30, HEIGHT // 2 - 30, 10, 60))
paddle_right = Rect((WIDTH - 40, HEIGHT // 2 - 30, 10, 60))
ball = Rect((WIDTH // 2, HEIGHT // 2, 10, 10))
ball_vel = [5, 5]  

wkey = Actor('wkey')
wkey.x = 100
wkey.y = 100

skey = Actor('skey')
skey.x = 100
skey.y = 300

upkey = Actor('upkey')
upkey.x = 500
upkey.y = 100

downkey = Actor('downkey')
downkey.x = 500
downkey.y = 300


bouncyball = Rect((150, 100, 50, 50))       
bouncyball2 = Rect((275, 175, 50, 50))      
bouncyball3 = Rect((400, 266, 50, 50))      
score = 0
score1 = 0

#Game Start Waiting

game_started = False

show_wkey = True

# Starts Game

def start_game():
    global game_started
    game_started = True

# Hides all keyboard icons
def hide_wkey():
    global show_wkey
    global show_skey
    global show_upkey
    global show_downkey
    show_wkey = False
    show_skey = False
    show_upkey = False
    show_downkey = False 

# Clock

clock.schedule_unique(start_game, 3.0)

clock.schedule_unique(hide_wkey, 10.0)

# Main Code

def update():
    global score
    global score1
    global game_started 

    if keyboard.w and paddle_left.top > 0:
        paddle_left.y -= 5
    if keyboard.s and paddle_left.bottom < HEIGHT:
        paddle_left.y += 5
    if keyboard.up and paddle_right.top > 0:
        paddle_right.y -= 5
    if keyboard.down and paddle_right.bottom < HEIGHT:
        paddle_right.y += 5

    if not game_started:
        return 

    ball.x += ball_vel[0]
    ball.y += ball_vel[1]
   
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
        sounds.pong.play()
    
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_vel[0] = -ball_vel[0]
        sounds.pong.play()
    
    if ball.left < 0:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_vel[0] = -ball_vel[0]  
        score = 0
        
    if ball.right > WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_vel[0] = -ball_vel[0]  
        score1 = 0
    
    if ball.colliderect(bouncyball) or ball.colliderect(bouncyball2) or ball.colliderect(bouncyball3):
        ball_vel[0] = -ball_vel[0]
   
    if ball.colliderect(paddle_left):
        score = score + 1

    if ball.colliderect(paddle_right):
        score1 = score1 + 1
# Drawings

def draw():
    screen.clear()
    
    screen.draw.filled_rect(paddle_left, "white")
    screen.draw.filled_rect(paddle_right, "white")
    screen.draw.filled_rect(ball, "white")

    
    if show_wkey:
        wkey.draw()
        skey.draw()
        upkey.draw()
        downkey.draw()

    
    
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)
    screen.draw.text('Score: ' + str(score1), (500,10), color=(255,255,255), fontsize=30)
    
    screen.draw.filled_rect(bouncyball, "green")
    screen.draw.filled_rect(bouncyball2, "yellow")
    screen.draw.filled_rect(bouncyball3, "red")

    if not game_started:
        screen.draw.text("GET READY!", center=(WIDTH // 2, HEIGHT // 4), color="orange", fontsize=50)
# Game Starts

pgzrun.go()
