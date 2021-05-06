import xml.etree.ElementTree as ET
import os
import re

splits_files = os.listdir("./splits")
splits_names = []

for x in splits_files:
    # Get rid of non-split files
    if x[-3:] != "lss":
        splits_files.remove(x)
    # Get proper split names for automatic subsplits
    else:
        splits_names.append(re.sub(r'^.*? ', '', x)[:-4])


blank = ET.parse("blank.lss")
blank_tree = blank.getroot()
blank_tree[7].remove(blank_tree[7][0])

for x in splits_files:
    split_file_tree = ET.parse(f"./splits/{x}").getroot()

    for segment in split_file_tree[7]:
        segment.remove(segment[1])
        # Messy solution but w/e. if run hasn't finished then PB doesn't exist, this checks for that
        try:
            segment[1][0].remove(segment[1][0][0])
        except IndexError:
            pass
        if len(split_file_tree[7]) - 1 != list(split_file_tree[7]).index(segment):
            segment[0].text = "-" + segment[0].text
            blank_tree[7].append(segment)
        else:
            segment[0].text = "{" + splits_names[splits_files.index(x)] + "}" + segment[0].text
            blank_tree[7].append(segment)

blank.write("output.lss")
