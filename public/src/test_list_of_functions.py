import unittest

from textnode import TextNode, TextType
from list_of_function import  split_nodes_delimiter,extract_markdown_images, extract_markdown_links



class TestNodeParser(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertListEqual([
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ],new_nodes
            )


class Testextract_markdown_images(unittest.TestCase):
    def test_eq(self):
        str_to_test="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result= extract_markdown_images(str_to_test)
        self.assertListEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")
             , ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
             )


class Testextract_markdown_link(unittest.TestCase):
    def test_eq(self):
        str_to_test="This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result= extract_markdown_links(str_to_test)
        self.assertListEqual(
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")
             , ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
             )
        
    """def not_eq(self):
        str_to_test="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result= extract_markdown_link(str_to_test)
        self.assertListEqual (
            result,
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")
             , ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
             )
        """



if __name__ == "__main__":
    unittest.main()