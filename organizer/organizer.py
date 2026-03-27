import json

series_relations = ["sequel", "prequel", "summary"]
alternative_version = ["alternative version", "adaptation"]
franchise_relations = (
    series_relations
    + alternative_version
    + [
        "side story",
        "alternative setting",
        "other",
        "spin-off",
        "character",
        "full story",
        "parent story",
    ]
)
big_data = []
organized_data = {}


def write_json(data):
    with open("test_series.json", "w") as outfile:
        json.dump(data, outfile)


def related_entries_compare(entries, related_type):
    global organized_data
    keys_list = list(entries.keys())
    i = 0
    max_i = len(keys_list)
    while i < max_i:
        key = keys_list[i]
        entry = entries[key]
        title = entry["title"]
        if title in organized_data:
            data = organized_data[title]
            relateds = data[related_type]
            relateds_keys = list(relateds.keys())
            for related_key in relateds_keys:
                if related_key not in entries:
                    keys_list.append(related_key)
                    entries[related_key] = relateds[related_key]
                    max_i += 1
            if key not in relateds:
                relateds[key] = entry
        i += 1


with open("test5.json", "r") as f:
    try:
        big_data = json.load(f)
    except:
        big_data = []

for i in range(len(big_data)):
    # title =
    # for i in range(2):
    # print(big_data[i]["titles"])
    entry = big_data[i]
    titles = entry["titles"]
    entry_title = ""
    for title in titles:
        if title["title_type"] == "Title":
            entry_title = title["title"]
            break
    if entry_title == "":
        print("no title for entry: " + str(i))
        print(entry)
        break
    if entry_title in organized_data:
        continue
    related = entry["related"]
    series = {}
    # alternatives = []
    franchies = {}
    for r in related:
        # words = r.split()
        relation = r["relation"]
        relation = relation.lower()
        btitle = r["title"] + " " + relation
        for srel in series_relations:
            if srel in relation:
                # series.append(r)
                series[btitle] = r
                break
        # for arel in alternative_version:
        #     if arel in relation:
        #         alternatives.append(r)
        #         break
        franchies[btitle] = r
    related_entries_compare(series, "series")
    # related_entries_compare(alternatives, "alternatives")
    related_entries_compare(franchies, "franchises")
    entry["series"] = series
    # entry["alternatives"] = alternatives
    entry["franchises"] = franchies
    organized_data[entry_title] = entry
    print(entry_title)
    print(i)

write_json(organized_data)
print(len(organized_data))
# if title not in organized_data:
#     organized_data[title] = entry
