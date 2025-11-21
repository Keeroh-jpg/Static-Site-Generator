import unittest
from block_markdown import *


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
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


if __name__ == "__main__":
    unittest.main()