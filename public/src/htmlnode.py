

class HTMLNode():
    def __init__(self,tag=None,value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError("")
    
    
    def props_to_html(self):
        return_text=""

        if self.props==None or self.props =={}:
            return ""
        else:
            for prop in self.props:
                return_text+=f' {prop}="{self.props[prop]}"'

            return return_text
        
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props_to_html()}")

    def __eq__(self, other):
        return (
            self.children==other.children
            and self.tag==other.tag
            and self.value==other.value
            and self.props==other.props
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return self.value
        return_text=""
        if self.props ==None:
            return_text+=f"<{self.tag}>"
        else:
            for prop in self.props:
                return_text+=f'<{self.tag} {prop}="{self.props[prop]}">'
        return_text+=f"{self.value}</{self.tag}>"
        return return_text
    
    def __repr__(self):
        print(f"tag:{self.tag}, value:{self.value}, props:{self.props_to_html()}")
        
    def __eq__(self, other):
        return (
            self.tag==other.tag
            and self.value==other.value
            and self.props==other.props
        )

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag==None:
            raise ValueError("the parent node have no tag")
        if self.children==None:
            raise ValueError("the parent node have no child attached")
        
        return_text=""
        if self.props ==None:
            return_text+=f"<{self.tag}>"
            for child in self.children:
                return_text+=child.to_html()
        else:
            for prop in self.props:
                return_text+=f'<{self.tag} {prop}="{self.props[prop]}">'
            for child in self.children:
                return_text+=child.to_html()

        return_text+=f"</{self.tag}>"
        return return_text
    


    def __eq__(self, other):
        return (
            self.tag==other.tag
            and self.children==other.children
            and self.props==other.props
        )