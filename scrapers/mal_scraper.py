import json
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

# url = "https://myanimelist.net/topanime.php?limit=0"
# response = requests.get(url)
# # print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")
# soup = soup.find_all("tr", {"class": "ranking-list"})
# # print(soup.prettify())
# links = []
# for entry in soup:
#     tag = entry.find_all("a", {"class": "hoverinfo_trigger fl-l ml12 mr8"})
#     link = tag[0]["href"]
#     links.append(link)
#
# # for link in links:
# #     response = requests.get(link)
# response = requests.get(links[0])


def write_csv(data):
    df = pd.DataFrame.from_dict(data, orient="index")
    df.to_csv("test.csv", index=False)


write = 2


def write_json(data):
    with open("test5.json", "w") as outfile:
        json.dump(data, outfile)


def get_songs(trs):
    songs = []
    for tr in trs:
        if (
            tr.has_attr("class")
            and len(tr.get("class")) > 0
            and tr.get("class")[0] == "hide"
        ):
            break
        tds = tr.find_all("td")
        if len(tds) < 2:
            return songs
        song_info = tds[1]
        song_text = song_info.text.strip()
        song_index_end = song_text.find(":")
        first_quote = song_text.find('"')
        song_name_end = song_text.find('"', first_quote + 1)
        artist_start = song_text.find("by", song_name_end + 1) + 3
        artist_end = song_text.rfind("(")
        if artist_end == -1:
            artist = song_text[artist_start:].strip()
            episodes = ""
        else:
            episodes = song_text[artist_end:].strip()
            artist = song_text[artist_start:artist_end].strip()
        if song_index_end == -1:
            song_index = ""
            song_name = song_text[: song_name_end + 1].replace('"', "").strip()
        else:
            song_name = (
                song_text[song_index_end + 1 : song_name_end + 1]
                .replace('"', "")
                .strip()
            )
            song_index = song_text[:song_index_end].strip()
        songs.append(
            {
                "song_name": song_name,
                "artist": artist,
                "song_index": song_index,
                "episodes": episodes,
            }
        )
    return songs


def get_related_entries(page):
    related = []
    related_entries = page.find("div", {"class": "related-entries"})
    if related_entries is None:
        return related
    related_border_class = related_entries.find_all(
        "div", {"class": "entry borderClass"}
    )
    for entry in related_border_class:
        content = entry.find("div", {"class": "content"})
        if content is not None:
            relation = (
                entry.find("div", {"class": "relation"}).text.replace("\n", "").strip()
            )
            relation_words = relation.split()
            relation = " ".join(relation_words)
            title_div = entry.find("div", {"class": "title"})
            title = title_div.a.text.replace("\n", "").strip()
            title_words = title.split()
            title = " ".join(title_words)
            related.append({"relation": relation, "title": title})
    related_entries_table = related_entries.find("table", {"class": "entries-table"})
    if related_entries_table is None:
        return related
    related_et_entries = related_entries_table.find_all("tr")
    for entry in related_et_entries:
        exist = entry.find("td", {"class": "ar fw-n borderClass nowrap"})
        if exist is None:
            continue
        relation_long = exist.text
        ind = relation_long.find(":")
        relation = relation_long[:ind].strip()
        big_title_div = entry.find_all("td", {"class": "borderClass"})[1]
        title_divs = big_title_div.find_all("li")
        for title_div in title_divs:
            if (
                title_div.has_attr("class")
                and len(title_div["class"]) > 0
                and title_div["class"][0] == "hide-entry"
            ):
                continue
            title = title_div.a.text
            item_type = title_div.text[len(title) :].strip()
            related.append(
                {"relation": relation, "title": title, "item_type": item_type}
            )
    return related


