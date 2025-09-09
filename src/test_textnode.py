import unittest

from textnode import TextNode, TextType


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
    
    def test_if_str(self):
        node = TextNode("This is a link", TextType.link, "https://www.boot.dev")
        node2 = TextNode("Why me?", TextType.plain)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()