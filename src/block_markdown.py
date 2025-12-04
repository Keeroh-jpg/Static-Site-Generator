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

    

    

        
    
    
    
