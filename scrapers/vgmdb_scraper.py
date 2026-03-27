import json
import sys
import threading

import requests
from bs4 import BeautifulSoup
from vgmdb_dummy import vgmdb_album_page, vgmdb_element_product_page

product_url_start = "https://vgmdb.net/product/"
album_url_start = "https://vgmdb.net/album/"
url_start = "https://vgmdb.net/search?q="
url_end = "&type=product"
# search = "sousou"
cloudflare_bypass = "http://localhost:8191/v1"
headers = {"Content-Type": "application/json"}
url_payload = {
    "cmd": "request.get",
    "url": "",
    "maxTimeout": 60000,
}
# response = requests.post(cloudflare_bypass, headers=headers, json=data)
# soup = BeautifulSoup(response.text, "html.parser")
# products = soup.find("div", {"id": "productresults"})
# print(soup.prettify())


def write_json(data, filename):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def unique_songs(openings, endings, songs):
    known_songs = {}
    soundtracks_to_add = {}
    for song in openings:
        known_songs[song["song_name"]] = song
    for song in endings:
        known_songs[song["song_name"]] = song
    for song in songs:
        titles = song["titles"]
        found = False
        name = ""
        backup_name = ""
        for lang, title in titles.items():
            if title in known_songs:
                found = True
                break
            if lang == "English:":
                name = title
            elif lang == "Romaji" and name == "":
                name = title
            else:
                backup_name = title
        if found:
            continue
        if name == "":
            name = backup_name
        soundtracks_to_add[name] = song
    return soundtracks_to_add


def filter_soundtracks(product_page):
    soup = BeautifulSoup(product_page, "html.parser")
    discotable = soup.find("div", {"id": "discotable"})
    table = discotable.table
    tbodys = table.find_all("tbody")
    soundtracks = []
    for tbody in tbodys:
        trs = tbody.find_all("tr")
        for tr in trs:
            if not tr.has_attr("rel") or tr["rel"] == "year":
                continue
            td = tr.find_all("td")[1]
            # title = td.a["title"]
            # href = td.a["href"]
            types = td.find("span", {"class": "smallfont label"}).text
            if "soundtrack" in types.lower():
                title = td.a["title"]
                href = td.a["href"]
                soundtracks.append({"title": title, "href": href})
    return soundtracks


def find_tracks(album_page):
    soup = BeautifulSoup(album_page, "html.parser")
    innermain = soup.find("div", {"id": "innermain"})
    tracklist = innermain.find("div", {"id": "tracklist"})
    tlnav = innermain.find("ul", {"id": "tlnav", "class": "tabnav"})
    langs = []
    for li in tlnav.find_all("li"):
        lang = li.a.text.strip()
        langs.append(lang)
    # tracks = tracklist.find_all("tr", {"class": "rolebit"})
    track_tables = tracklist.find_all("table", {"class": "role"})
    tracks0 = track_tables[0].find_all("tr", {"class": "rolebit"})
    num_tracks = len(tracks0)
    songs = [{}] * (num_tracks)
    # notes = innermain.find("div", {"id": "notes"})
    for track in tracks0:
        tds = track.find_all("td")
        index = int(tds[0].span.text.strip())
        name = tds[1].text.strip()
        length = tds[2].text.strip()
        songs[index - 1] = {
            "titles": {langs[0]: name},
            "length": length,
            "index": index,
        }
    for j in range(1, len(track_tables)):
        track_table = track_tables[j]
        for tracks in track_table.find_all("tr", {"class": "rolebit"}):
            tds = tracks.find_all("td")
            index = int(tds[0].span.text.strip())
            name = tds[1].text.strip()
            songs[index - 1]["titles"][langs[j]] = name
    return songs


number_threads = int(sys.argv[1].strip())

multiple_ids = []


def main_func(key, data, results, index):
    ids = data["ids"]
    if len(ids) > 1:
        print("too many ids:", key)
        multiple_ids.append(key)
        results[index] = data
        return
    product_id = ids[0]
    url_payload["url"] = product_url_start + product_id
    response = requests.post(cloudflare_bypass, headers=headers, json=url_payload)
    # to connect
    soundtracks = filter_soundtracks(response.text)
    data["vgmdb soundtracks"] = soundtracks
    for soundtrack in soundtracks:
        link = soundtrack["href"]
        url_payload["url"] = album_url_start + link
        response = requests.post(cloudflare_bypass, headers=headers, json=url_payload)
        # to connect
        album_page = response.text
        songs = find_tracks(album_page)
        openings = data["openings"]
        endings = data["endings"]
        data["soundtracks"] = unique_songs(openings, endings, songs)


organized_data = {}
with open("test_series_with_id.json", "r") as f:
    try:
        organized_data = json.load(f)
    except:
        organized_data = {}
i = 0
max_i = len(organized_data)
keys = list(organized_data.keys())
while i < max_i:
    threads = []
    updated = []
    results = [{}] * number_threads
    if i + number_threads > max_i:
        number_threads = max_i - i
    for j in range(number_threads):
        key = keys[i + j]
        threads[j] = threading.Thread(
            target=main_func, args=(key, organized_data[key], results, j)
        )
        threads[j].start()
        updated.append(key)

    for j in range(number_threads):
        threads[j].join()
        organized_data[updated[j]] = results[j]

    i += number_threads
