import json

big_data = {}
with open("test_series.json", "r") as f:
    try:
        big_data = json.load(f)
    except:
        big_data = {}
# video_types = set()
# for key in big_data.keys():
#     data = big_data[key]
#     video_type = data["information"]["video_type"]["value"]
#     video_types.add(video_type)
# print("types", video_types)

video_types = {
    "PV",  # promotional video
    "CM",  # tv ads
    "TV Special",
    "OVA",  # original video animation straight to video
    "TV",
    "Music",
    "Movie",
    "ONA",  # original net animation straight to internet
    "Unknown",
    "Special",
}

statuses = set()
for key in big_data.keys():
    data = big_data[key]
    status = data["information"]["status"]["value"]
    statuses.add(status)
print("types", statuses)

statuses = {"Not yet aired", "Currently Airing", "Finished Airing"}