def get_video_data(reponse):
    text = response.text.replace("<br>", "")
    page = BeautifulSoup(text, "html.parser")
    description = page.find("p", {"itemprop": "description"}).text
    mal_tribute = description.find("[Written by MAL Rewrite]")
    description = description[:mal_tribute]
    related = get_related_entries(page)

    leftside = page.find("div", {"class": "leftside"})
    title_start = -1
    information_start = 0
    statistics_start = 0
    statistics_end = 0
    list_leftside = list(leftside.contents)
    for i, c in enumerate(list_leftside):
        if c.name == "h2" and c.string == "Alternative Titles":
            title_start = i
            break
    for i in range(title_start, len(list_leftside)):
        c = list_leftside[i]
        if c.name == "h2" and c.string == "Information":
            information_start = i
            break
    for i in range(information_start, len(list_leftside)):
        c = list_leftside[i]
        if c.name == "h2" and c.string == "Statistics":
            statistics_start = i
            break
    for i in range(statistics_start, len(list_leftside)):
        c = list_leftside[i]
        if c.name == "h2" and c.string == "Available At":
            statistics_end = i
            break

    titles = []
    bold_title_div = page.find("h1", {"class": "title-name h1_bold_none"})
    bold_title = bold_title_div.text.strip()
    titles.append({"title": bold_title, "title_type": "Title"})
    title_info = list_leftside[title_start:information_start]
    for t_info in title_info:
        if t_info.name != "div":
            continue
        title_div = t_info
        if t_info.get("class")[0] == "js-alternative-titles":
            title_div = t_info.find("div", {"class": "spaceit_pad"})
        span = title_div.find("span", {"class": "dark_text"})
        title_type = span.text.strip()
        ind = title_div.text.find(":")
        title = title_div.text[ind + 1 :].strip()
        titles.append({"title": title, "title_type": title_type})

    information_div = list_leftside[information_start:statistics_start]
    information = {
        "video_type": {"keyword": "Type:", "value": ""},
        "episodes": {"keyword": "Episodes:", "value": ""},
        "status": {"keyword": "Status:", "value": ""},
        "aired": {"keyword": "Aired:", "value": ""},
        "premiered": {"keyword": "Premiered:", "value": ""},
        "broadcast": {"keyword": "Broadcast:", "value": ""},
        "producers": {"keyword": "Producers:", "value": []},
        "licensors": {"keyword": "Licensors:", "value": []},
        "studios": {"keyword": "Studios:", "value": []},
        "source": {"keyword": "Source:", "value": ""},
        "genres": {"keyword": "Genres:", "value": []},
        "theme": {"keyword": "Themes:", "value": ""},
        "demographic": {"keyword": "Demographic:", "value": ""},
        "duration": {"keyword": "Duration:", "value": ""},
        "rating": {"keyword": "Rating:", "value": ""},
    }
    for info in information_div:
        if info.name != "div":
            continue
        span = info.find("span", {"class": "dark_text"})
        keyword = span.text.strip()
        if keyword == information["video_type"]["keyword"]:
            if info.a is not None:
                video_type = info.a.text.strip()
                information["video_type"]["value"] = video_type
            else:
                video_type_long = info.text
                ind = video_type_long.find(":")
                video_type = video_type_long[ind + 1 :].strip()
                information["video_type"]["value"] = video_type
        elif keyword == information["episodes"]["keyword"]:
            episodes_long = info.text
            ind = episodes_long.find(":")
            episodes = episodes_long[ind + 1 :].strip()
            information["episodes"]["value"] = episodes
        elif keyword == information["status"]["keyword"]:
            status_long = info.text
            ind = status_long.find(":")
            status = status_long[ind + 1 :].strip()
            information["status"]["value"] = status
        elif keyword == information["aired"]["keyword"]:
            aired_long = info.text
            ind = aired_long.find(":")
            aired = aired_long[ind + 1 :].strip()
            information["aired"]["value"] = aired
        elif keyword == information["premiered"]["keyword"]:
            if info.a is not None:
                premiered = info.a.text.strip()
                information["premiered"]["value"] = premiered
            else:
                premiered_long = info.text
                ind = premiered_long.find(":")
                premiered = premiered_long[ind + 1 :].strip()
                information["premiered"]["value"] = premiered
        elif keyword == information["broadcast"]["keyword"]:
            broadcast_long = info.text
            ind = broadcast_long.find(":")
            broadcast = broadcast_long[ind + 1 :].strip()
            information["broadcast"]["value"] = broadcast
        elif keyword == information["producers"]["keyword"]:
            producers = []
            for producer in info.find_all("a"):
                producers.append(producer.text.strip())
            information["producers"]["value"] = producers
        elif keyword == information["licensors"]["keyword"]:
            licensors = []
            for licensor in info.find_all("a"):
                licensors.append(licensor.text.strip())
            information["licensors"]["value"] = licensors
        elif keyword == information["studios"]["keyword"]:
            studios = []
            for studio in info.find_all("a"):
                studios.append(studio.text.strip())
            information["studios"]["value"] = studios
        elif keyword == information["source"]["keyword"]:
            if info.a is not None:
                source = info.a.text.strip()
                information["source"]["value"] = source
            else:
                source_long = info.text
                ind = source_long.find(":")
                source = source_long[ind + 1 :].strip()
                information["source"]["value"] = source
        elif keyword == information["genres"]["keyword"]:
            genres = []
            for genre in info.find_all("a"):
                genres.append(genre.text.strip())
            information["genres"]["value"] = genres
        elif keyword == information["theme"]["keyword"]:
            theme = info.a.text.strip()
            information["theme"]["value"] = theme
        elif keyword == information["demographic"]["keyword"]:
            demographic = info.a.text.strip()
            information["demographic"]["value"] = demographic
        elif keyword == information["duration"]["keyword"]:
            duration_long = info.text
            ind = duration_long.find(":")
            duration = duration_long[ind + 1 :].strip()
            information["duration"]["value"] = duration
        elif keyword == information["rating"]["keyword"]:
            rating_long = info.text
            ind = rating_long.find(":")
            rating = rating_long[ind + 1 :].strip()
            information["rating"]["value"] = rating

    statistics_div = list_leftside[statistics_start:statistics_end]
    statistics = {
        "score": {"keyword": "Score:", "value": ""},
        "rank": {"keyword": "Ranked:", "value": ""},
        "popularity": {"keyword": "Popularity:", "value": ""},
        "members": {"keyword": "Members:", "value": ""},
        "favorites": {"keyword": "Favorites:", "value": ""},
    }
    for stat in statistics_div:
        if stat.name != "div":
            continue
        span = stat.find("span", {"class": "dark_text"})
        keyword = span.text.strip()
        if keyword == statistics["score"]["keyword"]:
            if stat.find("small") is not None:
                stat.find("small").extract()
            score_long = stat.text.replace("\n", "")
            ind = score_long.find(":")
            score = score_long[ind + 1 :].strip()
            statistics["score"]["value"] = score
        elif keyword == statistics["rank"]["keyword"]:
            if stat.find("small") is not None:
                stat.find("small").extract()
            rank_long = stat.text.replace("\n", "")
            ind = rank_long.find(":")
            rank = rank_long[ind + 1 :].strip()
            statistics["rank"]["value"] = rank
        elif keyword == statistics["popularity"]["keyword"]:
            if stat.find("small") is not None:
                stat.find("small").extract()
            popularity_long = stat.text.replace("\n", "")
            ind = popularity_long.find(":")
            popularity = popularity_long[ind + 1 :].strip()
            statistics["popularity"]["value"] = popularity
        elif keyword == statistics["members"]["keyword"]:
            if stat.find("small") is not None:
                stat.find("small").extract()
            members_long = stat.text.replace("\n", "")
            ind = members_long.find(":")
            members = members_long[ind + 1 :].strip()
            statistics["members"]["value"] = members
        elif keyword == statistics["favorites"]["keyword"]:
            if stat.find("small") is not None:
                stat.find("small").extract()
            favorites_long = stat.text.replace("\n", "")
            ind = favorites_long.find(":")
            favorites = favorites_long[ind + 1 :].strip()
            statistics["favorites"]["value"] = favorites
    opening_song_div = page.find(
        "div", {"class": "theme-songs js-theme-songs opnening"}
    )
    opening_tbody = opening_song_div.find("table", recursive=False)
    opening_trs = opening_tbody.find_all("tr")
    openings = get_songs(opening_trs)

    ending_song_div = page.find("div", {"class": "theme-songs js-theme-songs ending"})
    ending_tbody = ending_song_div.find("table", recursive=False)
    ending_trs = ending_tbody.find_all("tr")
    endings = get_songs(ending_trs)
    return {
        "description": description,
        "related": related,
        "titles": titles,
        "information": information,
        "statistics": statistics,
        "openings": openings,
        "endings": endings,
    }


