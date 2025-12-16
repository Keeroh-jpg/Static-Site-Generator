from enum import Enum
from htmlnode import *
from inline_markdown import *
from textnode import *


def markdown_to_blocks(markdown):
    final_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        else:
            final_blocks.append(block.strip())
    return final_blocks


class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"
    
def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    lines = block.split("\n")
    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.quote
    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.unordered_list
    is_ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{str(i)}. "):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ordered_list
    hash_count = 0
    for char in block:
        if char == "#":
            hash_count += 1
        else:
            break
    if 1 <= hash_count <= 6 and len(block) > hash_count and block[hash_count] == " ":
        return BlockType.heading
    else:
        return BlockType.paragraph
    
def markdown_to_html_node(markdown):
    block_nodes = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.quote:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                line = line.lstrip()
                if line.startswith(">"):
                    line = line[1:]
                    if line.startswith(" "):
                        line = line[1:]
                cleaned_lines.append(line)
            text = "\n".join(cleaned_lines)
            children_from_inline = text_to_children(text)
            block_nodes.append(HTMLNode("blockquote", None, children_from_inline))
        elif block_type == BlockType.unordered_list:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                line = line.lstrip()
                if line.startswith("-"):
                    line = line[1:]
                    if line.startswith(" "):
                        line = line[1:]
                children = text_to_children(line)
                li_nodes.append(HTMLNode("li", None, children))
            block_nodes.append(HTMLNode("ul", None, li_nodes))
        elif block_type == BlockType.heading:
            hash_count = 0
            line = block.lstrip()
            while hash_count < len(line) and hash_count < 6 and line[hash_count] == "#":
                hash_count += 1
            text = line[hash_count:].lstrip()
            children = text_to_children(text)
            tag = f"h{hash_count}"
            block_nodes.append(HTMLNode(tag, None, children))
        elif block_type == BlockType.code:
            lines = block.split("\n")
            code_text = ""
            for line in lines:
                if line.startswith("```"):
                    continue
                code_text += line +"\n"
            text_node = TextNode(code_text, TextType.code)
            code_child = text_node_to_html_node(text_node)
            pre_node = HTMLNode("pre", None, [code_child])
            block_nodes.append(pre_node)
        elif block_type == BlockType.ordered_list:
            lines = block.split("\n")
            li_nodes = []
            num = 0
            for line in lines:
                num += 1
                line = line.lstrip()
                prefix = f"{num}."
                if not line.startswith(prefix):
                    continue
                line = line[len(prefix):]
                if line.startswith(" "):
                    line = line[1:]
                children = text_to_children(line)
                li_nodes.append(HTMLNode("li", None, children))
            block_nodes.append(HTMLNode("ol", None, li_nodes))            
        else:
            children_from_inline = text_to_children(block)
            block_nodes.append(HTMLNode("p", None, children_from_inline))
    final_node = HTMLNode("div", None, block_nodes)
    return final_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
        



    

    

        
    
    
    
