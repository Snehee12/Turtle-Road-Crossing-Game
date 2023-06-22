import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1=Player()
cars=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player1.move_turtle,"Up")

# writing next level 
write_level=Turtle()
write_level.hideturtle()
write_level.color()
for_time_2sec=2


sleep_time=0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    
    cars.create_cars()
    cars.move_cars()
    
    # detecting car collision 
    for present_car in cars.all_cars:
        if player1.distance(present_car)<20:
            game_is_on=False
            scoreboard.game_over()

    # detecting crossing the finish line 
    if player1.is_at_finishLine():
        sleep_time*=0.9
        scoreboard.increment_score()
        
            
        



screen.exitonclick()