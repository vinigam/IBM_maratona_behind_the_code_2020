import requests
from bs4 import BeautifulSoup
import json
# Paths
# ted_sites.txt, olhardigital_scrap.txt starse_scrap.txt
sites = 'olhardigital_sites.txt'
with open(sites, 'r') as file:
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
    author = soup.find('span', 'meta-item meta-aut')
    title = soup.find("h1", 'mat-tit')
    content = soup.find_all("p")
    # put the title in string
    title_text = []
    author_text = []
    for char in title:
        title_text.append(char)
    for char in author:
        author_text.append(char)
    # delete selected strings

    flag = False



    filtered_title = title_text[0]
    filttered_author = author_text[0]
    # Get Author and Title
    author = ''
    title = ''

    # get title and author

    for char in range(len(filtered_title)):

        title = title + filtered_title[char]

    for char in range(len(filttered_author)):
        author = author + filttered_author[char]


    content_body = []
    filttered_content_body = ''

    # Get the string from bs4 element in content
    #    for cont in range(len(content) - 2): for ted sites
    #    for cont in range(len(content)): for olhardigital sites

    for cont in range(len(content)):
        flag2 = False

        for char in content[cont]:
            content_body.append(char)

    # transform bs4 element in string
    body = filttered_content_body.join(str(content_body))

    # remove \n and \t to be read correctly in json file

    body = body.replace('\n', '').replace('\t', '').replace("\ ", '')



    doc = {
        "author": author,
        "body": body,
        "title": title,
        "type": "article",
        "url": path
    }
    # create a json file
    file_name = 'olhardigital_jsons/doc' + str(aux) + '.json'
    aux += 1
    print(aux)
    with open(file_name, 'w') as json_file:
        json.dump(doc, json_file)

