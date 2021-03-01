from htmlBuilder.exceptions import HtmlBuildError, InvalidAttributeError, NestingError
from .attributes import HtmlTagAttribute
from .utils import flatten_params

from itertools import repeat, chain


class Text:
    def __init__(self, text):
        self.text = text

    def _render(self, pretty=False, nesting_level=None) -> str:
        separator = "\n" if pretty else ''
        indentation = "  "*nesting_level if pretty else ''
        return f"{indentation}{self.text}{separator}"

    def __str__(self):
        return self.text


class HtmlTag:
    belongs_to: list = None

    @classmethod
    def validate_attributes(cls, attributes):
        for attr in attributes:
            if not isinstance(attr, HtmlTagAttribute):
                raise HtmlBuildError(
                    f"HtmlTag's 'attributes' elements must be HtmlTagAttribute instances. [{attr}->{attr.__class__.__name__}] found"
                )
            # TODO: enable this when implementing HTML syntax validation
            # if attr.belongs_to and cls.__name__ not in attr.belongs_to:
            #     raise InvalidAttributeError(f"{attr.__class__} is not allowed in {cls}")

    @classmethod
    def validate_inner_html(cls, inner_html):
        for item in inner_html:
            if not (
                isinstance(item, str) or
                issubclass(item.__class__, HtmlTag) or
                isinstance(item, Text)):
                raise HtmlBuildError(f"All inner_html elements must be 'HtmlTag' or 'str' instances, [{item}->{item.__class__.__name__}] found")
        return True

    def __init__(self, attributes=tuple(), *inner_content):
        self._name = self.__class__.__name__.lower()
        self.attributes = attributes
        self._inner_html = []

        self.validate_attributes(self.attributes)

        inner_content = flatten_params(inner_content)
        self.validate_inner_html(inner_content)
        for item in inner_content:
            if isinstance(item, str):
                self._inner_html.append(Text(item))
            else:
                self._inner_html.append(item)

    @property
    def inner_html(self):
        return self._inner_html

    @inner_html.setter
    def inner_html(self, content):
        self.validate_inner_html(flatten_params(content))
        self._inner_html = []
        for item in content:
            if isinstance(item, str):
                self._inner_html.append(Text(item))
            else:
                self._inner_html.append(item)

    @property
    def name(self) -> str:
        return self._name

    def render(self, pretty=False, doctype=False) -> str:
        result = ''
        if doctype:
            result += DOCTYPE()._render(pretty=pretty)
        result+= self._render(pretty=pretty, nesting_level=0)
        return result

    def _render(self, pretty=False, nesting_level=None) -> str:
        separator = "\n" if pretty else ''
        indentation = "  "*nesting_level if pretty else ''

        tag_components: list = [
                f"{indentation}<{self._name}",
            ] + [
                f" {attribute.name}='{str(attribute.value)}'" for attribute in self.attributes
            ] + [
                f">{separator if self.inner_html else ''}",
                "".join((tag._render(pretty, nesting_level+1) for tag in self.inner_html)),
                f"{indentation if self.inner_html else ''}</{self._name}>{separator}",
            ]

        return "".join(tag_components)


