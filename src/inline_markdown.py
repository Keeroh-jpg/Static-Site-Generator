from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type == TextType.plain:
            temp_list = []
            split_node = node.text.split(delimiter)
            if len(split_node) % 2 == 0:
                raise Exception("That's invalid markdown syntax!")
            for i, part in enumerate(split_node):
                if part == "":
                    continue
                if i % 2 == 0:
                    temp_list.append(TextNode(part, TextType.plain))
                else:
                    temp_list.append(TextNode(part, text_type))
            new_list.extend(temp_list)
        else:
            new_list.append(node)
            continue
    return new_list   