from utils import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidates_from_json("candidates.json")

    return render_template("index.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def candidate_profile(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    candidate = get_candidate(candidates, candidate_id)

    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidates = load_candidates_from_json("candidates.json")
    candidates_by_name = get_candidates_by_name(candidates, candidate_name)
    candidates_count = len(candidates_by_name)

    return render_template("search.html", candidates=candidates_by_name, candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def skill(skill_name):
    candidates = load_candidates_from_json("candidates.json")
    candidates_by_skill = get_candidates_by_skill(candidates, skill_name)
    candidates_count = len(candidates_by_skill)

    return render_template("skill.html", candidates=candidates_by_skill, candidates_count=candidates_count)


app.run()
