# Attributes docstrings pulled from https://www.w3schools.com/tags/ref_attributes.asp

class HtmlTagAttribute:
    belongs_to: list = None

    def __init__(self, value: str):
        self._name: str = self.__class__.__name__.lower()
        self._value: str = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self._name}='{self._value}'"


class Style(HtmlTagAttribute):
    """Specifies an inline CSS style for an element"""

    def __init__(self, value: str = '', **params):
        self._name: str = 'style'
        self._value: str = value
        if not value:
            self._value = "; ".join(
                f"{key.replace('_','-')}: {val}"
                for key, val in params.items()
            )


class Data_(HtmlTagAttribute):
    """Used to store custom data private to the page or application"""

    def __init__(self, name, value):
        self._name = "data-"+name
        self._value = value


class Accept(HtmlTagAttribute):
    """Specifies the types of files that the server accepts (only for type="file")"""
    belongs_to = ['Input']


class AcceptCharset(HtmlTagAttribute):
    """Specifies the character encodings that are to be used for the form submission"""
    belongs_to = ['Form']


class Accesskey(HtmlTagAttribute):
    """Specifies a shortcut key to activate/focus an element"""


class Action(HtmlTagAttribute):
    """Specifies where to send the form-data when a form is submitted"""
    belongs_to = ['Form']


class Alt(HtmlTagAttribute):
    """Specifies an alternate text when the original element fails to display"""
    belongs_to = ['Area', 'Img', 'Input']


class Async(HtmlTagAttribute):
    """Specifies that the script is executed asynchronously (only for external scripts)"""
    belongs_to = ['Script']


class Autocomplete(HtmlTagAttribute):
    """Specifies whether the <form> or the <input> element should have autocomplete enabled"""
    belongs_to = ['Form', 'Input']


class Autofocus(HtmlTagAttribute):
    """Specifies that the element should automatically get focus when the page loads"""
    belongs_to = ['Button', 'Input', 'Keygen', 'Select', 'Textarea']


class Autoplay(HtmlTagAttribute):
    """Specifies that the audio/video will start playing as soon as it is ready"""
    belongs_to = ['Audio', 'Video']


class Challenge(HtmlTagAttribute):
    """Specifies that the value of the <keygen> element should be challenged when submitted"""
    belongs_to = ['Keygen']


class Charset(HtmlTagAttribute):
    """Specifies the character encoding"""
    belongs_to = ['Meta', 'Script']


class Checked(HtmlTagAttribute):
    """Specifies that an <input> element should be pre-selected when the page loads 
    (for type="checkbox" or type="radio")"""
    belongs_to = ['Input']


class Cite(HtmlTagAttribute):
    """Specifies a URL which explains the quote/deleted/inserted text"""
    belongs_to = ['Blockquote', 'Del', 'Ins', 'Q']


class Class(HtmlTagAttribute):
    """Specifies one or more classnames for an element (refers to a class in a style sheet)"""
    pass


class Cols(HtmlTagAttribute):
    """Specifies the visible width of a text area"""
    belongs_to = ['Textarea']


class Colspan(HtmlTagAttribute):
    """Specifies the number of columns a table cell should span"""
    belongs_to = ['Td', 'Th']


class Content(HtmlTagAttribute):
    """Gives the value associated with the http-equiv or name attribute"""
    belongs_to = ['Meta']


class Contenteditable(HtmlTagAttribute):
    """Specifies whether the content of an element is editable or not"""


class Contextmenu(HtmlTagAttribute):
    """Specifies a context menu for an element. The context menu appears when a user right-clicks on the element"""


class Controls(HtmlTagAttribute):
    """Specifies that audio/video controls should be displayed (such as a play/pause button etc)"""
    belongs_to = ['Audio', 'Video']


class Coords(HtmlTagAttribute):
    """Specifies the coordinates of the area"""
    belongs_to = ['Area']


class Data(HtmlTagAttribute):
    """Specifies the URL of the resource to be used by the object"""
    belongs_to = ['Object']


class DataAll(HtmlTagAttribute):
    """Used to store custom data private to the page or application"""


