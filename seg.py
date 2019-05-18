from flask import Flask, render_template
app = Flask(__name__)


class Person:
    def __init__(self, name, points):
        self.name = name
        self.points = points


N_super_elite = 1000
N_elite = 750
N_pro = 500
N_member = 250
N_beginner = 0

people = [
    Person("Louie Atkins", 1150),
    Person("Cooper Chesworth", 1100),
    Person("Luke Walker", 1050),
    Person("AJ", 950),
    Person("Hamish", 900),
    Person("Elija", 800),
    Person("Riley", 700),
    Person("Sam", 650),
    Person("Roxana", 600),
    Person("Rachel", 550),
    Person("Sayed", 450),
    Person("Logan", 400),
    Person("Josh", 350),
    Person("Eric", 300),
    Person("Jacob", 200),
    Person("Jude", 150),
    Person("Luca", 100),
    Person("Chayse", 50),
]


def get_people(nmin, nmax=None):
    return sorted(filter(lambda p: p.points >= nmin and
                         (nmax is None or p.points < nmax),
                         people),
                  key=lambda p: p.points,
                  reverse=True)


@app.route('/')
def main():
    return render_template('seg.html',
                           superelite=[N_super_elite, get_people(N_super_elite)],
                           elite=[N_elite, get_people(N_elite, N_super_elite)],
                           pro=[N_pro, get_people(N_pro, N_elite)],
                           member=[N_member, get_people(N_member, N_pro)],
                           beginner=[N_beginner, get_people(N_beginner, N_member)])
