import unittest

from inline_markdown import (split_nodes_delimiter,)
from inline_markdown import (extract_markdown_images)
from inline_markdown import (extract_markdown_links)

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual([TextNode("This is text with a ", TextType.plain),TextNode("bolded", TextType.bold),TextNode(" word", TextType.plain),],new_nodes,)

        
    def test_split_delimiter_code(self):
        node = TextNode("This is a text with a `code block` word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertListEqual([TextNode("This is a text with a ", TextType.plain),TextNode("code block", TextType.code),TextNode(" word", TextType.plain),],new_nodes,)

    def test_split_delimiter_double_bold(self):
        node = TextNode("This is a text with a **bold** word and **another**", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual([TextNode("This is a text with a ", TextType.plain),TextNode("bold", TextType.bold),TextNode(" word and ", TextType.plain),TextNode("another", TextType.bold),],new_nodes)
    
    def test_split_delimiter_bold_and_italic(self):
        node = TextNode("This is a text with an __italic__ word and a **bold** word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        new_nodes = split_nodes_delimiter(new_nodes, "__", TextType.italic)
        self.assertListEqual([TextNode("This is a text with an ", TextType.plain),TextNode("italic", TextType.italic),TextNode(" word and a ", TextType.plain),TextNode("bold", TextType.bold),TextNode(" word", TextType.plain),],new_nodes)

    def test_split_delimiter_italic(self):
        node = TextNode("This is a text with an __italic__ word", TextType.plain)
        new_nodes = split_nodes_delimiter([node], "__", TextType.italic)
        self.assertListEqual([TextNode("This is a text with an ", TextType.plain),TextNode("italic",TextType.italic),TextNode(" word", TextType.plain),],new_nodes)
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is test with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "So this is my link that sends you [to oldschool runescape](https://oldschool.runescape.com/)"
        )
        self.assertListEqual([("to oldschool runescape", "https://oldschool.runescape.com/")], matches)

    def test_multiple_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is a test with multiple images, ![image](httpps://i.imgur.com/whoreadsthis.png) and the second image is ![image](https://i.imgur.com/godihopethisworks.png)"
        )
        self.assertListEqual([("image", "httpps://i.imgur.com/whoreadsthis.png"), ("image", "https://i.imgur.com/godihopethisworks.png")], matches)

    def test_multiple_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a link [to youtube](https://www.youtube.com) and another link [to my warcraft logs](https://www.warcraftlogs.com/character/eu/silvermoon/keeroh)"
        )
        self.assertListEqual([("to youtube", "https://www.youtube.com"), ("to my warcraft logs", "https://www.warcraftlogs.com/character/eu/silvermoon/keeroh")], matches)

    def test_multiple_brackets_extract_markdown_links(self):
        matches = extract_markdown_links(
            "So this is my link that sends you [to oldschool runescape](https://oldschool.runescape.com/) (what do?)"
        )
        self.assertListEqual([("to oldschool runescape", "https://oldschool.runescape.com/")], matches)


if __name__ == "__main__":
    unittest.main()
