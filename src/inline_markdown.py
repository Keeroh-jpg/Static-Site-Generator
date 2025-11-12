from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.plain:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.plain))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes 

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

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.plain)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "__", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

