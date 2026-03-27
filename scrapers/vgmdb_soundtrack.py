import ast
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://0.0.0.0:9990/productlist"



def driver_get_data(url):
    current_dir = os.getcwd()
    download_dir = os.path.join(current_dir, "downloads")
    options = webdriver.EdgeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": download_dir,  # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True,  # It will not show PDF directly in chrome
        },
    )
    driver = webdriver.Edge(options=options)
    driver.get(url)
    pre = None
    while pre is None:
        print("none", pre)
        pre = driver.find_element(By.TAG_NAME, "pre")
    return pre


info = {
    "products": [
        {
            "link": "product/14454",
            "type": "Tokusatsu/Puppetry",
            "names": {"en": "A 10TH RIDER APPEARS! KAMEN RIDER - ALL RIDERS ASSEMBLE!"},
        },
        {
            "link": "product/23821",
            "type": "Game",
            "names": {"en": "A Boy and His Blob"},
        },
        {"link": "product/21696", "type": "Franchise", "names": {"en": "A Bug's Life"}},
        {"link": "product/23627", "type": "Game", "names": {"en": "A cat never meow"}},
        {
            "link": "product/5218",
            "type": "Animation",
            "names": {"en": "A Centaur's Life"},
        },
        {
            "link": "product/1276",
            "type": "Animation",
            "names": {"en": "A Certain Magical Index"},
        },
        {
            "link": "product/1277",
            "type": "Animation",
            "names": {"en": "A Certain Magical Index II"},
        },
        {
            "link": "product/6623",
            "type": "Animation",
            "names": {"en": "A Certain Magical Index III"},
        },
        {
            "link": "product/1278",
            "type": "Animation",
            "names": {"en": "A Certain Magical Index: Miracle of Endymion"},
        },
        {
            "link": "product/7454",
            "type": "Radio & Audio Drama",
            "names": {"en": "A Certain Radio's Accelerator"},
        },
        {
            "link": "product/6788",
            "type": "Animation",
            "names": {"en": "A Certain Scientific Accelerator"},
        },
        {
            "link": "product/1279",
            "type": "Animation",
            "names": {"en": "A Certain Scientific Railgun"},
        },
        {
            "link": "product/1280",
            "type": "Animation",
            "names": {"en": "A Certain Scientific Railgun EX"},
        },
        {
            "link": "product/1522",
            "type": "Animation",
            "names": {"en": "A Certain Scientific Railgun S"},
        },
        {
            "link": "product/7664",
            "type": "Animation",
            "names": {"en": "A Certain Scientific Railgun T"},
        },
        {
            "link": "product/8094",
            "type": "Franchise",
            "names": {"en": "A Clockwork Ley-Line"},
        },
        {
            "link": "product/8093",
            "type": "Game",
            "names": {"en": "A Clockwork Ley-Line -Asagiri ni Chiru Hana-"},
        },
        {
            "link": "product/8091",
            "type": "Game",
            "names": {"en": "A Clockwork Ley-Line -Tasogaredoki no Kyoukaisen-"},
        },
        {
            "link": "product/8092",
            "type": "Game",
            "names": {"en": "A Clockwork Ley-Line -Zanei no Yoru ga Akeru Toki-"},
        },
        {
            "link": "product/22166",
            "type": "Animation",
            "names": {"en": "A Condition Called Love"},
        },
        {
            "link": "product/10218",
            "type": "Animation",
            "names": {"en": "A Couple of Cuckoos"},
        },
        {
            "link": "product/13400",
            "type": "Game",
            "names": {"en": "A Dance of Fire and Ice"},
        },
        {
            "link": "product/5667",
            "type": "Animation",
            "names": {"en": "A Dark Rabbit has Seven Lives"},
        },
        {
            "link": "product/7782",
            "type": "Animation",
            "names": {"en": "A Destructive God Sits Next to Me"},
        },
        {"link": "product/14504", "type": "Game", "names": {"en": "A Fistful of Gun"}},
        {
            "link": "product/12868",
            "type": "Animation",
            "names": {"en": "A Galaxy Next Door"},
        },
        {
            "link": "product/20882",
            "type": "Tokusatsu/Puppetry",
            "names": {"en": "A Girl of Wonder"},
        },
        {
            "link": "product/3069",
            "type": "Animation",
            "names": {"en": "A good librarian like a good shepherd"},
        },
        {"link": "product/6137", "type": "Game", "names": {"en": "A Hat in Time"}},
        {
            "link": "product/12239",
            "type": "Animation",
            "names": {
                "en": "A Herbivorous Dragon of 5,000 Years Gets Unfairly Villainized"
            },
        },
        {"link": "product/19690", "type": "Game", "names": {"en": "A Highland Song"}},
        {
            "link": "product/18651",
            "type": "Animation",
            "names": {
                "en": "A Journey Through Another World: Raising Kids While Adventuring"
            },
        },
        {"link": "product/13121", "type": "Game", "names": {"en": "A Kappa's Trail"}},
        {
            "link": "product/13051",
            "type": "Game",
            "names": {"en": "A King's Tale: Final Fantasy XV"},
        },
        {
            "link": "product/18185",
            "type": "Game",
            "names": {"en": "A Kingdom for Keflings"},
        },
        {
            "link": "product/18008",
            "type": "Game",
            "names": {"en": "a letter of challenge"},
        },
        {
            "link": "product/4494",
            "type": "Animation",
            "names": {"en": "A Little Snow Fairy Sugar"},
        },
        {
            "link": "product/23405",
            "type": "Game",
            "names": {"en": "A Little to the Left"},
        },
        {
            "link": "product/9748",
            "type": "Game",
            "names": {"en": "A love in Sacra & Scarlet"},
        },
        {
            "link": "product/2408",
            "type": "Animation",
            "names": {"en": "A Lull in the Sea"},
        },
        {
            "link": "product/15424",
            "type": "Game",
            "names": {"en": "A Maiden's woven Canvas of Love"},
        },
        {
            "link": "product/15430",
            "type": "Game",
            "names": {"en": "A Maiden's woven Canvas of Love ~Futari no Gallery~"},
        },
        {"link": "product/18143", "type": "Game", "names": {"en": "A Memoir Blue"}},
        {
            "link": "product/20795",
            "type": "Live Action",
            "names": {"en": "A Minecraft Movie"},
        },
        {
            "link": "product/7313",
            "type": "Game",
            "names": {"en": "A Nightmare on Elm Street"},
        },
        {
            "link": "product/20912",
            "type": "Animation",
            "names": {"en": "A Ninja and an Assassin Under One Roof"},
        },
        {
            "link": "product/22347",
            "type": "Animation",
            "names": {"en": "A Nobody's Way Up to an Exploration Hero"},
        },
        {
            "link": "product/18009",
            "type": "Game",
            "names": {"en": "a pet shop after dark"},
        },
        {
            "link": "product/23841",
            "type": "Animation",
            "names": {"en": "a piece of PHANTASMAGORIA"},
        },
        {
            "link": "product/6053",
            "type": "Animation",
            "names": {"en": "A Place Further Than the Universe"},
        },
        {
            "link": "product/7040",
            "type": "Franchise",
            "names": {"en": "A Place Further Than the Universe"},
        },
        {
            "link": "product/7041",
            "type": "Radio & Audio Drama",
            "names": {
                "en": "A Place Further Than the Universe ~Nankyoku yori mo Samui Bangumi~"
            },
        },
        {
            "link": "product/19689",
            "type": "Franchise",
            "names": {"en": "A Plague Tale"},
        },
        {
            "link": "product/19686",
            "type": "Game",
            "names": {"en": "A Plague Tale: Innocence"},
        },
        {
            "link": "product/19688",
            "type": "Game",
            "names": {"en": "A Plague Tale: Requiem"},
        },
        {
            "link": "product/22877",
            "type": "Game",
            "names": {"en": "A Rose in the Twilight"},
        },
        {"link": "product/16043", "type": "Game", "names": {"en": "A Short Hike"}},
        {
            "link": "product/5156",
            "type": "Animation",
            "names": {"en": "A Silent Voice The Movie"},
        },
        {
            "link": "product/5484",
            "type": "Animation",
            "names": {"en": "A Sister's All You Need"},
        },
        {
            "link": "product/5485",
            "type": "Franchise",
            "names": {"en": "A Sister's All You Need"},
        },
        {"link": "product/5483", "type": "Print Publication", "names": {"en": "None"}},
        {
            "link": "product/8027",
            "type": "Game",
            "names": {"en": "a synopsis of girls who don't flatter me."},
        },
        {
            "link": "product/5481",
            "type": "Print Publication",
            "names": {"en": "A Tale of Worst One"},
        },
        {
            "link": "product/17471",
            "type": "Game",
            "names": {"en": "A Total War Saga: THRONES OF BRITANNIA"},
        },
        {
            "link": "product/17464",
            "type": "Game",
            "names": {"en": "A Total War Saga: TROY"},
        },
        {
            "link": "product/4590",
            "type": "Animation",
            "names": {"en": "A town where you live"},
        },
        {
            "link": "product/8433",
            "type": "Animation",
            "names": {"en": "A Whisker Away"},
        },
        {"link": "product/22922", "type": "Game", "names": {"en": "A Witch's Tale"}},
        {"link": "product/5220", "type": "Animation", "names": {"en": "A-Channel"}},
        {"link": "product/5222", "type": "Franchise", "names": {"en": "A-Channel"}},
        {
            "link": "product/5221",
            "type": "Animation",
            "names": {"en": "A-Channel+smile"},
        },
        {"link": "product/7338", "type": "Game", "names": {"en": "A-JAX"}},
        {
            "link": "product/20901",
            "type": "Game",
            "names": {"en": "A-Rank Thunder: Tanjouhen"},
        },
        {
            "link": "product/10347",
            "type": "Game",
            "names": {"en": "A-Train: All Aboard! Tourism"},
        },
        {"link": "product/13391", "type": "Game", "names": {"en": "A.B.Cop"}},
        {
            "link": "product/21150",
            "type": "Game",
            "names": {"en": "A.S.P.: Air Strike Patrol"},
        },
        {
            "link": "product/3958",
            "type": "Game",
            "names": {"en": "A.W. : Phoenix Festa"},
        },
        {"link": "product/7745", "type": "Animation", "names": {"en": "None"}},
        {"link": "product/7743", "type": "Franchise", "names": {"en": "A3!"}},
        {"link": "product/7744", "type": "Game", "names": {"en": "None"}},
        {"link": "product/13462", "type": "Game", "names": {"en": "Aa Harimanada"}},
        {
            "link": "product/11200",
            "type": "Game",
            "names": {"en": "Abadox: The Deadly Inner War"},
        },
        {"link": "product/17129", "type": "Game", "names": {"en": "ABaLABURN"}},
        {"link": "product/8442", "type": "Game", "names": {"en": "Abandoner"}},
        {
            "link": "product/17383",
            "type": "Game",
            "names": {"en": "ABANDONER: THE SEVERED DREAMS"},
        },
        {
            "link": "product/21152",
            "type": "Game",
            "names": {"en": "ABC Monday Night Football"},
        },
        {"link": "product/23432", "type": "Game", "names": {"en": "Abnormal Check"}},
        {"link": "product/22934", "type": "Game", "names": {"en": "Absolum"}},
        {"link": "product/3241", "type": "Animation", "names": {"en": "Absolute Duo"}},
        {"link": "product/14394", "type": "Game", "names": {"en": "Absolver"}},
        {
            "link": "product/18720",
            "type": "Game",
            "names": {"en": "Abyss: The Wraiths of Eden"},
        },
        {"link": "product/18503", "type": "Game", "names": {"en": "ABZÛ"}},
        {
            "link": "product/9222",
            "type": "Animation",
            "names": {"en": "ACCA: 13-Territory Inspection Dept."},
        },
        {
            "link": "product/9223",
            "type": "Franchise",
            "names": {"en": "ACCA: 13-Territory Inspection Dept."},
        },
        {
            "link": "product/9224",
            "type": "Animation",
            "names": {"en": "ACCA: 13-Territory Inspection Dept. - Regards"},
        },
        {
            "link": "product/19606",
            "type": "Game",
            "names": {"en": "Accel Knights: Nanji ga Tame Waga wa Ken o Toru"},
        },
        {"link": "product/2605", "type": "Animation", "names": {"en": "Accel World"}},
        {"link": "product/4100", "type": "Franchise", "names": {"en": "Accel World"}},
        {
            "link": "product/4101",
            "type": "Animation",
            "names": {"en": "Accel World INFINITE∞BURST"},
        },
        {
            "link": "product/4419",
            "type": "Game",
            "names": {"en": "Accel World VS Sword Art Online: Millennium Twilight"},
        },
    ],
    "meta": {"time": "0.13", "fetched_date": "2026-03-20T20:27"},
    "letters": [
        "#",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ],
    "pagination": {
        "last": 13,
        "current": 1,
        "link_first": "productlist/A1",
        "link_last": "productlist/A13",
        "link_next": "productlist/A2",
    },
    "link": "productlist/A1",
    "vgmdb_link": "https://vgmdb.net/db/product.php?ltr=A1&field=title&perpage=100&page=1",
}

# info = ast.literal_eval(pre.text)

pagination = info["pagination"]
products = info["products"]
vgmdb_link = info["vgmdb_link"]


for product in products:

# next_page = "http://0.0.0.0:9990/productlist/~1"
# base_next = "http://0.0.0.0:9990/"
# counter = 1
# if "link_next" in pagination:
#     next_page = base_next + pagination["link_next"]
#     counter += 1
# else:
#     if counter < pagination["last"]:
#         next_page = base_next + "productlist/~" + str(counter)
#         counter += 1
#     else:
#         next_letter = "~"
#         for l in range(len(letters)):
#             letter = letters[l]
#         # to complete
#

# print("next_page", next_page)

print("test", info["pagination"])
