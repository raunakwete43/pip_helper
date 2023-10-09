import requests
from bs4 import BeautifulSoup

name = input("Enter the name of pip module to search: ")
name = name.replace(" ", "")
URL = f"https://pypi.org/search/?q={name}&o="
request = requests.get(url=URL)

soup = BeautifulSoup(request.content, "html.parser")

pages = soup.find("strong")
try:
    no_of_searches = int(pages.text)
except ValueError:
    no_of_searches = 40
    
if no_of_searches > 40:
    no_of_searches = 40
    
no_of_pages = ((no_of_searches) // 20) + 2

title = []
version = []
description = []
package_data = {}
for page in range(1, no_of_pages):
    URL = f"https://pypi.org/search/?o=&q={name}&page={page}"
    new_request = requests.get(url=URL)
    new_soup = BeautifulSoup(new_request.content, "html.parser")
    
    # Parse data from the current page
    names = new_soup.find_all("span", attrs={"class": "package-snippet__name"})
    vers = new_soup.find_all("span", attrs={"class": "package-snippet__version"})
    des = new_soup.find_all("p", attrs={"class": "package-snippet__description"})
    
    # Check if the lists have the same length after appending
    if len(names) == len(vers) == len(des):
        title += [name.text for name in names]
        version += [ver.text for ver in vers]
        description += [descr.text for descr in des]
    else:
        print(f"Warning: Inconsistent data on page {page}")


for index, (pkg_title, pkg_version, pkg_description) in reversed(list(enumerate(zip(title, version, description), start=1))):
    print(f"{index}. Name: {pkg_title}")
    print(f"   Version: {pkg_version}")
    print(f"   Description: {pkg_description}\n")

index = int(input("Select the package to install: "))
command = f"pip install {title[index - 1]}"
print(command)
