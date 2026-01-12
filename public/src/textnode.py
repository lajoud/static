from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"



class TextNode():
    def __init__(self,text, texttype, url=None):
        self.text=text
        self.texttype=texttype
        self.url=url
    def __eq__(self, other):
        if self.text ==other.text and self.texttype==other.texttype and self.url==other.url:
            return True
        else:
            return False
    def __repr__(self):
        return f"TextNode({self.text},{self.texttype},{self.url})"
    
