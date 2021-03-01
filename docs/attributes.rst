HTML attributes
***************
Each HTML attribute has a corresponding class defined in the ``htmlBuilder.attributes`` module. These can be used when initializing ``htmlBuilder.tags.HtmlTag`` instances.

.. code:: python

    from htmlBuilder.tags import Div
    from htmlBuilder.attributes import Id, Class

    html = Div([Id('main-div'), Class('pretty')])
    print(html.render())

.. code:: html

    <div id='main-div' class='pretty'></div>

Every ``HtmlTag`` is initialized with zero or more. If it receives one or more parameters, then the first must be a python iterable with zero or more ``HtmlTagAttribute`` instances.

.. note::
    Attribute class names are created by "camel casing" their corresponding HTML names. This process is done by uppercasing each letter after a hyphen(-) and then removing each of the hyphens. E.g.
       - ``class`` -> ``Class``
       - ``id`` -> ``Id``
       - ``accept-charset`` -> ``AcceptCharset``
       - ``onkeypress`` -> ``Onkeypress``

Special attributes
==================
Users can initialize all ``HtmlTagAttribute`` classes by passing a single ``str`` parameter with that attribute's value. Also, there are some frequently used attributes with more support.

``style``
---------
This attribute can use keyword arguments to define each CSS property. Both of the following objects render the same HTML.

.. note::
   All of the following examples in this page will exclude the following lines unless specified otherwise
    - ``from htmlBuilder.tags import *``
    - ``from htmlBuilder.attributes import *``
    - ``print(html.render())``

.. code:: python

    # Both objects represent the same html
    # <div style='color: white; background_color: black'>Hello World</div>

    Div([Style(color="white", background_color="black")], "Hello World")

    Div([Style("color: white; background-color: black")], "Hello World")

.. note::
    Notice that when using keyword arguments to initialize a ``Style`` instance, the CSS property name is constructed by replacing ``_`` with ``-``.

``data-*``
----------
Users can handle ``data-*`` attributes using the ``htmlBuilder.attributes.Data_`` class which expects a ``name`` and a ``value`` its  ``__init__`` first and second parameters respectively.

When rendered, the attribute name is constructed by appending the string ``"data-"`` with the given ``name``.

.. code:: python

    # Both objects represent the same html
    # <div data-message='Hello World'></div>

    Div([Data_("message", "Hello World")])

    Div([Data_(name="message", value="Hello World")])
