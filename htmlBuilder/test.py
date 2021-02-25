import unittest

from htmlBuilder.exceptions import HtmlBuildError, InvalidAttributeError, NestingError
from htmlBuilder.tags import HtmlTag, SelfClosingHtmlTag, DOCTYPE, Div, A, Text
from htmlBuilder.utils import flatten_params
from htmlBuilder.attributes import HtmlTagAttribute, InlineStyle, Href, Autofocus


class TestFlattenMethod(unittest.TestCase):
    def test_nested_one_level(self):
        self.assertEqual(flatten_params([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_nested_two_levels(self):
        self.assertEqual(flatten_params([1, [2, [3]], 4]), [1, 2, 3, 4])

    def test_nested_three_levels(self):
        self.assertEqual(flatten_params([1, [[2, [3]], 4]]), [1, 2, 3, 4])


class TestTagObjectCreation(unittest.TestCase):

    def test_html_tag_params_must_be_an_html_tag_or_str_instance(self):
        HtmlTag([], Div())
        HtmlTag([], "Test")
        with self.assertRaises(HtmlBuildError):
            HtmlTag([], Div)

    def test_self_closing_tags_dont_allow_inner_tags_or_str_instance(self):
        with self.assertRaises(NestingError):
            SelfClosingHtmlTag([], Div())

class TestTagRendering(unittest.TestCase):
    def setUp(self):
        self.not_self_closing_tags = filter(lambda tag: tag is not SelfClosingHtmlTag, HtmlTag.__subclasses__())
        self.self_closing_tags = SelfClosingHtmlTag.__subclasses__()

    def test_empty_tag_render(self):
        for tag in self.not_self_closing_tags:
            self.assertEqual(tag().render(), f"<{tag.__name__.lower()}></{tag.__name__.lower()}>")

    def test_one_level_nested_tag_render(self):
        for tag_x in self.not_self_closing_tags:
            for tag_y in self.not_self_closing_tags:
                self.assertEqual(
                    tag_x([], tag_y()).render(),
                    f"<{tag_x.__name__.lower()}>"
                    f"<{tag_y.__name__.lower()}></{tag_y.__name__.lower()}>"
                    f"</{tag_x.__name__.lower()}>")

    def test_self_closing_tag_render(self):
        for tag in filter(lambda tag: tag is not DOCTYPE, self.self_closing_tags):
            self.assertEqual(tag().render(), f"<{tag.__name__.lower()}/>")

    def test_text_renders_correctly_inside_tags(self):
        test_str = "Testing"
        self.assertEqual(
            HtmlTag([],
                test_str
            ).render(),
            f"<htmltag>{test_str}</htmltag>"
        )

        self.assertEqual(
            Div([],
                test_str,
                test_str
            ).render(),
            f"<div>{test_str}{test_str}</div>"
        )

        self.assertEqual(
            Div([],
                test_str,
                A(),
                test_str
            ).render(),
            f"<div>{test_str}<a></a>{test_str}</div>"
        )


class TestTagAttributeRendering(unittest.TestCase):
    def setUp(self):
        self.all_attributes = HtmlTagAttribute.__subclasses__()
        self.all_tags = HtmlTag.__subclasses__()

    def test_render_from_string_constructor(self):
        for tag in self.all_tags:
            for attribute in self.all_attributes:
                if attribute.belongs_to and tag.__name__ in attribute.belongs_to:
                    self.assertEqual(
                        tag([attribute('test')]).render(),
                        f"<{tag.__name__.lower()} {attribute('test').name}='test'></{tag.__name__.lower()}>"
                    )

    def test_render_style_attribute_from_named_params(self):
        self.assertEqual(
            HtmlTag([InlineStyle(custom_param1='test', custom_param2='test')]).render(),
            f"<htmltag style='custom-param1: test; custom-param2: test; '></htmltag>"
        )

    def test_raise_error_when_invalid_type_is_provided(self):
        with self.assertRaises(HtmlBuildError):
            HtmlTag(["invalid_attribute"])
        with self.assertRaises(HtmlBuildError):
            HtmlTag([HtmlTag])


    def test_raise_error_if_not_in_allowed_tag(self):
        self.error_count = 0
        self.expected_error_count = 0
        for tag in self.all_tags:
            for attribute in self.all_attributes:
                if attribute.belongs_to and tag.__name__ not in attribute.belongs_to:
                    self.expected_error_count += 1
                    try:
                        tag([attribute('test')])
                        print('ups')
                    except InvalidAttributeError:
                        self.error_count += 1
        self.assertEqual(self.error_count, self.expected_error_count)
