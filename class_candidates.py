class Candidates:

    def __init__(self, file):
        self.file = file

    # По pk и name формата list of dict
    def load_candidates(self):
        list_candidates = []
        for i in self.file:
            dict_candidates = {x: y for x, y in i.items() if x == 'pk' or x == 'name'}
            list_candidates.append(dict_candidates)
        return list_candidates

    # Поиск по одинаковым именам
    def get_candidates_by_name(self, candidate_name):
        copy_name = [i for i in self.file if candidate_name.title() in i['name']]
        return copy_name

    # Функция вывода кандидатов по порядковому номеру
    def get_by_pk(self, pk):
        for i in self.file:
            if i["pk"] == pk:
                return i

    # Функция вывода кандидатов по навыку
    def get_by_skill(self, skill):
        _l_candidates = []
        for i in self.file:
            list_skills = i["skills"].lower().split(', ')
            if skill.lower() in list_skills:
                _l_candidates.append(i)
        return _l_candidates
