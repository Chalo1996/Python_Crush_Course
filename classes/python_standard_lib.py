from collections import OrderedDict

fav_languages = OrderedDict()

fav_languages["Emmanuel"] = "Python"
fav_languages["David"] = "C++"
fav_languages["Eric"] = "Java"
fav_languages["Jen"] = "Ruby"

for k, v in fav_languages.items():
    print(k+"'s favorite language is "+v)