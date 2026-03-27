import json
import sys
import threading

import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
from vgmdb_dummy import vgmdb_element

url_start = "https://vgmdb.net/search?q="
url_end = "&type=product"

cloudflare_bypass_start = "http://localhost:820"
cloudflare_bypass_end = "/v1"
headers = {"Content-Type": "application/json"}
url_payload = {
    "cmd": "request.get",
    "url": "",
    "maxTimeout": 60000,
}

BIG_KEY = 0
lock = threading.Lock()
organized_data = {}
missing = {}
passed = {}
multiple_ids = {}
with open("test_series.json", "r") as f:
    try:
        organized_data = json.load(f)
    except:
        organized_data = {}
keys = list(organized_data.keys())
# keys = ["Yamada-kun to Lv999 no Koi wo Suru"]
keys_len = len(keys)


def write_json(data, filename):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def year_in_string(string):
    start = 0
    for i, l in enumerate(string):
        if l == "(":
            start += 1
        elif start > 0 and l.isdigit():
            start += 1
        elif start > 0 and l == ")":
            start += 1
        elif start == 6:
            return True
        else:
            start = 0
    if start == 6:
        return True
    return False


def filter_soundtracks(product_page_soup, title, data):
    discotable = product_page_soup.find("div", {"id": '\\"discotable\\"'})
    soundtracks = []
    correct_page = False
    if discotable == None:
        # print("Invalid Product Page", key)
        return soundtracks, correct_page
    table = discotable.table
    if table == None:
        # print("Invalid Product Page", key)
        return soundtracks, correct_page
    titles_div = product_page_soup.find("h1", {"id": '\\"maintitle\\"'})
    title_spans = titles_div.find_all("span")
    for tspan in title_spans:
        em = tspan.find("em")
        if em != None:
            em.decompose()
        if fuzz.ratio(tspan.text.lower().strip(), title) > 90:
            correct_page = True
    tbodys = table.find_all("tbody")
    for tbody in tbodys:
        trs = tbody.find_all("tr")
        for tr in trs:
            if not tr.has_attr("rel") or tr["rel"] == '\\"year\\"':
                continue
            td = tr.find_all("td")[1]
            types = td.find_all("span", recursive=False)[1].text
            if "soundtrack" in types.lower():
                tit = td.a.find("span").text.replace('\\"', "")
                href = td.a["href"].replace('\\"', "")
                soundtracks.append({"title": tit, "href": href})
    return soundtracks, correct_page


def filter_results(search, title, data):
    soup = BeautifulSoup(search, "html.parser")
    m_id = ""
    soundtracks = []
    correct_page = False
    search_products = soup.find("div", {"id": '\\"productresults\\"'})
    # print("search_products", search_products)
    if search_products == None:
        if (
            soup.html != None
            and soup.html.head != None
            and soup.html.head.find("link") != None
        ):
            href = soup.html.head.find("link")["href"].replace('\\"', "")
            m_id = href[href.rfind("/") + 1 :]
            soundtracks, correct_page = filter_soundtracks(soup, title, data)
        if correct_page is True:
            return {}, {}, m_id, soundtracks
        return {}, {}, "", []
    table_p = search_products.find("table", {"class": '\\"results\\"'})
    if table_p is None:
        return {}, {}, m_id, soundtracks
    tbody_p = table_p.find_all("tbody")[1]
    products_s = tbody_p.find_all("tr")
    results = {}
    irrelavent_results = {}
    for prod_s in products_s:
        prod_a = prod_s.a
        href = prod_a["href"].replace('\\"', "")
        ind = href.rfind("/")
        href = href[ind + 1 :]
        span_p = prod_a.span
        span_style = span_p["style"]
        names = span_p.find_all("span", {"class": '\\"productname\\"'})
        title = names[0].text.replace('\\"', "").lower()
        if span_style != '\\"color:yellowgreen\\"':
            if title not in irrelavent_results:
                irrelavent_results[title] = {}
                irrelavent_results[title]["titles"] = {}
                irrelavent_results[title]["id"] = ""
            for n in range(len(names)):
                name = names[n]
                lang = name["lang"].replace('\\"', "")
                text = name.text.replace('\\"', "").lower().strip()
                if text not in irrelavent_results[title]["titles"]:
                    irrelavent_results[title]["titles"][text] = lang
            irrelavent_results[title]["id"] = href
        else:
            if title not in results:
                results[title] = {}
                results[title]["titles"] = {}
                results[title]["id"] = ""
            for n in range(len(names)):
                name = names[n]
                lang = name["lang"].replace('\\"', "")
                text = name.text.replace('\\"', "").lower().strip()
                if text not in results[title]["titles"]:
                    results[title]["titles"][text] = lang
            results[title]["id"] = href
    return results, irrelavent_results, m_id, soundtracks


