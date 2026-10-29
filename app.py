from __future__ import annotations

import json
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "site_data.json"

app = Flask(__name__)
app.config["SECRET_KEY"] = "bmsit-admin-secret-key-change-me"


DEFAULT_DATA = {
    "college": {
        "name": "BMS Institute of Technology & Management",
        "short_name": "BMSIT&M",
        "location": "Bengaluru",
        "tagline": "Shaping future-ready leaders for a changing world.",
        "hero_text": "BMS Institute of Technology & Management empowers students with industry-relevant learning, global outlook, and innovation-led experiences across engineering, technology, and management.",
        "hero_badge": "A legacy of excellence since 2002",
        "about": "We combine strong fundamentals with a future-focused curriculum, ensuring students learn by doing, lead by example, and become resilient professionals who can thrive in a rapidly evolving world.",
        "address": "Doddaballapur Main Road, Yelahanka, Bengaluru, Karnataka 560064",
        "phone": "+91 80 2297 1028",
        "email": "admissions@bmsit.in",
    },
    "stats": [
        {"value": "28+", "label": "Years of academic excellence"},
        {"value": "9,000+", "label": "Students and alumni network"},
        {"value": "95%", "label": "Placement success"},
    ],
    "programs": [
        {
            "type": "UG Programs",
            "title": "B.E. in Computer Science",
            "description": "Cutting-edge software engineering, AI, data systems, and cloud technology.",
        },
        {
            "type": "UG Programs",
            "title": "B.E. in Electronics & Communication",
            "description": "Embedded systems, signal processing, robotics, and next-gen communication.",
        },
        {
            "type": "UG Programs",
            "title": "B.E. in Mechanical Engineering",
            "description": "Design thinking, smart manufacturing, and sustainable innovation.",
        },
        {
            "type": "PG Programs",
            "title": "M.Tech / MBA",
            "description": "Advanced specializations with leadership training and applied research.",
        },
    ],
    "highlights": [
        {
            "title": "Industry-integrated learning",
            "text": "Live projects, internships, and expert mentorship.",
        },
        {
            "title": "Global perspective",
            "text": "International exposure, exchange opportunities, and cultural diversity.",
        },
        {
            "title": "Career-focused outcomes",
            "text": "Strong placement assistance, entrepreneurship support, and alumni guidance.",
        },
    ],
    "news": [
        {
            "category": "Innovation",
            "title": "BMSIT&M students showcase award-winning prototype at national tech forum.",
            "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80",
        },
        {
            "category": "Campus",
            "title": "Annual cultural festival brings together innovation, creativity, and community.",
            "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80",
        },
        {
            "category": "Career",
            "title": "Industry leaders mentor students through internship pathways and placement prep.",
            "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80",
        },
    ],
    "campus_points": [
        "State-of-the-art labs and digital classrooms",
        "Student entrepreneurship and innovation center",
        "Sports, clubs, cultural initiatives, and leadership platforms",
        "Strong faculty mentorship and student support systems",
    ],
    "metrics": [
        {"value": "95%", "label": "Placement assistance and internship success"},
        {"value": "100+", "label": "Research publications and innovation projects"},
        {"value": "50+", "label": "Student clubs and technical communities"},
        {"value": "24/7", "label": "Campus support for student well-being and mentoring"},
    ],
    "admissions": {
        "title": "Start your next chapter with a community that supports your ambition.",
        "cta": "Apply for admission",
    },
}


def load_site_data() -> dict:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        save_site_data(DEFAULT_DATA)
        return DEFAULT_DATA

    with DATA_FILE.open("r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = {}

    merged = DEFAULT_DATA.copy()
    merged.update(data)
    for key in ["college", "stats", "programs", "highlights", "news", "campus_points", "metrics", "admissions"]:
        if key in data:
            merged[key] = data[key]
    return merged


def save_site_data(data: dict) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


@app.context_processor
def inject_data():
    return {"site_data": load_site_data()}


@app.route("/")
def home():
    return render_template("index.html", data=load_site_data())


@app.route("/about")
def about():
    return render_template("about.html", data=load_site_data())


@app.route("/academics")
def academics():
    return render_template("academics.html", data=load_site_data())


@app.route("/admissions")
def admissions():
    return render_template("admissions.html", data=load_site_data())


@app.route("/contact")
def contact():
    return render_template("contact.html", data=load_site_data())


@app.route("/admin", methods=["GET", "POST"])
def admin():
    data = load_site_data()

    if request.method == "POST":
        form = request.form
        data["college"]["name"] = form.get("college_name", data["college"]["name"])
        data["college"]["short_name"] = form.get("college_short_name", data["college"]["short_name"])
        data["college"]["location"] = form.get("college_location", data["college"]["location"])
        data["college"]["tagline"] = form.get("college_tagline", data["college"]["tagline"])
        data["college"]["hero_text"] = form.get("college_hero_text", data["college"]["hero_text"])
        data["college"]["hero_badge"] = form.get("college_hero_badge", data["college"]["hero_badge"])
        data["college"]["about"] = form.get("college_about", data["college"]["about"])
        data["college"]["address"] = form.get("college_address", data["college"]["address"])
        data["college"]["phone"] = form.get("college_phone", data["college"]["phone"])
        data["college"]["email"] = form.get("college_email", data["college"]["email"])

        data["stats"] = [
            {"value": form.get("stat1_value", "28+"), "label": form.get("stat1_label", "Years of academic excellence")},
            {"value": form.get("stat2_value", "9,000+"), "label": form.get("stat2_label", "Students and alumni network")},
            {"value": form.get("stat3_value", "95%"), "label": form.get("stat3_label", "Placement success")},
        ]

        data["admissions"]["title"] = form.get("admissions_title", data["admissions"]["title"])

        save_site_data(data)
        flash("Website information updated successfully.")
        return redirect(url_for("admin"))

    return render_template("admin.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
