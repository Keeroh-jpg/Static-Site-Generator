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
    image_matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_matches

def extract_markdown_links(text):
    link_matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link_matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain:
            new_nodes.append(node)
            continue
        
        text = node.text
        parts = extract_markdown_images(text)
        if parts == []:
            new_nodes.append(node)
            continue

        while len(parts) > 0:
            alt, url = parts[0]
            snippet = f"![{alt}]({url})"
            before, after = text.split(snippet, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.plain))
            new_nodes.append(TextNode(alt, TextType.image, url))
            text = after
            parts = extract_markdown_images(text)
        if text != "":
            new_nodes.append(TextNode(text, TextType.plain))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain:
            new_nodes.append(node)
            continue
        
        text = node.text
        parts = extract_markdown_links(text)
        if parts == []:
            new_nodes.append(node)
            continue

        while len(parts) > 0:
            label, url = parts[0]
            snippet = f"[{label}]({url})"
            before, after = text.split(snippet, 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.plain))
            new_nodes.append(TextNode(label, TextType.link, url))
            text = after
            parts = extract_markdown_links(text)
        if text != "":
            new_nodes.append(TextNode(text, TextType.plain))
    return new_nodes

