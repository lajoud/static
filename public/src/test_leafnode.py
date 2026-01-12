import unittest

from htmlnode import LeafNode, HTMLNode


class Test_LeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        

if __name__ == "__main__":
    unittest.main()