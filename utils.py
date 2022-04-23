import json


def load_candidates_from_json(path):
    """
    Загружает список кандидатов из json файла
    :param path: json файл со списком кандидатов
    :return: Список кандидатов
    """
    with open(path, "r") as file:
        candidates_list = json.load(file)
    return candidates_list


def get_candidate(candidates, candidate_id):
    """
    Получает одного кандидата из списка по id
    :param candidates: Список кандидатов
    :param candidate_id: id кандидата
    :return: Возвращает одного кандидата
    """
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidates, candidate_name):
    """
    Получает список кандидатов по имени из общего списка
    :param candidates: Список кандидатов
    :param candidate_name: Имя кандидата
    :return: Список кандидатов по имени
    """
    candidates_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidates_by_skill(candidates, skill_name):
    """
    Получает список кандидатов по скиллу из общего списка
    :param candidates: Список кандидатов
    :param skill_name: Название скилла
    :return: Список кандидатов по скиллу
    """
    candidates_by_skill = []
    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in candidate_skills:
            candidates_by_skill.append(candidate)
    return candidates_by_skill
