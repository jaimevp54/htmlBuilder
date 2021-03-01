HTML tags
*********

Each HTML element type has a corresponding class defined in the ``htmlBuilder.tags`` module.

.. code:: python

    from htmlBuilder.tags import Div

    html = Div()
    print(html.render())

.. code:: html

    <div></div>

As you can see in the previous example, the ``Div`` instance has a ``render()`` method which returns a string with the resulting HTML. This is true for all HTML elements defined within ``htmlBuilder.tags``.

Adding content
==============
We'll continue by adding some text content into our HTML element.

.. code:: python

    from htmlBuilder.tags import Div, Span

    html = Div([], "Hello world")
    print(html.render())

    html = Div([], Span())
    print(html.render())

.. code:: html

   <div>Hello world</div>
   <div><span></span></div>

When initializing a HTML element the first argument must be a ``list``, ``tuple`` or iterable containing any number of ``htmlBuilder.attributes.HtmlTagAttribute`` instances (see :doc:`attributes` for more details). Then, zero or more ``htmlBuilder.tags.HtmlTag``, ``str`` or iterable instance objects as the element's content. That means that all of the following are valid and will render the same HTML:

.. note::
   All of the following examples in this page will exclude the following lines unless specified otherwise
    - ``from htmlBuilder.tags import *``
    - ``print(html.render())``

.. code:: python

    # All of the following will render:
    # '<ul><li></li><li></li></ul>'

    Ul([],
        Li(),
        Li(),
    )

    Ul([], [
        Li(),
        Li(),
    ])

    Ul([],
        Li(),
        [Li()],
    )

    Ul([], (Li() for _ in range(2)))

    #Any level of nesting is allowed when passing an iterable. So this is also valid:
    Ul([], [[[[Li(), Li()]]]])

Adding a <!DOCTYPE> declaration
===============================
HTML documents should declare their type for browsers to know what to expect. So all HTML documents should start with a ``<!DOCTYPE>`` declaration.

Users can pass the ``doctype=True`` option to the ``render()`` method to handle this.

.. code:: python

    html = Div()
    print(html.render(doctype=True, pretty=True))

.. code:: html

    <!DOCTYPE html>
    <div></div>

For information on how to control the render process and the ``pretty=True`` option, see :doc:`output-format`.
