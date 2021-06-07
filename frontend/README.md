# Front End Design

## Introduction

The front end design usually consists of three parts: HTML, CSS, and JavaScript. Since it controls how the interface displays to the users, it is crucial to have a easy-to-follow, interactive design.

## Components

### HTML

HTML stands for Hyper Text Markup Language and is the standard markup language for creating Web pages. HTML document is made of a series of HTML elements. HTML elements tell the browser how to display the content. For instance, HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc. You may refer to the [HTML file](index.html) and take a look how the elements are arranged in the document.

External Material: https://www.w3schools.com/html/html_intro.asp

### CSS

CSS stands for Cascading Style Sheets. CSS describes how HTML elements are to be displayed on screen, paper, or in other media. CSS can save a lot of effort by controling the layout of multiple web pages all at once. However, it is important to note that you don't always need to generate CSS files on your own. There are many well-written CSS templates online, such as w3css, UIkit, etc. In our demo, we do not create our own CSS files. Instead, we load a CSS from online resource.

External Material: https://www.w3schools.com/w3css/defaulT.asp

### JavaScript

JavaScript files is capable of changing the HTML elements and CSS attributes. In order words, JavaScript can change a site from static to dynamic based on the user's behavior. For instance, when we submit a sentence to the backend for annotation and receive a result, we need to create a new HTML element to store the result and display it nicely. The JavaScript's functionality can also be enhanced by JQuery, a JavaScript library. It allows us to generate code in a simpler and cleaner way. You may refer to the [JavaScript file](js/demo.js) to see how we create the functions to manipulate the views.

External Material: https://www.w3schools.com/jquery/jquery_intro.asp

## Things to Modify for Your Demo

### HTML

The HTML file [index.html](To be Update for Final Version) controls the static elements of the page, and it generates a overall HTML DOM structure. Currently our HTML file contain a language option for multilingual models, but we do not utilize it since we are only running basic NER and PoS tagging in English. If your model only serve a single language, please remove the language option. We also have another option box for sentence examples. If our users just wish to run a simple demo, this feature can be very handy. Therefore, it is recommended that you include some examples that can clearly and nicely demonstrate the functionality of your demo. 

In addition, you may also modify the hyperlink to the [CSS files](To be Update for Final Version) and the hyperlink to the [JavaScript files](To be Update for Final Version) according to your needs.

### CSS

Since we are using external CSS files, we do not keep a hard copy of any CSS files in the folder for this demo as they are served online. However, if you want to build your own CSS files, you can include the file in the frondend/css folder and add the extra configuration in the [service_backend.py](To be Update for Final Version) file.

### Javascript

The [demo.js](To be Update for Final Version) controls the dynamic contents on the website, such as form submitting or language option choosing. Based on your annotation service, you can modify the list of available languages. You can also modify the examples for each language. Furthermore, there are several functions that handle changes and sumbits on the HTML form. You may refer to the [JavaScript file](To be Update for Final Version) and use the comments to understand what each function behaves.

Please note that you are very likely need to change the [runAnnotation()](To be Update for Final Version). Please modify the data variable to include every necessary elements for you annotation service. For our demo, we only need to send the text in data, but for your purpose, the data can be more complicated, such as adding language and other flags.