class Datetime(HtmlTagAttribute):
    """Specifies the date and time"""
    belongs_to = ['Del', 'Ins', 'Time']


class Default(HtmlTagAttribute):
    """Specifies that the track is to be enabled if the user's preferences do not indicate 
    that another track would be more appropriate"""
    belongs_to = ['Track']


class Defer(HtmlTagAttribute):
    """Specifies that the script is executed when the page has finished parsing (only for external scripts)"""
    belongs_to = ['Script']


class Dir(HtmlTagAttribute):
    """Specifies the text direction for the content in an element"""


class Dirname(HtmlTagAttribute):
    """Specifies that the text direction will be submitted"""
    belongs_to = ['Input', 'Textarea']


class Disabled(HtmlTagAttribute):
    """Specifies that the specified element/group of elements should be disabled"""
    belongs_to = ['Button', 'Fieldset', 'Input', 'Keygen', 'Optgroup', 'Option', 'Select', 'Textarea']


class Download(HtmlTagAttribute):
    """Specifies that the target will be downloaded when a user clicks on the hyperlink"""
    belongs_to = ['A', 'Area']


class Draggable(HtmlTagAttribute):
    """Specifies whether an element is draggable or not"""


class Dropzone(HtmlTagAttribute):
    """Specifies whether the dragged data is copied, moved, or linked, when dropped"""


class Enctype(HtmlTagAttribute):
    """Specifies how the form-data should be encoded when submitting it to the server (only for method="post")"""
    belongs_to = ['Form']


class For(HtmlTagAttribute):
    """Specifies which form element(s) a label/calculation is bound to"""
    belongs_to = ['Label', 'Output']


class Form(HtmlTagAttribute):
    """Specifies the name of the form the element belongs to"""
    belongs_to = ['Button', 'Fieldset', 'Input', 'Keygen', 'Label', 'Meter', 'Object', 'Output', 'Select', 'Textarea']


class Formaction(HtmlTagAttribute):
    """Specifies where to send the form-data when a form is submitted. Only for type="submit"""
    belongs_to = ['Button', 'Input']


class Headers(HtmlTagAttribute):
    """Specifies one or more headers cells a cell is related to"""
    belongs_to = ['Td', 'Th']


class Height(HtmlTagAttribute):
    """Specifies the height of the element"""
    belongs_to = ['Canvas', 'Embed', 'Iframe', 'Img', 'Input', 'Object', 'Video']


class Hidden(HtmlTagAttribute):
    """Specifies that an element is not yet, or is no longer, relevant"""


class High(HtmlTagAttribute):
    """Specifies the range that is considered to be a high value"""
    belongs_to = ['Meter']


class Href(HtmlTagAttribute):
    """Specifies the URL of the page the link goes to"""
    belongs_to = ['A', 'Area', 'Base', 'Link']


class Hreflang(HtmlTagAttribute):
    """Specifies the language of the linked document"""
    belongs_to = ['A', 'Area', 'Link']


class HttpEquiv(HtmlTagAttribute):
    """Provides an HTTP header for the information/value of the content attribute"""
    belongs_to = ['Meta']


class Id(HtmlTagAttribute):
    """Specifies a unique id for an element"""


class Ismap(HtmlTagAttribute):
    """Specifies an image as a server-side image-map"""
    belongs_to = ['Img']


class Keytype(HtmlTagAttribute):
    """Specifies the security algorithm of the key"""
    belongs_to = ['Keygen']


class Kind(HtmlTagAttribute):
    """Specifies the kind of text track"""
    belongs_to = ['Track']


class Label(HtmlTagAttribute):
    """Specifies the title of the text track"""
    belongs_to = ['Track', 'Option', 'Optgroup']


class Lang(HtmlTagAttribute):
    """Specifies the language of the element's content"""


class List(HtmlTagAttribute):
    """Refers to a <datalist> element that contains pre-defined options for an <input> element"""
    belongs_to = ['Input']


class Loop(HtmlTagAttribute):
    """Specifies that the audio/video will start over again, every time it is finished"""
    belongs_to = ['Audio', 'Video']


class Low(HtmlTagAttribute):
    """Specifies the range that is considered to be a low value"""
    belongs_to = ['Meter']


