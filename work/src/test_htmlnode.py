import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        node2 = HTMLNode(None,None,None,None)
        self.assertEqual(node,node2)

    def test_noteq(self):
        node = HTMLNode()
        node2 = HTMLNode("p","this is some text", None, None)
       
        self.assertNotEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()