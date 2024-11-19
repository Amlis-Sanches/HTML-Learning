---
author:
  - Brian Yu
aliases:
  - HTML
  - CSS
---
# HTML

## First Program
Here we will create a program in visual studio code called `Hello.html`. Here we will copy the following lines bellow. This will give us our first code. Now for us we have the Live Server extension installed in our visual studio code, so if we right click the file and run server we will get a page that has a tittle 'Hello!' and a text with "Hello, World!".

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        Hello, world!
    </body>
<html>
```

But lets break this down and try to figure out what is going on here:
- `<!DOCTYPE html>` This is a doctype declaration. Here we are describing what version of HTML we are using. 
- `<html lang="en"> ..to.. </html> ` Here we are tying to describe the content of the page and in between these two items, this is the html content. but within the first html we have a **attribute** `lang="en"`. This attribute is describing that the language that this page is written in is in English. 
- The next section we have is `<head>` and this is additional information you are adding to the page that the user isn't necessarily going to see. Within our heading we are adding a `<tittle>`.
- We also have a `<body>` for this page and that body contains the text. 

Additional Items to think of:
- After that, the page consists of nested **HTML elements** (such as html and body), each with an **opening and closing tag** marked with either `<element>` for an opening and `</element>` for a closing.
- With all html code its best to think with your code with the Document Object Model ( #DOM )

## Headings
Headings in html are coded with `<h1></h1>`. Here this is the first and largest heading you can make in html. There are 6 to choose from. You can see with running this, there is three different headings applied bellow.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Headings</title>
    </head>
    <body>
        <h1>This is a heading</h1>
        <h2>This is a smallar heading</h2>
        <h6>This is the smallest heading</h6>
    </body>
</html>
```

## Lists
In addition to headings there are lists. There are two types of list; Ordered lists `<ol></ol>` and Unordered Lists `<ul></ul>`. Each list need to have a line item `<li></li>`. When a line item is added to a ordered or unordered list, the list is indented. For a ordered list, it is numbered and an unordered is bullet point.
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Lists</title>
    </head>
    <body>
        An Unordered List:
        <ul>
            <li>One Item</li>
            <li>Another Item</li>
            <li>Yet Another Item</li>            
        </ul>

        An Ordered List:
        <ol>
            <li>First Item</li>
            <li>Second Item</li>            
            <li>Third Item</li>                
        </ol>
    </body>
</html>
```

## Images
Additionally you can add an image `<img>` to a page. Although this image indicator is unique from the others we have learned. This doesn't use a / to close its information. This is because this doesn't require additional information within the item. Though it has three **attributes**: 
- `src` the link to the name of the file you want to display. in this case "cat.jpg"
- `alt` What text displays instead of the image if the image cant show.
- `width` A indicator on how wide the image can be.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Image</title>
    </head>
    <body>
        <img src="cat.jpg" alt="Cat" width="300">
    </body>
</html>
```

## Links
There is also a way to link your files and external links to a page using the `<a></a>` item. Inside links you need to describe the **attribute** `href=""`. Inside the "" you can put an external link for the page to attack to or a page that already exists within your folder. You then can split the `<a>` item to have information directed to the link. say, just plain text or a heading.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Link</title>
    </head>
    <body>
        External Link
        <a href="https://google.com">
            Click Here
        </a>
        Internal Link
        <a href="image.html">
            <h1>Click For Cats</h1>
        </a>
    </body>
</html>
```

## Tables
tables `<table></table>` are more complex as they have headers `<thead>`, rows `<tr>`, a heading `<th>` a body `<tbody>` and data `<td>`. 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Table</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th>Ocean</th>
                    <th>Average Depth</th>
                    <th>Maximum Depth</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Pacific Ocean</td>
                    <td>4,280 m</td>
                    <td>10,911 m</td>
                </tr>
                <tr>
                    <td>Atlantic Ocean</td>
                    <td>3,646 m</td>
                    <td>8,486 m</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
```
# CSS

# Responsive Design

# Bootstrap

# Sass

