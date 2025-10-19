from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type == TextType.plain:
            temp_list = []
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise Exception("That's invalid markdown syntax!")
            for i, part in enumerate(split_node):
                if part == "":
                    continue
                if i % 2 == 0:
                    temp_list.append(TextNode(part, TextType.plain))
                else:
                    temp_list.append(TextNode(part, text_type))
            new_list.extend(temp_list)
        else:
            new_list.append(node)
            continue
    return new_list   

def extract_markdown_images(text):
    image_matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        info = extract_markdown_images(node.text)
        image_alt = info(0)
        image_link = info(1)
        sections = node.text.split(f"![{image_alt}]({image_link})", 1)
        for i, part in enumerate(sections):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(part)


def split_nodes_link(old_nodes):
    new_nodes = []