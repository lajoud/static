from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH= "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered_list"
    ORDLIST= "ordered_list"



def block_to_block_type(block):
    


    pattern_headings = r'^(#{1,6})\s+(.+)'
    code_pattern= r"```[\r\n]+([\s\S]*?)```"

    splitted=block.split("\n")

    if re.match(pattern_headings,block)!=None:
        return BlockType.HEADING
    
    if re.search(code_pattern, block)!=None:
        return BlockType.CODE
    
    if block[0:6]=="```\n" and block[-4:]=="```":
        return BlockType.CODE
    
    test_quote=True
    for element in block.split("\n"):
        if len(element)>0:
            if element[0]!=">":
                test_quote=False
            
    if test_quote:
        return BlockType.QUOTE
    
    test_unlist=True
    for element in splitted:
        if len(element)<2:
            test_unlist=False
        else:
            #print(element,element[0:2])
            if element[0:2]!="- ":
                test_unlist=False

    if test_unlist:
        return BlockType.UNLIST

    test_ordlist=True

    for i in range(len(splitted)):
        if len(splitted[i])<3:
            test_ordlist=False
        else:
            if splitted[i][0:3]!=f"{i+1}. ":
                test_ordlist=False

    if test_ordlist:
        return BlockType.ORDLIST
    


    return BlockType.PARAGRAPH


block1="""### heading"""

block2="""1. test\n2. test"""

block3="simple test"

block4=" ```\nthis is some line of code ```"

block5=">this is a quote\n>this is another one"
block6=">this is a single quote"

block7="- an item\n- and another one"
"""
print(block_to_block_type(block1),"heading")

print(block_to_block_type(block2),"ordered")
print(block_to_block_type(block3),"paragraph")
"""
print(block_to_block_type(block4),"code")
"""
print(block_to_block_type(block5),"multiple quote")
print(block_to_block_type(block6),"single quote")
print(block_to_block_type(block7),"unordered")
"""