# Импорт
from flask import Flask, render_template

from class_candidates import *
from functions import load_candidates, back_home

# Сделал экземпляр класса. Подробнее в class_candidates.py
candidates = Candidates(load_candidates())

app = Flask(__name__)


# Главный роут
@app.route("/")
def main_page():
    candidates_main = candidates.load_candidates()
    return render_template("list_main_page.html", candidates_list=candidates_main)


# Добавил ссылки "На главную" через back_home()
@app.route("/candidate/<int:uid>")
def canditates(uid):
    candidate_card = candidates.get_by_pk(uid)
    return render_template("card.html", candidate_dict=candidate_card) + back_home()


@app.route("/search/<name>")
def search_name(name):
    names = candidates.get_candidates_by_name(name)
    return render_template("search.html", names=names) + back_home()


@app.route("/skills/<uid>")
def skills(uid):
    candidate_with_skills = candidates.get_by_skill(uid)
    return render_template("skill.html", candidate_with_skills=candidate_with_skills, skill=uid) + back_home()


# Порт иногда забивает. Если не работает, то поменяйте номер порта
if __name__ == '__main__':
    app.run(host='127.0.0.3', port=7000, debug=True)
