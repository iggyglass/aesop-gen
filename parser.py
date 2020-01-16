import json
import nltk

read_file = open("html-parse/out.json", "r")
vals = json.loads(read_file.read())
read_file.close()

data = {
    "adjectives" : [],
    "nouns" : [],
    "pronouns" : [],
    "morals" : []
}

# TODO:
#   - Put adjectives (JJ), nouns (NN), and possesive pronouns (PRP$) into different lists
#   - Serialize the data then write a generator in js or something

def remove_duplicates(a):
    return list(dict.fromkeys(a))

for val in vals:
    tags = nltk.pos_tag(nltk.word_tokenize(val["title"].lower()))
    
    try:
        data["morals"].append(val["adage"])
    except KeyError:
        pass

    for tag in tags:
        if (tag[1] == "JJ"):
            data["adjectives"].append(tag[0])
        elif (tag[1] == "NN"):
            data["nouns"].append(tag[0])
        elif (tag[1] == "PRP$"):
            data["pronouns"].append(tag[0])

data["adjectives"] = remove_duplicates(data["adjectives"])
data["nouns"] = remove_duplicates(data["nouns"])
data["pronouns"] = remove_duplicates(data["pronouns"])
data["morals"] = remove_duplicates(data["morals"])

write_file = open("data.json", "w")
write_file.write(json.dumps(data))
write_file.close()