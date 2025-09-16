from enum import Enum
from htmlnode import *

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
    if text_node.text_type.plain:
        plain_node = LeafNode(None, text_node.text)
        return plain_node
    if text_node.text_type.bold:
        bold_node = LeafNode("b", text_node.text)
        return bold_node
    if text_node.text_type.italic:
        italic_node = LeafNode("i", text_node.text)
        return italic_node
    if text_node.text_type.code:
        code_node = LeafNode("code", text_node.text)
        return code_node
    if text_node.text_type.link:
        link_node = LeafNode("a", text_node.text, "href")
        return link_node
    if text_node.text_type.image:
        image_node = LeafNode("img", "", {"src": text_node.src, "alt": text_node.alt})
        return image_node