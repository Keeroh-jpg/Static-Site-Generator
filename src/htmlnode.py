from textnode import *


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f'{key}="{value}"'
        return " " + props_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            str += child.to_html()
        str += f"</{self.tag}>"
        return str
    
def text_node_to_html_node(text_node):
    if text_node.text_type == None:
        raise Exception("Text_node needs to have a text_type.")
    if text_node.text_type == "plain":
        print("TestTestTest")
        plain_node = LeafNode(None, text_node.text)
        return plain_node    
    if text_node.text_type == "**bold_text**":
        bold_node = LeafNode("b", text_node.text)
        return bold_node
    if text_node.text_type == "__italic_text__":
        italic_node = LeafNode("i", text_node.text)
        return italic_node
    if text_node.text_type == "`code_text`":
        code_node = LeafNode("<code>", text_node.text)
        return code_node
    if text_node.text_type == "link":
        link_node = LeafNode("a", text_node.text, "href")
        return link_node
    if text_node.text_type == "image":
        image_node = LeafNode("img", "", "src" or "alt")
        return image_node