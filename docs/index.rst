.. htmlBuilder documentation master file, created by
   sphinx-quickstart on Fri Jul  7 18:16:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to htmlBuilder's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Html Builder
=============
HtmlBuilder is a python library with the purpose of allowing you to render html by writing python code and also to make use of python features like comprehensions, clean syntax  and object oriented design to its full potential. 

A simple example ::

    # import necesary tags and attributes
    from htmlBuilder.tags import *
    from htmlBuilder.attributes import Class, InlineStyle

    
    # html tags are represented as classes 
    html = Html(
        # any tag can receive another tag as constructor parameter
        Head(
            Title(Text("A beautiful site"))
        ),
        Body(
            # tag's contructors can also receive attributes
            Class('btn', 'btn-success'), InlineStyle(background_color='red', bottom='35px'),
            Hr(),
            Div(
                Div()
            )
        ),
    )
    # no closing tags are required

    # call the render() method to return tag instances as html text
    print(html.render())


    ######### result #########

    <html>
        <head>
            <title>A beautiful site</title>
        </head>
        <body style='background-color:red; bottom:35px;' class='btn btn-success'>
            <hr/>
            <div>
                <div></div>
            </div>
        </body>
    </html>

A not so simple example ::

    from htmlBuilder.attributes import Class
    from htmlBuilder.tags import Html, Head, Title, Text, Body, Nav, Div, Footer, Ul, Li
    
    # declare data
    users = [
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
        return Nav(
            Class("nav pretty"),
            Div(Text("A beautiful NavBar"))
        )


    html = Html(
        Head(
            Title(Text("An awesome site"))
        ),
        Body(
            
            my_custom_nav(), # calling previously defined function
            [Div(
                Class(f"user-{user['name'].lower()}"), # string formating can be used to handle dinamic data
                Div(Text(user['name'])),
                Ul(
                    [Li(Text(movie)) for movie in user["movies"]] # list comprehensions can be used to easily render multiple tags
                ) if user['favorite-number'] < 100 else Text("Favorite number is too high") # python's ternary operation is allowed too
            ) for user in users], 
            Footer(Text("My Footer")),
        )
    )

    print(html.render())


    ######### result #########

    # <html>
    # <head><title>An awesome site</title></head>
    # <body>
    # <nav class='nav pretty'>
    #     <div>A beautiful NavBar</div>
    # </nav>
    # <div class='user-jose'>
    #     <div>Jose</div>
    #     <ul>
    #         <li>A beautiful mind</li>
    #         <li>Red</li>
    #     </ul>
    # </div>
    # <div class='user-jaime'>
    #     <div>Jaime</div>
    #     <ul>
    #         <li>The breakfast club</li>
    #         <li>Fight club</li>
    #     </ul>
    # </div>
    # <div class='user-jhon'>
    #     <div>Jhon</div>
    #     Favorite number is too high
    # </div>
    # <footer>My Footer</footer>
    # </body>
    # </html>

Wait! ... Maybe that was too much as an starting example, but that was a bit of what htmlBuilder is capable of doing.

For more detailed information checkout the `Source Code <www.github.com/jaimevp54/htmlBuilder>`


Installation
------------
Python 3.6 or higher is required to use htmlBuilder. If you meet this requirement just run ::

    pip install htmlbuilder

How to contribute
-----------------

The whole source code is available on `GitHub <www.github.com/jaimevp54/htmlBuilder>`_.

Feel to open an `Issue <www.github.com/jaimevp54/htmlBuilder/issues>`_ or to submit a pull request.

Liscence
--------
The project is licensed under the MIT license.


