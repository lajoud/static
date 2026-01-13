import unittest

from textnode import TextNode, TextType
from list_of_function import  split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node",TextType.BOLD,None)
        node4= TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)
        self.assertEqual(node,node4)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node",TextType.BOLD,None)
        node4= TextNode("This is a text node", TextType.BOLD, None)
        
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)
        

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node",TextType.BOLD,None)
        node4= TextNode("This is a text node", TextType.BOLD, None)
        
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)




if __name__ == "__main__":
    unittest.main()