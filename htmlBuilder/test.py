import unittest

from htmlBuilder.tags import HtmlTag, SelfClosingHtmlTag, DOCTYPE
from htmlBuilder.utils import flatten_params


class TestFlattenMethod(unittest.TestCase):
    def test_nested_one_level(self):
        self.assertEqual(flatten_params([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_nested_two_levels(self):
        self.assertEqual(flatten_params([1, [2, [3]], 4]), [1, 2, 3, 4])

    def test_nested_three_levels(self):
        self.assertEqual(flatten_params([1, [[2, [3]], 4]]), [1, 2, 3, 4])


class TestTagRendering(unittest.TestCase):
    def setUp(self):
        self.not_self_closing_tags = list(filter(lambda tag: tag is not SelfClosingHtmlTag, HtmlTag.__subclasses__()))
        self.self_closing_tags = SelfClosingHtmlTag.__subclasses__()

    def test_empty_tag_render(self):
        for tag in self.not_self_closing_tags:
            self.assertEqual(tag().render(), f"<{tag.__name__.lower()}></{tag.__name__.lower()}>")

    def test_one_level_nested_tag_render(self):
        for tag_x in self.not_self_closing_tags:
            for tag_y in self.not_self_closing_tags:
                self.assertEqual(
                    tag_x(tag_y()).render(),
                    f"<{tag_x.__name__.lower()}><{tag_y.__name__.lower()}>"
                    f"</{tag_y.__name__.lower()}></{tag_x.__name__.lower()}>")

    def test_self_closing_tag_render(self):
        for tag in filter(lambda tag: tag is not DOCTYPE, self.self_closing_tags):
            self.assertEqual(tag().render(), f"<{tag.__name__.lower()}/>")


class TestTimesTagMethod(unittest.TestCase):
    def test_returns_list(self):
        self.assertIsInstance(HtmlTag().times(1), list)

    def test_returned_list_length(self):
        self.assertEquals(len(HtmlTag().times(10)), 10)

    def test_element_types(self):
        tag: HtmlTag = HtmlTag()
        self.assertEquals(tag.times(2), [tag, tag])

