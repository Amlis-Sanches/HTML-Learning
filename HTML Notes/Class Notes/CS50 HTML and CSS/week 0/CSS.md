---
aliases:
  - CSS3
---
CSS, or **Cascading Style Sheets**, is a language used to style and layout web pages created with HTML. While HTML provides the structure and content of a webpage, CSS controls how it looks and feels.

### What CSS Does:
1. **Styling Elements**: CSS defines the colors, fonts, sizes, and other visual aspects of HTML elements.
2. **Layout Control**: It determines how elements are positioned, spaced, and aligned on the page.
3. **Responsive Design**: CSS makes websites look good on different devices by adjusting styles based on screen sizes (e.g., mobile vs. desktop).
4. **Visual Effects**: It adds animations, transitions, and other effects to make web pages interactive and engaging.
### Example:
Without CSS:
```html
<h1>Welcome to My Website</h1>
<p>This is a simple webpage.</p>
```

With CSS:
```html
<style>
    body {
        background-color: #f0f8ff;
        font-family: Arial, sans-serif;
        text-align: center;
    }
    h1 {
        color: #ff6347;
    }
    p {
        font-size: 18px;
    }
</style>

<h1>Welcome to My Website</h1>
<p>This is a simple webpage.</p>
```

CSS transforms a plain page into an attractive, professional-looking design. It separates the **content** (HTML) from the **presentation** (CSS), making it easier to maintain and update websites.

## Style
Here we can add a **attribute** to each item `<body> or <h1>` for example and change just one element or multiple. Adding style in multiple places allows me to change the color, alignment and more. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1 style="color: aquamarine; text-align: center;">Welcome to my Webpage!</h1>
        Hello World
    </body>
    <body style="color: blueviolet; text-align: center;">
        <h1>Welcome to My Webpage</h1>
        Hello World
    </body>
</html>
```

## Elements
But this is a pain in the butt to change when you want to change all your elements for every `<h1>` item. In this case you can dictate the style within the `<head>` and describe what every `<h1>` will look like. achieving the same thing. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            h1 {
                color: violet;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to my Webpage!</h1>
        Hello World
    </body>
    <body>
        <h1>This is my second element text</h1>
        Hello World
    </body>
</html>
```

## Applying Elements Across pages
There is an additional issue when you start adding pages. These new pages need to have the same style, this means you have to change each page. Alternatively you can create a styles.css code that contains the styles you want and using the `<link>` method you can pull the styles from the css file into your code. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    ...
```

## Most Common Elements
A lot of time you will need to edit the sizing of a area and in the case of a *Divider* `<div>`, you can change the background, size, margins and how much padding the elements inside have. 
```css
div {
	background-color: bisque;
	width: 200px;
	height: 500px;
	padding: 100px;
	margin: 200px;
}
```

## Stacking CSS changes
But what if I have multiple elements I am changing and they are the same. Lets take the table for example and how we can create borders. There were many items needed to build a table but if we wanted `<td> and <th>` to be the same, we can `td, th` use a comma to accept both are changing for this element. 
```css
table {
	border: 1px solid black;
	border-collapse:  collapse;
}

td, th {
	border: 1px solid blue;
}
```

## html ids to css
In other cases you might want to select one item and it is best practice to separate your html and CSS code. So what you can do in your html code is give it a id. This id can be referenced in CSS and any elements that use that id will have those changes. and you can stack these id's just like we did in [[#Stacking CSS changes]].
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            #headingspecial {
            color: aqua
            }
        </style>
    </head>
    <body>
        <h1 id="headingspecial">Heading 1</h1>
        <h1>Heading 2</h1>
        <h1>Heading 3</h1>
    </body>
</html>
```

## Classes
Though you can make something more complicated and need to reference the same point. but there are multiple points throughout your code. you instead can use a class. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            .bazz {
                color: blue;
            }
        </style>
    </head>
    <body>
        <h1 class="bazz">Heading 1</h1>
        <h1 class="bazz">Heading 2</h1>
        <h1>Heading 3</h1>
    </body>
</html>
```

## Specificity
But what order do you determine that the code will override each other. We have to keep in mind that the following is the order of priority.
1. inline - hard coding style indented in the item
2. id - `#id {}`
3. class - class = "something"
4. type - general use

## Selectors
Though remember where we were indicating all the types of variables that would be affected in the CSS code. Well it turns out you can use many different symbols to dictate what the relationship means. You can use the following:

![selectors](https://cs50.harvard.edu/web/2020/notes/0/images/selectors.png)

For example if we used the `Child Selector >` we can say that all elements that are descendance from another element will have the color blue. Here we create two list one ol and one ul. Then with the > we can say all list items descended from ul's will be blue. 
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            ul > li {
                color: blue;
            }
        </style>
    </head>
    <body>
        <ol>
            <li>List item one</li>
            <li>List item two</li>
            <ul>
                <li>Sublist One</li>
                <li>Sublist two</li>
            </ul>
            <li>List item three</li>
        </ol>
    </body>
</html>
```

Where as we can go something so specific that we choose an attribute an element has.  With CSS we can say that links that have facebook will only be red. That link will be the only one affected. 
```css
a[href="https://m.facebook.com/"] {
                color: red;
            }
```