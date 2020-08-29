import requests
from bs4 import BeautifulSoup
import json
# Paths

with open('ted_sites.txt', 'r') as file:
    paths = file.readlines()
aux = 0
for cont in range(len(paths)):
    # replace \n in the archive with '' to avoid errors in the link requested
    paths[cont] = paths[cont].replace('\n', '')
    # make a request
    page = requests.get(paths[cont]).content
    path = paths[cont]
    # Get the html page
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find("title")
    content = soup.find_all("p")

    # put the title in string
    title_text = []
    for char in title:
        title_text.append(char)
    # delete selected strings

    delete_title = '| TED Talk Subtitles and Transcript | TED'
    flag = False

    title_text[0] = title_text[0].replace(delete_title, "")

    filtered_title = title_text[0]

    # Get Autor and Title
    autor = ''
    title = ''
    flag = False

    # get title
    for char in range(len(filtered_title)):
        if filtered_title[char] == ':':
            flag = True
        if not flag:
            autor = autor + filtered_title[char]
        else:
            if filtered_title[char] != ':' and filtered_title[char - 1] != ':':
                title = title + filtered_title[char]

    content_body = []
    filttered_content_body = ''

    # Get the string from bs4 element in content
    for cont in range(len(content) - 2):
        flag2 = False

        for char in content[cont]:
            content_body.append(char)

    # transform bs4 element in string
    body = filttered_content_body.join(content_body)

    # remove \n and \t to be read correctly in json file
    body = body.replace('\n', '').replace('\t', '')
    doc = {
        "author": autor,
        "body": body,
        "title": title,
        "type": "video",
        "url": path
    }
    # create a json file
    file_name = 'ted_jsons/doc' + str(aux) + '.json'
    aux +=1
    print(aux)
    with open(file_name, 'w') as json_file:
     json.dump(doc, json_file)