class Max(HtmlTagAttribute):
    """Specifies the maximum value"""
    belongs_to = ['Input', 'Meter', 'Progress']


class Maxlength(HtmlTagAttribute):
    """Specifies the maximum number of characters allowed in an element"""
    belongs_to = ['Input', 'Textarea']


class Media(HtmlTagAttribute):
    """Specifies what media/device the linked document is optimized for"""
    belongs_to = ['A', 'Area', 'Link', 'Source', 'Style']


class Method(HtmlTagAttribute):
    """Specifies the HTTP method to use when sending form-data"""
    belongs_to = ['Form']


class Min(HtmlTagAttribute):
    """Specifies a minimum value"""
    belongs_to = ['Input', 'Meter']


class Multiple(HtmlTagAttribute):
    """Specifies that a user can enter more than one value"""
    belongs_to = ['Input', 'Select']


class Muted(HtmlTagAttribute):
    """Specifies that the audio output of the video should be muted"""
    belongs_to = ['Video', 'Audio']


class Name(HtmlTagAttribute):
    """Specifies the name of the element"""
    belongs_to = ['Button', 'Fieldset', 'Form', 'Iframe', 'Input', 'Keygen', 'Map', 'Meta', 'Object', 'Output', 'Param',
                  'Select', 'Textarea']


class Novalidate(HtmlTagAttribute):
    """Specifies that the form should not be validated when submitted"""
    belongs_to = ['Form']


class Onabort(HtmlTagAttribute):
    """Script to be run on abort"""
    belongs_to = ['Audio', 'Embed', 'Img', 'Object', 'Video']


class Onafterprint(HtmlTagAttribute):
    """Script to be run after the document is printed"""
    belongs_to = ['Body']


class Onbeforeprint(HtmlTagAttribute):
    """Script to be run before the document is printed"""
    belongs_to = ['Body']


class Onbeforeunload(HtmlTagAttribute):
    """Script to be run when the document is about to be unloaded"""
    belongs_to = ['Body']


class Onblur(HtmlTagAttribute):
    """Script to be run when the element loses focus"""
    pass


class Oncanplay(HtmlTagAttribute):
    """Script to be run when a file is ready to start playing (when it has buffered enough to begin)"""
    belongs_to = ['Audio', 'Embed', 'Object', 'Video']


class Oncanplaythrough(HtmlTagAttribute):
    """Script to be run when a file can be played all the way to the end without pausing for buffering"""
    belongs_to = ['Audio', 'Video']


class Onchange(HtmlTagAttribute):
    """Script to be run when the value of the element is changed"""
    pass


class Onclick(HtmlTagAttribute):
    """Script to be run when the element is being clicked"""
    pass


class Oncontextmenu(HtmlTagAttribute):
    """Script to be run when a context menu is triggered"""
    pass


class Oncopy(HtmlTagAttribute):
    """Script to be run when the content of the element is being copied"""
    pass


class Oncuechange(HtmlTagAttribute):
    """Script to be run when the cue changes in a <track] element"""
    belongs_to = ['Track']


class Oncut(HtmlTagAttribute):
    """Script to be run when the content of the element is being cut"""
    pass


class Ondblclick(HtmlTagAttribute):
    """Script to be run when the element is being double-clicked"""
    pass


class Ondrag(HtmlTagAttribute):
    """Script to be run when the element is being dragged"""
    pass


class Ondragend(HtmlTagAttribute):
    """Script to be run at the end of a drag operation"""
    pass


class Ondragenter(HtmlTagAttribute):
    """Script to be run when an element has been dragged to a valid drop target"""
    pass


class Ondragleave(HtmlTagAttribute):
    """Script to be run when an element leaves a valid drop target"""
    pass


class Ondragover(HtmlTagAttribute):
    """Script to be run when an element is being dragged over a valid drop target"""
    pass


class Ondragstart(HtmlTagAttribute):
    """Script to be run at the start of a drag operation"""
    pass


class Ondrop(HtmlTagAttribute):
    """Script to be run when dragged element is being dropped"""
    pass


class Ondurationchange(HtmlTagAttribute):
    """Script to be run when the length of the media changes"""
    belongs_to = ['Audio', 'Video']


