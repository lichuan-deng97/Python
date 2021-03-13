import bs4
def get_all_item_1(html, class_name, attrs_name):
    soup = bs4.BeautifulSoup(html, "lxml")
    content_all = soup.find_all(class_=class_name)
    item_all_list = []
    for content in content_all:
        item_content = content.find_all(name=attrs_name)
        for item_all in item_content:
            item = item_all.text
            item_all_list.append(item)
    return item_all_list
