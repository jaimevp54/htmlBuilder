import unittest

from htmlBuilder.exceptions import HtmlBuildError, InvalidAttributeError, NestingError
from htmlBuilder.tags import HtmlTag, SelfClosingHtmlTag, DOCTYPE, Div, A, Text, Html
from htmlBuilder.utils import flatten_params
from htmlBuilder.attributes import HtmlTagAttribute, Data_, Style as InlineStyle


class TestFlattenMethod(unittest.TestCase):
    def test_nested_one_level(self):
        self.assertEqual(flatten_params([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_nested_two_levels(self):
        self.assertEqual(flatten_params([1, [2, [3]], 4]), [1, 2, 3, 4])

    def test_nested_three_levels(self):
        self.assertEqual(flatten_params([1, [[2, [3]], 4]]), [1, 2, 3, 4])

    def test_flatten_generators(self):
        self.assertEqual(flatten_params([1, [[2, [3]], 4], (i for i in range(5))]), [1, 2, 3, 4, 0, 1, 2, 3, 4])


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

    def test_render_with_doctype_option(self):
        self.assertEqual("<!DOCTYPE html><htmltag></htmltag>", HtmlTag().render(doctype=True))
        self.assertEqual("<!DOCTYPE html><selfclosinghtmltag/>", SelfClosingHtmlTag().render(doctype=True))

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

    def test_pretty_render(self):
        def build_html_text(nesting_level, current_level=1):
            if current_level>nesting_level:
                return

            html_text = ''
            html_text += "  "*current_level + "<htmltag>"

            result = build_html_text(nesting_level, current_level+1)
            if result:
                html_text += "\n" + result
                html_text += "\n" + "  "*current_level + "</htmltag>\n"
            else:
                html_text += "</htmltag>\n"

            html_text += "  "*current_level + "<htmltag></htmltag>\n"
            html_text += "  "*current_level + "<selfclosinghtmltag/>\n"
            html_text += "  "*current_level + f"level {current_level}"

            return html_text

        root_element = Html()
        current_element = root_element

        for i in range(1,10):
            inner_div = HtmlTag()

            current_element.inner_html = [
                inner_div,
                HtmlTag(),
                SelfClosingHtmlTag(),
                f"level {i}"
            ]

            self.assertEqual(
                f"<!DOCTYPE html>\n<html>\n{build_html_text(nesting_level=i)}\n</html>\n",
                root_element.render(pretty=True, doctype=True),
            )

            current_element = inner_div



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

    def test_render_style_attribute_from_value_str(self):
        self.assertEqual(
            HtmlTag([InlineStyle("custom-param1: test; custom-param2: test")]).render(),
            f"<htmltag style='custom-param1: test; custom-param2: test'></htmltag>"
        )

    def test_render_style_attribute_from_named_params(self):
        self.assertEqual(
            HtmlTag([InlineStyle(custom_param1='test', custom_param2='test')]).render(),
            f"<htmltag style='custom-param1: test; custom-param2: test'></htmltag>"
        )

    def test_render_data_attribute(self):
        self.assertEqual(
            HtmlTag([Data_("test-value", "Testing")]).render(),
            "<htmltag data-test-value='Testing'></htmltag>"
        )

    def test_raise_error_when_invalid_type_is_provided(self):
        with self.assertRaises(HtmlBuildError):
            HtmlTag(["invalid_attribute"])
        with self.assertRaises(HtmlBuildError):
            HtmlTag([HtmlTag])
