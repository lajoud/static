from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes:TextNode, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.texttype != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes



def extract_markdown_images(text):
     #return re.findall(r"!\[(\w)\]\((\w)\)",text)
     return re.findall(r"!\[(.*?)\]\((.*?)\)",text)


def extract_markdown_links(text):
     #return re.findall(r"!\[(\w)\]\((\w)\)",text)
     return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.texttype != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.texttype != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    new_node=[TextNode(text,TextType.TEXT)]

    return_italic= split_nodes_delimiter(new_node,"_",TextType.ITALIC)
    return_bold= split_nodes_delimiter(return_italic,"**",TextType.BOLD)
    return_code=split_nodes_delimiter(return_bold,"`",TextType.CODE)
    return_image=split_nodes_image(return_code)
    return_link=split_nodes_link( return_image)
    return return_link



def markdown_to_blocks(markdown):
    splitted=markdown.split("\n\n")
    for i in range(len(splitted)):
        splitted[i]=splitted[i].strip("\n")
        
    for element in splitted:
        if element =="":
            splitted.remove("")
        
    
    return splitted

