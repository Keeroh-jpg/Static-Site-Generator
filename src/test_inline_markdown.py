import unittest

from inline_markdown import (split_nodes_delimiter,)

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



if __name__ == "__main__":
    unittest.main()
