# Custom functions

- In a page, define the custom JavaScript function in a custom HTML, within
<script> tags.
- In a view, define the custom JavaScript functions in the Inline JavaScript editor, under
Behavior.

## Using the keywords this and page

In the inline JavaScript of a view, the keyword this uses the Initial global
execution context scope, which means that this refers to the view itself and can
also refer to any view that is nested inside it.

In the following example, the login form has a text and a password view defined in the page, with
the control IDs User name and Password. Note how
this is used in the inline JavaScript. The function Login() is
defined in the context of the this view. The same applies to the variables that
are defined in the function.

<!-- image -->

The keyword page can be used either in a custom HTML or in the inline
JavaScript of a view. Page refers to the topmost view of the page, which means
that the views in the page and also the views nested inside them can be accessed. For the nested
views, you must define the paths. For example, if you tried accessing the Username
control ID in the LoginV view at the page level, you would specify the path
as shown:

<!-- image -->

Note how this approach of defining a function does not use a keyword that precedes the function
name because the function is not ambiguous at page level. Also, note how the keyword
page is used instead of this, and the path to
Username had to be defined in the get() function. In the
example, LoginV is the control ID of the view, and
Username is the text control ID.

## Calling custom functions

After you have defined a function by using one of the methods described earlier, your function
can be accessed through the event handlers of any view. To call a function, use
@functionName or @functionName(); in the configuration options of
the event handler. In the following example, your custom function is added to the On
click event handler of a button.

<!-- image -->

When a function is defined at more levels, for example, in both the page and the view, the
version that is called is the one closest to the view. In our example, because
myFunction() is defined at both the page and view levels, the version that is
called is the myFunction() defined in the view itself. Functions that are defined
at the same level as the call are searched first, and then the search moves up sequentially through
the levels until it finds the function defined.

## Creating custom functions with parameters

A custom function can also be passed in arguments, which makes it reusable in other types of
views. A method that is commonly used in many views is setLabel. You can create a
single function with a parameter.

<!-- image -->

The function changeLabel was given the control parameter.
You can then call a method on that control. In this case, the setLabel method was
called to change the label to Label Changed. To call the
changeLabel function, you can call it from one of the events of a view.

<!-- image -->

A text view has been added, which calls the changeLabel function from the
On change event. The function does not need an argument passed in since the view of
the control is always passed in as the first argument. As long as the view has the called method in
the custom function, the custom function will work with various types of views.

For more information about the available methods, see UI toolkit JavaScript API.