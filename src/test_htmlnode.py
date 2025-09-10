import unittest

from htmlnode import HTMLNode

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