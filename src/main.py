from textnode import TextNode, TextType

def main():
    text_node = TextNode("Hello, World!", TextType.link, "https://www.boot.dev")
    print(text_node)

main()