class SelfClosingHtmlTag(HtmlTag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._inner_html:
            raise NestingError(f"SelfClosingHtmlTag {self.name} must not have inner html, {self._inner_html[0].name} was found")


    def _render(self, pretty=False, nesting_level=None) -> str:
        separator = "\n" if pretty else ''
        indentation = "  "*nesting_level if pretty else ''
        tag_components: list = [
                                   f"{indentation}<{self._name}",
                               ] + [
                                   f" {attribute.name}='{str(attribute.value)}'" for attribute in self.attributes
                               ] + [
                                   f"/>{separator}",
                               ]
        return "".join(tag_components)


class DOCTYPE(SelfClosingHtmlTag):
    """Defines the document type"""

    def _render(self, pretty=False, nesting_level=None) -> str:
        separator = "\n" if pretty else ''
        return f"<!DOCTYPE html>{separator}"


class A(HtmlTag):
    """Defines a hyperlink"""
    pass


class Abbr(HtmlTag):
    """Defines an abbreviation or an acronym"""
    pass


class Acronym(HtmlTag):
    """Not supported in HTML5. Use <abbr> instead."""
    pass


class Address(HtmlTag):
    """Defines contact information for the author/owner of a document"""
    pass


class Applet(HtmlTag):
    """Not supported in HTML5. Use <embed> or <object> instead."""
    pass


class Area(SelfClosingHtmlTag):
    """Defines an area inside an image-map"""
    pass


class Article(HtmlTag):
    """Defines an article"""
    pass


class Aside(HtmlTag):
    """Defines content aside from the page content"""
    pass


class Audio(HtmlTag):
    """Defines sound content"""
    pass


class B(HtmlTag):
    """Defines bold text"""
    pass


class Base(SelfClosingHtmlTag):
    """Specifies the base URL/target for all relative URLs in a document"""
    pass


class Basefont(HtmlTag):
    """Not supported in HTML5. Use CSS instead."""
    pass


class Bdi(HtmlTag):
    """Isolates a part of text that might be formatted in a different direction from other text outside it"""
    pass


class Bdo(HtmlTag):
    """Overrides the current text direction"""
    pass


class Big(HtmlTag):
    """Not supported in HTML5. Use CSS instead."""
    pass


class Blockquote(HtmlTag):
    """Defines a section that is quoted from another source"""
    pass


class Body(HtmlTag):
    """Defines the document's body"""
    pass


class Br(SelfClosingHtmlTag):
    """Defines a single line break"""
    pass


class Button(HtmlTag):
    """Defines a clickable button"""
    pass


class Canvas(HtmlTag):
    """Used to draw graphics, on the fly, via scripting (usually JavaScript)"""
    pass


class Caption(HtmlTag):
    """Defines a table caption"""
    pass


class Center(HtmlTag):
    """Not supported in HTML5. Use CSS instead."""
    pass


class Cite(HtmlTag):
    """Defines the title of a work"""
    pass


class Code(HtmlTag):
    """Defines a piece of computer code"""
    pass


class Col(SelfClosingHtmlTag):
    """Specifies column properties for each column within a <colgroup> element """
    pass


class Colgroup(HtmlTag):
    """Specifies a group of one or more columns in a table for formatting"""
    pass


class Datalist(HtmlTag):
    """Specifies a list of pre-defined options for input controls"""
    pass


class Dd(HtmlTag):
    """Defines a description/value of a term in a description list"""
    pass


class Del(HtmlTag):
    """Defines text that has been deleted from a document"""
    pass


class Details(HtmlTag):
    """Defines additional details that the user can view or hide"""
    pass


class Dfn(HtmlTag):
    """Represents the defining instance of a term"""
    pass


class Dialog(HtmlTag):
    """Defines a dialog box or window"""
    pass


class Dir(HtmlTag):
    """Not supported in HTML5. Use <ul> instead."""
    pass


class Efines(HtmlTag):
    """directory list"""
    pass


class Div(HtmlTag):
    """Defines a section in a document"""
    pass


class Dl(HtmlTag):
    """Defines a description list"""
    pass


class Dt(HtmlTag):
    """Defines a term/name in a description list"""
    pass


class Em(HtmlTag):
    """Defines emphasized text """
    pass


class Embed(SelfClosingHtmlTag):
    """Defines a container for an external (non-HTML) application"""
    pass


class Fieldset(HtmlTag):
    """Groups related elements in a form"""
    pass


class Figcaption(HtmlTag):
    """Defines a caption for a <figure> element"""
    pass


class Figure(HtmlTag):
    """Specifies self-contained content"""
    pass


class Font(HtmlTag):
    """Not supported in HTML5. Use CSS instead."""
    pass


class Footer(HtmlTag):
    """Defines a footer for a document or section"""
    pass


class Form(HtmlTag):
    """Defines an HTML form for user input"""
    pass


class Frame(HtmlTag):
    """Not supported in HTML5."""
    pass


class Frameset(HtmlTag):
    """Not supported in HTML5."""
    pass


class H1(HtmlTag):
    """HTML heading"""
    pass


class H2(HtmlTag):
    """HTML heading"""
    pass


class H3(HtmlTag):
    """HTML heading"""
    pass


class H4(HtmlTag):
    """HTML heading"""
    pass


class H5(HtmlTag):
    """HTML heading"""
    pass


class H6(HtmlTag):
    """HTML heading"""
    pass


class Head(HtmlTag):
    """Defines information about the document"""
    pass


class Header(HtmlTag):
    """Defines a header for a document or section"""
    pass


class Hr(SelfClosingHtmlTag):
    """Defines a thematic change in the content"""
    pass


class Html(HtmlTag):
    """Defines the root of an HTML document"""
    pass


class I(HtmlTag):
    """Defines a part of text in an alternate voice or mood"""
    pass


class Iframe(HtmlTag):
    """Defines an inline frame"""
    pass


class Img(SelfClosingHtmlTag):
    """Defines an image"""
    pass


class Input(SelfClosingHtmlTag):
    """Defines an input control"""
    pass


class Ins(HtmlTag):
    """Defines a text that has been inserted into a document"""
    pass


class Kbd(HtmlTag):
    """Defines keyboard input"""
    pass


class Keygen(HtmlTag):
    """Defines a key-pair generator field (for forms)"""
    pass


class Label(HtmlTag):
    """Defines a label for an <input> element"""
    pass


class Legend(HtmlTag):
    """Defines a caption for a <fieldset> element"""
    pass


class Li(HtmlTag):
    """Defines a list item"""
    pass


class Link(SelfClosingHtmlTag):
    """Defines the relationship between a document and an external resource (most used to link to style sheets)"""
    pass


class Main(HtmlTag):
    """Specifies the main content of a document"""
    pass


class Map(HtmlTag):
    """Defines a client-side image-map"""
    pass


class Mark(HtmlTag):
    """Defines marked/highlighted text"""
    pass


class Menu(HtmlTag):
    """Defines a list/menu of commands"""
    pass


class Menuitem(HtmlTag):
    """Defines a command/menu item that the user can invoke from a popup menu"""
    pass


class Meta(SelfClosingHtmlTag):
    """Defines metadata about an HTML document"""
    pass


class Meter(HtmlTag):
    """Defines a scalar measurement within a known range (a gauge)"""
    pass


class Nav(HtmlTag):
    """Defines navigation links"""
    pass


class Noframes(HtmlTag):
    """Not supported in HTML5."""
    pass


class Noscript(HtmlTag):
    """Defines an alternate content for users that do not support client-side scripts"""
    pass


class Object(HtmlTag):
    """Defines an embedded object"""
    pass


class Ol(HtmlTag):
    """Defines an ordered list"""
    pass


class Optgroup(HtmlTag):
    """Defines a group of related options in a drop-down list"""
    pass


class Option(HtmlTag):
    """Defines an option in a drop-down list"""
    pass


class Output(HtmlTag):
    """Defines the result of a calculation"""
    pass


class P(HtmlTag):
    """Defines a paragraph"""
    pass


class Param(SelfClosingHtmlTag):
    """Defines a parameter for an object"""
    pass


class Picture(HtmlTag):
    """Defines a container for multiple image resources"""
    pass


class Pre(HtmlTag):
    """Defines preformatted text"""
    pass


class Progress(HtmlTag):
    """Represents the progress of a task"""
    pass


class Q(HtmlTag):
    """Defines a short quotation"""
    pass


class Rp(HtmlTag):
    """Defines what to show in browsers that do not support ruby annotations"""
    pass


class Rt(HtmlTag):
    """Defines an explanation/pronunciation of characters (for East Asian typography)"""
    pass


class Ruby(HtmlTag):
    """Defines a ruby annotation (for East Asian typography)"""
    pass


class S(HtmlTag):
    """Defines text that is no longer correct"""
    pass


class Samp(HtmlTag):
    """Defines sample output from a computer program"""
    pass


class Script(HtmlTag):
    """Defines a client-side script"""
    pass


class Section(HtmlTag):
    """Defines a section in a document"""
    pass


class Select(HtmlTag):
    """Defines a drop-down list"""
    pass


class Small(HtmlTag):
    """Defines smaller text"""
    pass


class Source(HtmlTag):
    """Defines multiple media resources for media elements (<video> and <audio>)"""
    pass


class Span(HtmlTag):
    """Defines a section in a document"""
    pass


class Strike(HtmlTag):
    """Not supported in HTML5. Use <del> or <s> instead."""
    pass


class Strong(HtmlTag):
    """Defines important text"""
    pass


class Style(HtmlTag):
    """Defines style information for a document"""
    pass


class Sub(HtmlTag):
    """Defines subscripted text"""
    pass


class Summary(HtmlTag):
    """Defines a visible heading for a <details> element"""
    pass


class Sup(HtmlTag):
    """Defines superscripted text"""
    pass


class Table(HtmlTag):
    """Defines a table"""
    pass


class Tbody(HtmlTag):
    """Groups the body content in a table"""
    pass


class Td(HtmlTag):
    """Defines a cell in a table"""
    pass


class Textarea(HtmlTag):
    """Defines a multiline input control (text area)"""
    pass


class Tfoot(HtmlTag):
    """Groups the footer content in a table"""
    pass


class Th(HtmlTag):
    """Defines a header cell in a table"""
    pass


class Thead(HtmlTag):
    """Groups the header content in a table"""
    pass


class Time(HtmlTag):
    """Defines a date/time"""
    pass


class Title(HtmlTag):
    """Defines a title for the document"""
    pass


class Tr(HtmlTag):
    """Defines a row in a table"""
    pass


class Track(HtmlTag):
    """Defines text tracks for media elements (<video> and <audio>)"""
    pass


class Tt(HtmlTag):
    """Not supported in HTML5. Use CSS instead."""
    pass


class U(HtmlTag):
    """Defines text that should be stylistically different from normal text"""
    pass


class Ul(HtmlTag):
    """Defines an unordered list"""
    pass


class Var(HtmlTag):
    """Defines a variable"""
    pass


class Video(HtmlTag):
    """Defines a video or movie"""
    pass


class Wbr(HtmlTag):
    """Defines a possible line-break"""
    pass
