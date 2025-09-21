import turtle
import pandas
data = pandas.read_csv("81_cities.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()

screen = turtle.Screen()
screen.title("Turkey City Game")
image = "turkey_blank.gif"
score = 0

screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
# "with this code i calculated the coordinate of the cities"
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_cities = []
while len(guessed_cities) < 81:
    answer_state = screen.textinput(title=f"{len(guessed_cities)}/81 city found!",prompt = "What's another state's name").title()

    if answer_state == "Exit":
        missing_cities = []
        for city in  data["state"].values:
            if city not in guessed_cities:
                missing_cities.append(city)
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("missing_cities")
        break

    if answer_state in data["state"].values:
        score += 1
        guessed_cities.append(answer_state)
        row = data[data["state"] == answer_state]
        x = int(row["x"].iloc[0])
        y = int(row["y"].iloc[0])
        t.goto(x, y)
        t.write(f"{answer_state}", align= "center")


screen.exitonclick()