class Onemptied(HtmlTagAttribute):
    """Script to be run when something bad happens and the file is suddenly unavailable 
    (like unexpectedly disconnects)"""
    belongs_to = ['Audio', 'Video']


class Onended(HtmlTagAttribute):
    """Script to be run when the media has reach the end (a useful event for messages like "thanks for listening")"""
    belongs_to = ['Audio', 'Video']


class Onerror(HtmlTagAttribute):
    """Script to be run when an error occurs"""
    belongs_to = ['Audio', 'Body', 'Embed', 'Img', 'Object', 'Script', 'Style', 'Video']


class Onfocus(HtmlTagAttribute):
    """Script to be run when the element gets focus"""
    pass


class Onhashchange(HtmlTagAttribute):
    """Script to be run when there has been changes to the anchor part of the a URL"""
    belongs_to = ['Body']


class Oninput(HtmlTagAttribute):
    """Script to be run when the element gets user input"""
    pass


class Oninvalid(HtmlTagAttribute):
    """Script to be run when the element is invalid"""
    pass


class Onkeydown(HtmlTagAttribute):
    """Script to be run when a user is pressing a key"""
    pass


class Onkeypress(HtmlTagAttribute):
    """Script to be run when a user presses a key"""
    pass


class Onkeyup(HtmlTagAttribute):
    """Script to be run when a user releases a key"""
    pass


class Onload(HtmlTagAttribute):
    """Script to be run when the element is finished loading"""
    belongs_to = ['Body', 'Iframe', 'Img', 'Input', 'Link', 'Script', 'Style']


class Onloadeddata(HtmlTagAttribute):
    """Script to be run when media data is loaded"""
    belongs_to = ['Audio', 'Video']


class Onloadedmetadata(HtmlTagAttribute):
    """Script to be run when meta data (like dimensions and duration) are loaded"""
    belongs_to = ['Audio', 'Video']


class Onloadstart(HtmlTagAttribute):
    """Script to be run just as the file begins to load before anything is actually loaded"""
    belongs_to = ['Audio', 'Video']


class Onmousedown(HtmlTagAttribute):
    """Script to be run when a mouse button is pressed down on an element"""
    pass


class Onmousemove(HtmlTagAttribute):
    """Script to be run as long as the  mouse pointer is moving over an element"""
    pass


class Onmouseout(HtmlTagAttribute):
    """Script to be run when a mouse pointer moves out of an element"""
    pass


class Onmouseover(HtmlTagAttribute):
    """Script to be run when a mouse pointer moves over an element"""
    pass


class Onmouseup(HtmlTagAttribute):
    """Script to be run when a mouse button is released over an element"""
    pass


class Onmousewheel(HtmlTagAttribute):
    """Script to be run when a mouse wheel is being scrolled over an element"""
    pass


class Onoffline(HtmlTagAttribute):
    """Script to be run when the browser starts to work offline"""
    belongs_to = ['Body']


class Ononline(HtmlTagAttribute):
    """Script to be run when the browser starts to work online"""
    belongs_to = ['Body']


class Onpagehide(HtmlTagAttribute):
    """Script to be run when a user navigates away from a page"""
    belongs_to = ['Body']


class Onpageshow(HtmlTagAttribute):
    """Script to be run when a user navigates to a page"""
    belongs_to = ['Body']


class Onpaste(HtmlTagAttribute):
    """Script to be run when the user pastes some content in an element"""
    pass


class Onpause(HtmlTagAttribute):
    """Script to be run when the media is paused either by the user or programmatically"""
    belongs_to = ['Audio', 'Video']


class Onplay(HtmlTagAttribute):
    """Script to be run when the media is ready to start playing"""
    belongs_to = ['Audio', 'Video']


class Onplaying(HtmlTagAttribute):
    """Script to be run when the media actually has started playing."""
    belongs_to = ['Audio', 'Video']


class Onpopstate(HtmlTagAttribute):
    """Script to be run when the window's history changes."""
    belongs_to = ['Body']


class Onprogress(HtmlTagAttribute):
    """Script to be run when the browser is in the process of getting the media data"""
    belongs_to = ['Audio', 'Video']


