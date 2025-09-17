from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    plain = "plain_text"
    italic = "__italic_text__"
    bold = "**bold_text**"
    code = "`code_text`"
    link = "link"
    image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == None:
        raise Exception("Text_node needs to have a text_type.")
    if text_node.text_type == TextType.plain:
        plain_node = LeafNode(None, text_node.text)
        return plain_node
    if text_node.text_type == TextType.bold:
        bold_node = LeafNode("b", text_node.text)
        return bold_node
    if text_node.text_type == TextType.italic:
        italic_node = LeafNode("i", text_node.text)
        return italic_node
    if text_node.text_type == TextType.code:
        code_node = LeafNode("code", text_node.text)
        return code_node
    if text_node.text_type == TextType.link:
        link_node = LeafNode("a", text_node.text, "href")
        return link_node
    if text_node.text_type == TextType.image:
        image_node = LeafNode("img", "", {"src": text_node.src, "alt": text_node.alt})
        return image_node

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
    return new_list          

            