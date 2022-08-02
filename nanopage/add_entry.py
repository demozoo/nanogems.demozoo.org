import requests
import json
import re
import config
import codecs
from pathlib import Path


def slugify(text: str) -> str:
    return re.sub(r"[\W_]+", "_", text.lower())


def data_from_demozoo(pid: str) -> dict:
    """
    Fetch data from demozoo api
    """
    url = f"http://demozoo.org/api/v1/productions/{pid}"
    req_dz = requests.get(url)
    data = json.loads(req_dz.content)

    if download_link := data["download_links"]:
        download_link = data["download_links"][0]["url"]

    if thumbnail := data["screenshots"]:
        thumbnail = data["screenshots"][0]["thumbnail_url"]
    return {
        "id": data["id"],
        "title": data["title"],
        "authors": ",".join(d["name"] for d in data["author_nicks"]),
        "platforms": ",".join([d["name"] for d in data["platforms"]]),
        "release_date": data["release_date"],
        "thumbnail": thumbnail or None,
        "url": data["demozoo_url"],
        "download_link": download_link or None,
        "other_links": data["external_links"],
    }


def add_entry(category: str, flavor: str, demozoo_id: str):
    """
    Create new entry on the correct category & flavor path
    """
    data = data_from_demozoo(demozoo_id)
    data["flavor"] = flavor
    data["category"] = category
    path = config.get_entry_dir_path(category, flavor)
    filename = f'{data["id"]}_{slugify(data["title"])}.json'
    filepath = path / Path(filename)
    json.dump(data, codecs.open(filepath, "w", "UTF-8"))
