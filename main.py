from program import helper, user, kursus, menu
import os

path = os.path.realpath(__file__)
path = path.replace("main.py", "")
path = os.path.join(path, "data")

h = helper.Helper(path)
u = user.User(h)
k = kursus.Kursus(h, u)

app = menu.Menu(h, u, k)
app.mulai()
