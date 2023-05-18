from flask import Flask, render_template, g
import requests
import glob
import config
import json
import codecs
import os.path
import minify_html
from pathlib import Path


def _fetch_thumbnail(entries: list) -> dict:
    """
    Check if thumbnail exists, if not download it and store it
    """
    for entry in entries:
        if entry["thumbnail"]:
            filename = entry["thumbnail"].split("/")[-1]
            filepath = config.BASE_THUMBNAIL_PATH / Path(filename)
            if not os.path.exists(filepath):
                url = entry["thumbnail"]
                r = requests.get(url, allow_redirects=True)
                open(filepath, "wb").write(r.content)
            entry["thumbnail_website"] = filename
        else:
            entry["thumbnail_website"] = config.DEFAULT_THUMBNAIL
    return entries


def _fetch_entries(is_archive:bool=False) -> list:
    """
    Get all entries
    """
    glob_target = f"{config.BASE_DATA_PATH}/**/**/*.json"
    if is_archive:
        glob_target = f"{config.BASE_DATA_PATH}/**/**/archive/*.json"
    entries = [
        json.load(codecs.open(file, "r", "UTF-8"))
        for file in glob.glob(glob_target)
    ]
    entries.sort(key=lambda a: a["release_date"], reverse=True)
    g._entries = entries
    return entries


def _get_organized_entries(entries: list) -> None:
    """
    Organise entries per category and flavor and generate the page
    """
    organized_entries = {}
    for category in config.CATEGORIES:
        organized_entries[category["id"]] = {
            flavor["id"]: [] for flavor in config.FLAVORS
        }

    for entry in entries:
        if (
            entry["category"] in organized_entries.keys()
            and entry["flavor"] in organized_entries[entry["category"]].keys()
        ):
            organized_entries[entry["category"]][entry["flavor"]].append(entry)
    return organized_entries


def _get_og_entries(entries):
    if not entries:
        return []
    return entries[:5]


def _filter_tag_from_entry(entries):
    for e in entries:
        if "tags" not in e.keys():
            continue
        e["tags"] = [t for t in e["tags"] if t in config.DISPLAY_TAGS]
    return entries


app = Flask(__name__)
with app.app_context():
    _fetch_entries()


@app.route("/")
def index():
    """
    Main function to generate the page
    """

    entries = _fetch_entries()
    entries = _fetch_thumbnail(entries)
    entries = _filter_tag_from_entry(entries)
    organized_entries = _get_organized_entries(entries)
    og_entries = _get_og_entries(entries)
    return minify_html.minify(
        render_template(
            "index.html",
            organized_entries=organized_entries,
            config=config,
            og_entries=og_entries,
        )
    )


@app.route("/archive.html")
def archive():
    """
    Main function to generate the page
    """

    entries = _fetch_entries(True)
    entries = _fetch_thumbnail(entries)
    entries = _filter_tag_from_entry(entries)
    organized_entries = _get_organized_entries(entries)
    og_entries = _get_og_entries(entries)
    return minify_html.minify(
        render_template(
            "archive.html",
            organized_entries=organized_entries,
            config=config,
            og_entries=og_entries,
        )
    )