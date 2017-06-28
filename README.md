# Html Builder

HtmlBuilder is a python library that allows you to render html files by writing python code.

## Installation
run `pip install htmlbuilder`
## Use examples:

```python
from htmlBuilder.tags import *
from htmlBuilder.attributes import Class, InlineStyle

html = Html(
    Head(
        Title(Text("A beautiful site"))
    ),
    Body(
        Class('btn', 'btn-success'), InlineStyle(background_color='red', bottom='35px'),
        Hr(),
        Div(
            Div(

            )
        )
    ),
)
print(html)

# output

# <html>
#     <head>
#         <title>A beautiful site</title>
#     </head>
#     <body style='background-color:red; bottom:35px;' class='btn btn-success'>
#         <hr/>
#         <div>
#             <div></div>
#         </div>
#     </body>
# </html>
```

```python
from htmlBuilder.tags import *
from htmlBuilder.attributes import Class, InlineStyle

def my_div() -> list:

    result = Div(
        Div(
            Div(),
            P().times(4),
        ),
    ).times(2)

    return result


a = Html(
    Body(
        my_div(),
    ),
)

print(a)


# output

# <html>
# <head><title>A beautiful site</title></head>
# <body>
# <div>
#     <div>
#        <div></div>
#        <p></p>
#        <p></p>
#        <p></p>
#        <p></p></div>
# </div>
# <div>
#    <div>
#        <div></div>
#        <p></p>
#        <p></p>
#        <p></p>
#        <p></p></div>
# </div>
# </body>
# </html>
```
