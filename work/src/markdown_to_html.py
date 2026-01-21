from htmlnode import HTMLNode,ParentNode,LeafNode
from list_of_function import(
    markdown_to_blocks,
    text_to_textnodes
)

import re

from markdownblock import BlockType, block_to_block_type
from htmlnode import HTMLNode
from textnode import TextNode, TextType,text_node_to_html_node



def markdown_to_html_node(md_text):

    md_blocks=markdown_to_blocks(md_text) #split in blocks
    child_htmlnode_list=[]
    for block in md_blocks:
        #work on all the blocks and append the different nodes
        #also needs to define the <div> section
        if not block.strip():
            continue
        child_htmlnode_list.append(md_block_to_html_node(block))

    return ParentNode(tag="div",children=child_htmlnode_list)
    

    

def md_block_to_html_node(md_block):
    block_type=block_to_block_type(md_block)

    if block_type==BlockType.QUOTE:
        #quote_node=[]
        lines=md_block.split("\n")
        clean_lines=[]
        for line in lines:
            clean_lines.append(line[2:])
        clean_lines= "\n".join(clean_lines)
        inline_children = text_to_children(clean_lines)
        return ParentNode(tag="blockquote",children=inline_children)


    if block_type == BlockType.UNLIST:
        li_nodes = []
        lines = md_block.split("\n")
        for line in lines:
            if not line.strip():
                continue
            # remove leading "- " (after trimming left spaces)
            clean = line.lstrip()
            if clean.startswith("- "):
                clean = clean[2:]  # drop "- "
            inline_children = text_to_children(clean)
            li_node = ParentNode(tag="li", children=inline_children)
            li_nodes.append(li_node)
        return ParentNode(tag="ul", children=li_nodes)
    
    if block_type== BlockType.ORDLIST:
        ol_nodes = []
        lines = md_block.split("\n")
        for line in lines:
            if not line.strip():
                continue
            clean = line.lstrip()
            idx = clean.index(".")
            clean = clean[idx+2:]
            inline_children = text_to_children(clean)
            ol_node = ParentNode(tag="li", children=inline_children)
            ol_nodes.append(ol_node)
        return ParentNode(tag="ol", children=ol_nodes)

    if block_type == BlockType.PARAGRAPH:
        text = md_block.strip()            # remove leading/trailing whitespace
        text = text.replace("\n", " ")     # convert newlines to spaces
        text = re.sub(r"\s+", " ", text)   # collapse multiple spaces to one
        inline_children = text_to_children(text)
        return ParentNode(tag="p", children=inline_children)
    
    """if block_type== BlockType.PARAGRAPH:
        text = md_block.replace("\n"," ")
        inline_children = text_to_children(text)
        return ParentNode(tag="p", children=inline_children)
    """
    if block_type == BlockType.CODE:
        # Split raw block into lines
        lines = md_block.split("\n")

        inner_lines = []
        in_code = False

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("```"):
                # toggle code mode but don't include fence line
                if not in_code:
                    in_code = True
                else:
                    in_code = False
                continue

            if in_code:
                # remove leading indentation from code content
                inner_lines.append(line.lstrip())

        inner = "\n".join(inner_lines) + "\n"

        return ParentNode("pre", [LeafNode("code", inner)])
    """
    if block_type==BlockType.CODE:
        lines = md_block.split("\n")
        inner = "\n".join(lines[1:-1]) + "\n"
        return ParentNode(tag="pre",children=[LeafNode(tag="code",value=inner)])
    """

    if block_type==BlockType.HEADING:
        header_count=0
        for c in md_block:
            if c=="#":
                header_count+=1
            else:
                break

        child=text_to_children(md_block[header_count+1:])
        return ParentNode(tag=f"h{header_count}",children=child)
    


def text_to_children(line):
    text_nodes=text_to_textnodes(line)
    children=[]
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children





    """PARAGRAPH= "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered_list"
    ORDLIST= "ordered_list"
"""