class Onratechange(HtmlTagAttribute):
    """Script to be run each time the playback rate changes (like when a user switches to a slow motion 
    or fast forward mode)."""
    belongs_to = ['Audio', 'Video']


class Onreset(HtmlTagAttribute):
    """Script to be run when a reset button in a form is clicked."""
    belongs_to = ['Form']


class Onresize(HtmlTagAttribute):
    """Script to be run when the browser window is being resized."""
    belongs_to = ['Body']


class Onscroll(HtmlTagAttribute):
    """Script to be run when an element's scrollbar is being scrolled"""
    pass


class Onsearch(HtmlTagAttribute):
    """Script to be run when the user writes something in a search field (for <input="search">)"""
    belongs_to = ['Input']


class Onseeked(HtmlTagAttribute):
    """Script to be run when the seeking attribute is set to false indicating that seeking has ended"""
    belongs_to = ['Audio', 'Video']


class Onseeking(HtmlTagAttribute):
    """Script to be run when the seeking attribute is set to true indicating that seeking is active"""
    belongs_to = ['Audio', 'Video']


class Onselect(HtmlTagAttribute):
    """Script to be run when the element gets selected"""
    pass


class Onshow(HtmlTagAttribute):
    """Script to be run when a <menu] element is shown as a context menu"""
    belongs_to = ['Menu']


class Onstalled(HtmlTagAttribute):
    """Script to be run when the browser is unable to fetch the media data for whatever reason"""
    belongs_to = ['Audio', 'Video']


class Onstorage(HtmlTagAttribute):
    """Script to be run when a Web Storage area is updated"""
    belongs_to = ['Body']


class Onsubmit(HtmlTagAttribute):
    """Script to be run when a form is submitted"""
    belongs_to = ['Form']


class Onsuspend(HtmlTagAttribute):
    """Script to be run when fetching the media data is stopped before it is completely loaded for whatever reason"""
    belongs_to = ['Audio', 'Video']


class Ontimeupdate(HtmlTagAttribute):
    """Script to be run when the playing position has changed (like when the user fast forwards 
    to a different point in the media)"""
    belongs_to = ['Audio', 'Video']


class Ontoggle(HtmlTagAttribute):
    """Script to be run when the user opens or closes the <details] element"""
    belongs_to = ['Details']


class Onunload(HtmlTagAttribute):
    """Script to be run when a page has unloaded (or the browser window has been closed)"""
    belongs_to = ['Body']


class Onvolumechange(HtmlTagAttribute):
    """Script to be run each time the volume of a video/audio has been changed"""
    belongs_to = ['Audio', 'Video']


class Onwaiting(HtmlTagAttribute):
    """Script to be run when the media has paused but is expected to resume 
    (like when the media pauses to buffer more data)"""
    belongs_to = ['Audio', 'Video']


class Onwheel(HtmlTagAttribute):
    """Script to be run when the mouse wheel rolls up or down over an element"""
    pass


class Open(HtmlTagAttribute):
    """Specifies that the details should be visible (open) to the user"""
    belongs_to = ['Details']


class Optimum(HtmlTagAttribute):
    """Specifies what value is the optimal value for the gauge"""
    belongs_to = ['Meter']


class Pattern(HtmlTagAttribute):
    """Specifies a regular expression that an <input] element's value is checked against"""
    belongs_to = ['Input']


class Placeholder(HtmlTagAttribute):
    """Specifies a short hint that describes the expected value of the element"""
    belongs_to = ['Input', 'Textarea']


class Poster(HtmlTagAttribute):
    """Specifies an image to be shown while the video is downloading, or until the user hits the play button"""
    belongs_to = ['Video']


class Preload(HtmlTagAttribute):
    """Specifies if and how the author thinks the audio/video should be loaded when the page loads"""
    belongs_to = ['Audio', 'Video']


class Readonly(HtmlTagAttribute):
    """Specifies that the element is read-only"""
    belongs_to = ['Input', 'Textarea']


class Rel(HtmlTagAttribute):
    """Specifies the relationship between the current document and the linked document"""
    belongs_to = ['A', 'Area', 'Link']


