Controlling the render process
******************************
Let's consider the following code:

.. code:: python

    from htmlBuilder.tags import Html, Head, Title, Body, Ul, Li
    from htmlBuilder.attributes import Id

    html = Html([],
        Head([],
            Title([], "My website"),
        ),
        Body([],
            Ul([Id('main-list')],
                Li([], 'Item 1'),
                Li([], 'Item 2'),
            )
        )
    )

    print(html.render())

.. code:: html

   <html><head><title>My website</title></head><body><ul id='main-list'><li>Item 1</li><li>Item 2</li></ul></body></html>

By default, ``htmlBuilder`` will try to keep the resulting HTML as small as possible. This is ideal for most cases and will not be a problem for browsers, but it can be for humans. So the `htmlBuilder.tasks.HtmlTag.render()` method allows you to control the output format of the rendered HTML.

Passing the option ``pretty=True``:

.. code:: python

    print(html.render(pretty=True))

.. code:: html

    <html>
      <head>
        <title>
          My website
        </title>
      </head>
      <body>
        <ul id='main-list'>
          <li>
            Item 1
          </li>
          <li>
            Item 2
          </li>
        </ul>
      </body>
    </html>