accepted_video_types = {
    "TV Special",
    "OVA",  # original video animation straight to video
    "TV",
    "Movie",
    "ONA",  # original net animation straight to internet
    "Special",
}


def main_func(key, data, index):
    status = data["information"]["status"]["value"]
    if status == "Not yet aired":
        passed[key] = "passed"
        print("Status Skipped:", key, status)
        return
    video_type = data["information"]["video_type"]["value"]
    if video_type not in accepted_video_types:
        passed[key] = "passed"
        print("Video Type Skipped:", key, video_type)
        return
    # print("key:", key)
    data["ids"] = set()
    data["extra_ids"] = {}
    titles_section = data["titles"]
    titles = set()
    for ts in titles_section:
        title = ts["title"]
        title = title.lower().strip()
        titles.add(title)
        phrase = '"' + title + '"'
        titles.add(phrase)
    found = False
    titles_used = []
    sorted_titles = sorted(titles, key=len, reverse=True)
    for title in sorted_titles:
        if found is True:
            break
        if len(title) < 3 or "," in title:
            continue
        titles_used.append(title)
        url_payload["url"] = url_start + title + url_end
        if index < 9:
            cloudflare_bypass = (
                cloudflare_bypass_start + str(index + 1) + cloudflare_bypass_end
            )
        else:
            cloudflare_bypass = (
                cloudflare_bypass_start[:-1] + str(index + 1) + cloudflare_bypass_end
            )
        response = requests.post(cloudflare_bypass, headers=headers, json=url_payload)
        filter_res, _, m_id, soundtracks = filter_results(response.text, title, data)
        if m_id != "":
            found = True
            data["ids"].add(m_id)
            data["vgmdb soundtracks"] = soundtracks
        else:
            for res_key, res_val in filter_res.items():
                if found is True:
                    break
                res_titles = res_val["titles"]
                for res_title, res_lang in res_titles.items():
                    if res_title in titles:
                        r_ids = res_val["id"]
                        data["ids"].add(r_ids)
                        if len(data["ids"]) > 1:
                            multiple_ids[key] = list(data["ids"])
                        found = True
                        break
                if found is False:
                    for res_title, _ in res_titles.items():
                        for data_title in titles:
                            partial_ratio = fuzz.ratio(res_title, data_title)
                            if partial_ratio > 60:
                                r_ids = res_val["id"]
                                data["extra_ids"][r_ids] = res_val["titles"]
    data["ids"] = list(data["ids"])
    extra_ids = list(data["extra_ids"].keys())
    if found is False:
        print(
            "\n\n\nNo Results: ",
            "|" + key + "|",
            "\nExtra IDs: ",
            extra_ids,
            "\nTitles Used: ",
            titles_used,
            "\n\n\n",
        )
        missing[key] = "missing"
        return
    print("key: ", key, "IDs: ", data["ids"], "\nTitles Used: ", titles_used)


def run_func(index):
    global keys
    global BIG_KEY
    global organized_data
    global keys_len
    key_index = -1
    with lock:
        key_index = BIG_KEY
        BIG_KEY += 1
    while key_index < keys_len:
        key = keys[key_index]
        data = organized_data[key]
        main_func(key, data, index)
        with lock:
            key_index = BIG_KEY
            BIG_KEY += 1


number_threads = int(sys.argv[1].strip())
threads = []
for i in range(number_threads):
    threads.append(threading.Thread(target=run_func, args=(i,)))
    threads[i].start()
for j in range(number_threads):
    threads[j].join()

passed = list(passed.keys())
missing = list(missing.keys())
write_json(organized_data, "test_series_with_id.json")
write_json(missing, "test_series_missing_id.json")
write_json(passed, "test_series_skipped_id.json")
write_json(multiple_ids, "test_series_multiple_ids.json")