# print(get_video_data(response))
# print("\n\n\n")
# print(list(leftside.contents)[information_start:statistics_start])
# print("\n\n\n")
# print(list(leftside.contents)[statistics_start:statistics_end])
# alternative_titles = leftside.find("h2", string="Alternative Titles").extract()
# print(alternative_titles)
# print(page.prettify())
# print(related)
# print(description)
# print("titles", titles)
# print(information)
# print(statistics)

# print(get_video_data(response))
# write_csv(get_video_data(response))
# test = "test"
# print(test.find(":"))
# big_data = []
# with open("test6.json", "r", encoding="utf-8") as f:
#     try:
#         big_data = json.load(f)
#     except:
#         big_data = []
# if not isinstance(big_data, list):
#     # If existing data is not a list, convert it
#     big_data = [big_data]
# i = 22250
# ind = 22250
# saved = 22299
# while i <= 24000:
#     try:
#         url = "https://myanimelist.net/topanime.php?type=bypopularity&limit=" + str(i)
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         entries = soup.find_all("tr", {"class": "ranking-list"})
#         links = []
#         for entry in entries:
#             tag = entry.find_all("a", {"class": "hoverinfo_trigger fl-l ml12 mr8"})
#             link = tag[0]["href"]
#             links.append(link)
#     except Exception as e:
#         print(e)
#         time.sleep(60)
#         continue
#     j = 0
#     while j < 50:
#         if ind < saved:
#             ind += 1
#             j += 1
#             continue
#         link = links[j]
#         print(saved)
#         print(link)
#         try:
#             response = requests.get(link)
#             data = get_video_data(response)
#             big_data.append(data)
#             write_json(big_data)
#         except Exception as e:
#             print(e)
#             time.sleep(60)
#             continue
#         saved += 1
#         ind += 1
#         j += 1
#     i += 50

# response = requests.get("https://myanimelist.net/anime/16397/Photokano")
# data = get_video_data(response)
# print(data)
url = "https://myanimelist.net/topanime.php?type=bypopularity&limit=" + str(1)
response = requests.get(url)
print(response.request.headers)
print(response.headers)
