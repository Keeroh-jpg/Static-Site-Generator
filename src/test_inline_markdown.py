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



if __name__ == "__main__":
    unittest.main()
