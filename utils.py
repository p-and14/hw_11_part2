import json


def load_candidates_from_json(path):
    with open(path, "r") as file:
        candidates_list = json.load(file)
    return candidates_list


def get_candidate(candidates, candidate_id):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidates, candidate_name):
    candidates_by_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidates_by_skill(candidates, skill_name):
    candidates_by_skill = []
    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in candidate_skills:
            candidates_by_skill.append(candidate)
    return candidates_by_skill
