Getting Started
###############

Installation
************

.. code:: bash

    pip install htmlBuilder

.. note::
    Python 3.6 or later is required

A simple example
****************
.. code:: python

    # import necessary tags and attributes
    from htmlBuilder.tags import *
    from htmlBuilder.attributes import Class, Style as InlineStyle

    # html tags are represented by classes
    html = Html([],
        # any tag can receive another tag as constructor parameter
        Head([],
            Title([], "A beautiful site")
        ),
        Body([Class('btn btn-success'), InlineStyle(background_color='red', bottom='35px')],
            Hr(),
            Div([],
                Div()
            )
        )
    )
    # no closing tags are required

    # call the render() method to return tag instances as html text
    print(html.render(pretty=True))

Output:

.. code:: html

    <html>
      <head>
        <title>
          A beautiful site
        </title>
      </head>
      <body class='btn btn-success' style='background-color: red; bottom: 35px'>
        <hr/>
        <div>
          <div></div>
        </div>
      </body>
    </html>

A not so simple example
***********************
.. code:: python

    from htmlBuilder.attributes import Class
    from htmlBuilder.tags import Html, Head, Title, Body, Nav, Div, Footer, Ul, Li

    users = [ # declare data
        {
            "name": "Jose",
            "movies": ['A beautiful mind', 'Red'],
            "favorite-number": 42,
        },
        {
            "name": "Jaime",
            "movies": ['The breakfast club', 'Fight club'],
            "favorite-number": 7,
        },
        {
            "name": "Jhon",
            "movies": ['The room', 'Yes man'],
            "favorite-number": 987654321,
        },
    ]

    # functions can be used to handle recurring tag structures
    def my_custom_nav():
        # these functions can return a tag or a list of tags ( [tag1,tag2,tag3] )
        return Nav([Class("nav pretty")],
            Div([], "A beautiful NavBar")
        )

    html = Html([],
        Head([],
            Title([], "An awesome site")
        ),
        Body([],
            my_custom_nav(), # calling previously defined function
            [Div([Class(f"user-{user['name'].lower()}")],
                Div([], user['name']),
                Ul([],
                    [Li([], movie) for movie in user["movies"]] # list comprehensions can be used to easily render multiple tags
                ) if user['favorite-number'] < 100 else "Favorite number is too high" # python's ternary operation is allowed too
            ) for user in users],
            Footer([], "My Footer"),
        )
    )

    print(html.render(pretty=True, doctype=True)) # pass doctype=True to add a document declaration

Output:

.. code:: html

    <!DOCTYPE html>
    <html>
      <head>
        <title>
          An awesome site
        </title>
      </head>
      <body>
        <nav class='nav pretty'>
          <div>
            A beautiful NavBar
          </div>
        </nav>
        <div class='user-jose'>
          <div>
            Jose
          </div>
          <ul>
            <li>
              A beautiful mind
            </li>
            <li>
              Red
            </li>
          </ul>
        </div>
        <div class='user-jaime'>
          <div>
            Jaime
          </div>
          <ul>
            <li>
              The breakfast club
            </li>
            <li>
              Fight club
            </li>
          </ul>
        </div>
        <div class='user-jhon'>
          <div>
            Jhon
          </div>
          Favorite number is too high
        </div>
        <footer>
          My Footer
        </footer>
      </body>
    </html>
