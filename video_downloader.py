import lxml.html
import os
import play_list

'''
:author Patrick 
'''


def parse_tree(tree_file, base_path):
    with open(tree_file, encoding="utf8") as f:
        html = f.read()
        tree = lxml.html.fromstring(html)

    _tree = tree.xpath("//body")[0]
    parse_node(_tree, (base_path,))


def uls_process(node):  # 对每个ul的attr 解析处理
    for ul_node in node.xpath("./ul"):
        attr_item = ul_node.attrib
        print(attr_item)
        if attr_item.get("status") == "skip":
            continue
        yield ul_node


def li_process(li_node, li_index, dir_path):
    li_item = li_node.attrib
    if li_item.get("status") == "skip":
        return
    playlist_attr = li_item.get("playlist")
    if playlist_attr:

        for url in play_list.site_func(li_node.text, playlist_attr):
            os.system("you-get -o {} {}".format(dir_path, url))
    else:

        os.system("you-get -o {} {}".format(dir_path, li_node.text))


def parse_node(node, prefxi):
    for ul_node in uls_process(node):
        dir_name = ul_node.get("class")
        print(prefxi, dir_name)
        dir_path = os.path.join(*prefxi, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        prefxi_list = list(prefxi)
        prefxi_list.append(dir_name)
        li_index = 1
        for li_node in ul_node.xpath("./li"):
            li_index += 1
            if li_node.xpath("./ul"):
                parse_node(li_node, tuple(prefxi_list))
            li_process(li_node, li_index, dir_path)


if __name__ == '__main__':
    parse_tree("v1.html", "E:\\my\\video")
