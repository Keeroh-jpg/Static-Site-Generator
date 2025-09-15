import unittest

from htmlnode import HTMLNode, ParentNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_props_to_html(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        props_html = node.props_to_html()
        self.assertIn('class="container"', props_html)
        self.assertIn('id="main"', props_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode("div")
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")

    def test_repr(self):
        node = HTMLNode("span", "Text", [], {"style": "color:red"})
        repr_str = repr(node)
        self.assertIn("HTMLNode", repr_str)
        self.assertIn("span", repr_str)
        self.assertIn("Text", repr_str)
        self.assertIn("{'style': 'color:red'}", repr_str)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click this!", {"href": "https://www.example.com"} )
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">Click this!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("em", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><em>grandchild</em></span></div>")
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
