import requests
import glob
import config
import json
import codecs
import os.path
import jinja2
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


def _fetch_entries() -> list:
    """
    Get all entries
    """
    return [
        json.load(codecs.open(file, "r", "UTF-8"))
        for file in glob.glob(f"{config.BASE_DATA_PATH}/**/**/*")
    ]


def _generate_page(entries: list) -> None:
    """
    Organise entries per category and flavor and generate the page
    """
    organized_entries = {}
    for category in config.CATEGORIES:
        organized_entries[category["id"]] = {
            flavor["id"]: [] for flavor in config.FLAVORS
        }

    entries.sort(key=lambda a:a['release_date'])
    og_entries= entries[:5]
    for entry in entries:
        organized_entries[entry["category"]][entry["flavor"]].append(entry)

    template_loader = jinja2.FileSystemLoader(searchpath="./nanopage/templates")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("index.html")
    page_html = template.render(organized_entries=organized_entries, config=config,og_entries=og_entries)
    page_html = minify_html.minify(
        page_html, minify_js=True, remove_processing_instructions=True
    )
    with codecs.open("./public/index.html", "w", "UTF-8") as f:
        f.write(page_html)


def generate_html() -> None:
    """
    Main function to generate the page
    """
    entries = _fetch_entries()
    entries = _fetch_thumbnail(entries)
    _generate_page(entries)
