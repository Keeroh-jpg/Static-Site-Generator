import unittest
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a link", TextType.link)
        node2 = TextNode("This is a text node", TextType.italic)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link", TextType.link, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.link, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.plain)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_split_delimiter_code(self):
        node = TextNode("This is a text with a `code block` word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)

    def test_split_delimiter_bold(self):
        node = TextNode("This is a text with a **bold** word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
    
    def test_split_delimiter_double_delimiter(self):
        node = TextNode("This is a text with a **** word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
    
    def test_split_delimiter_no_text(self):
        node = TextNode("****", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
    
    def test_split_delimiter_unbalanced_delimiters(self):
        node = TextNode("This is a **bold** word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
    
    

    
   