class Required(HtmlTagAttribute):
    """Specifies that the element must be filled out before submitting the form"""
    belongs_to = ['Input', 'Select', 'Textarea']


class Reversed(HtmlTagAttribute):
    """Specifies that the list order should be descending (9,8,7...)"""
    belongs_to = ['Ol']


class Rows(HtmlTagAttribute):
    """Specifies the visible number of lines in a text area"""
    belongs_to = ['Textarea']


class Rowspan(HtmlTagAttribute):
    """Specifies the number of rows a table cell should span"""
    belongs_to = ['Td', 'Th']


class Sandbox(HtmlTagAttribute):
    """Enables an extra set of restrictions for the content in an iframe]"""
    belongs_to = ['Iframe']


class Scope(HtmlTagAttribute):
    """Specifies whether a header cell is a header for a column, row, or group of columns or rows"""
    belongs_to = ['Th']


class Scoped(HtmlTagAttribute):
    """Specifies that the styles only apply to this element's parent element and that element's child elements"""
    belongs_to = ['Style']


class Selected(HtmlTagAttribute):
    """Specifies that an option should be pre-selected when the page loads"""
    belongs_to = ['Option']


class Shape(HtmlTagAttribute):
    """Specifies the shape of the area"""
    belongs_to = ['Area']


class Size(HtmlTagAttribute):
    """Specifies the width, in characters (for <input>) or specifies the number of visible options (for <select>)"""
    belongs_to = ['Input', 'Select']


class Sizes(HtmlTagAttribute):
    """Specifies the size of the linked resource"""
    belongs_to = ['Img', 'Link', 'Source']


class Span(HtmlTagAttribute):
    """Specifies the number of columns to span"""
    belongs_to = ['Col', 'Colgroup']


class Spellcheck(HtmlTagAttribute):
    """Specifies whether the element is to have its spelling and grammar checked or not"""


class Src(HtmlTagAttribute):
    """Specifies the URL of the media file"""
    belongs_to = ['Audio', 'Embed', 'Iframe', 'Img', 'Input', 'Script', 'Source', 'Track', 'Video']


class Srcdoc(HtmlTagAttribute):
    """Specifies the HTML content of the page to show in the iframe]"""
    belongs_to = ['Iframe']


class Srclang(HtmlTagAttribute):
    """Specifies the language of the track text data (required if kind="subtitles")"""
    belongs_to = ['Track']


class Srcset(HtmlTagAttribute):
    """Specifies the URL of the image to use in different situations"""
    belongs_to = ['Img', 'Source']


class Start(HtmlTagAttribute):
    """Specifies the start value of an ordered list"""
    belongs_to = ['Ol']


class Step(HtmlTagAttribute):
    """Specifies the legal number intervals for an input field"""
    belongs_to = ['Input']


class Tabindex(HtmlTagAttribute):
    """Specifies the tabbing order of an element"""


class Target(HtmlTagAttribute):
    """Specifies the target for where to open the linked document or where to submit the form"""
    belongs_to = ['A', 'Area', 'Base', 'Form']


class Title(HtmlTagAttribute):
    """Specifies extra information about an element"""


class Translate(HtmlTagAttribute):
    """Specifies whether the content of an element should be translated or not"""


class Type(HtmlTagAttribute):
    """Specifies the type of element"""
    belongs_to = ['Button', 'Embed', 'Input', 'Link', 'Menu', 'Object', 'Script', 'Source', 'Style']


class Usemap(HtmlTagAttribute):
    """Specifies an image as a client-side image-map"""
    belongs_to = ['Img', 'Object']


class Value(HtmlTagAttribute):
    """Specifies the value of the element"""
    belongs_to = ['Button', 'Input', 'Li', 'Option', 'Meter', 'Progress', 'Param']


class Width(HtmlTagAttribute):
    """Specifies the width of the element"""
    belongs_to = ['Canvas', 'Embed', 'Iframe', 'Img', 'Input', 'Object', 'Video']


class Wrap(HtmlTagAttribute):
    """Specifies how the text in a text area is to be wrapped when submitted in a form"""
    belongs_to = ['Textarea']
