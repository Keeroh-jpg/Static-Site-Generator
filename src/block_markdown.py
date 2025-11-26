from enum import Enum

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
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    if 1 <= count <= 6 and len(block) > count and block[count] == " ":
        return BlockType.heading
    
    
