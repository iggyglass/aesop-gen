import json
import xml.etree.ElementTree as ET

tree = ET.parse("source.html")

root = tree.getroot()

out = []

cur_title = None
cur_adage = None

for child in root:
    if(child.tag == "h2"):
        if(cur_title is not None):
            tmp = {
                "title": cur_title
            }

            if(cur_adage is not None):
                tmp["adage"] = cur_adage

            out.append(tmp)
            cur_adage = None

        cur_title = child.text

    elif(child.tag == "p" and "class" in child.attrib.keys() and child.attrib["class"] == "adage"):
        cur_adage = child.text

json_text = json.dumps(out)

write_file = open("out.json", "w")
write_file.write(json_text)
write_file.close()



