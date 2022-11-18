import csv
# import json
import deepl

APIkey = "YOUR-API-KEY"

def translate(content):
    translator = deepl.Translator(APIkey)

    result = translator.translate_text(content, source_lang="DE", target_lang="FR", tag_handling="html")

    return(result)


# read CSV and create a dictionary for each line
products = {}

with open('ToBeTranslated.csv', 'r', newline='', encoding='utf-8') as csv_file:

    reader = csv.reader(csv_file, delimiter=';')

    header = next(reader)
    print(header)

    for line in reader:
        entry = [
            line[1],
            line[2],
            line[3],
            line[4],
            line[5],
            line[6],
        ]
        products[line[0]] = entry


# translate file values with DeepL translator using their API
translated = {}
singleValues = []

# read dictionaries
for keys in products.keys():
    print(keys)
    i = 0
    # read each value for each dictionary and translate it
    for values in products[keys]:
        # first value is not to be translated in my case
        # appen translation to new list and recreate the dictionary with translated values
        if i > 0 and len(values) > 0:
            ready = translate(values).text
            singleValues.append(ready)
        else:
            singleValues.append(values)
        i = i + 1

    # create new dictionary entry with the same key as before but with the translated values now
    translated[keys] = singleValues
    # reset new list for next line in file
    singleValues = []

# if you want to check the content and have it dumped in a nicer way with JSON
# json_text = json.dumps(translated, indent=4, ensure_ascii=False)
# print(json_text)



# write new CSV file with new values
with open('translations.csv', 'w', newline='', encoding='utf-8') as csv_new:
    writer = csv.writer(csv_new, delimiter=';')
    writer.writerow(header)


    for keys in translated.keys():
        lines = []
        lines.append(keys)
        for entry in translated[keys]:
            lines.append(entry)
        writer.writerow(lines)