import unittest
from block_markdown import *
from htmlnode import *


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with __italic__ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with __italic__ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_single_block(self):
        md = "This is just one block with no separators"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is just one block with no separators"])

    def test_markdown_to_blocks_with_whitespace(self):
        md = """
    This block has leading whitespace    

    This block has trailing whitespace    

    This block is normal
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "This block has leading whitespace",
            "This block has trailing whitespace",
            "This block is normal",
        ],
    )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with __italic__ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_unorderedlistblock(self):
        md = """
- This is the first item in a list
- again with the list items
- lets throw in a bold **item** !!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the first item in a list</li><li>again with the list items</li><li>lets throw in a bold <b>item</b> !!</li></ul></div>"
        )
        


if __name__ == "__main__":
    unittest.main()