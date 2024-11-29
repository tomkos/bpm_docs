# Defining view behavior

## Procedure

Switch to Behavior to define the functionality and appearance of
the view:

- Add dynamic styling to control the appearance of the view.
Dynamic styling combines a Less style sheet with style definitions that are set in the parent,
which is typically the process application. For information about the Less language, see http://lesscss.org/. The combination of the Less stylesheet and the style definition generates
runtime CSS files. The runtime CSS files are used to display the view instances in the process application. By setting the
definition values at the container level, the view instances within that container can have
consistent styling. Additionally, global changes to that style can be made from one location.
- Add existing script and style sheet files from the library by using included
scripts. Typically, these files are reusable .js and
.css files. You can add these files to the library as individual web files or
package them in a .zip file and add that file as a web file. Packaging the
files in a .zip file means that they maintain their relative relationships. For
example, if you package a .css file and include the images that it refers to
using relative links, the system finds the images. However, the system does not find the images if
you package a .css file in one .zip file and package the
images that it refers to in a different .zip file. If you add
.css files as individual web files, you can edit them in the designer.
However, you cannot edit .css files that are packaged in a
.zip file. Instead, you must edit them externally, repackage them, and then
replace the .zip web file with your updated .zip
file.
- Prototype the CSS needed to style the view by using inline CSS. After you have developed theCSS, copy it to a .css file and import that file as an included script. Because inline CSS class names are global, there could be name collisions that result in onlythe last style definition being applied. For this reason, use inline CSS as a temporary place todevelop the CSS styles for your view. If you are pointing to an image file in a.zip file, use the following format for the URL:file .zip !path /file .extension .Note: The'! ' notation to reference a file inside an archive is supported only in inline CSSbehavior. When you are working in the designer, the view styles specified in.css files and inline CSS are applied to the view in theLayout properties, allowing you to see how the view will appear at run timewithout having to run or test your view. There are a few restrictions on this design-time stylingsupport: If you have large or complex coaches and views, the design-time application of stylesmight cause some performance issues. To disable design-time styling for the current session, switchto Layout , right-click anywhere on the canvas and select Disabledesign-time styling . For the rest of the session, the specified view styles are notapplied. To turn design-styling back on for the session, right-click on the canvas and selectEnable design-time styling .
    - If you use media query statements in your CSS, only media queries with a media type
screen are parsed and only the max-width and
min-width specifications are applied at design time. This design-time styling only
supports simple syntax, for example, the following media type statements are processed at design
time:@media screen ….
	@media all
	@media (min-width: 520 px ) However, the following statements are not processed at
design time: @media not screen
@media not print
@media not (tty and screen)
    - Imports within included scripts and inline CSS will only be processed to one level of embedding.
For example, if you have inline CSS that includes the statement @import
url('File1.css'), then the css within File1 is reflected at design time,
but any import statements inside File1 are not reflected at design time.

If you have large or complex coaches and views, the design-time application of styles
might cause some performance issues. To disable design-time styling for the current session, switch
to Layout, right-click anywhere on the canvas and select Disable
design-time styling. For the rest of the session, the specified view styles are not
applied. To turn design-styling back on for the session, right-click on the canvas and select
Enable design-time styling.

- Add conditional styling to handle differences between browsers and mediatypes. The conditional styling overrides the default styles when the conditionapplies. For example, you can apply one .css file for Microsoft Internet Explorer and a different .css file for other browsers.You use conditional styling to apply the appropriate file. To add conditionalstyling: You can also add conditional styling by adding inline JavaScript and inline CSS. Note: Any inline JavaScript styling and anystyling conditions entered in the IE Condition andMedia fields are only processed at run time and are not reflected at designtime.

1. Add screen size-specific styling or browser-specific styling to a
.css file. For example, you can add styles for tablets to use a
smaller font for labels and reduce padding.
2. Add the .css file as an included script.
3. In the IE Condition or Media fields, add the
condition that applies the styles in the .css file. 
For example, if the .css file contains styles for a tablet
presentation, add a condition like screen and (max-width: 600px) to the
Media field. If the user's screen is 600 pixels or less in width, the view
uses the styles in the .css file instead of default values.
- Add custom Dojo build layers to improve the performance of the view.
For information, see Improving the performance of views with Dojo build layers.
- Define common variables and functions for the event handlers of the view by using inline JavaScript.
For information about accessing parts of the DOM, see Accessing a child view by using a control ID. The editor
contains a code snippet. The editor does not show validation messages for code snippets.
- Define variables that identify user-defined event handlers. For more information, see the topic
User-defined events.
- If your view requires modules that are written in the AMD style, register the aliases for the
dependent modules by using AMD dependencies.
Script functions can then use these aliases to refer to the modules. For information about
registering AMD modules, see Adding custom AMD modules. For an example of using dependent modules, see Example: creating a control using custom HTML.
- To insert code like <meta> tags into the header of the view, use
Header HTML.
- If necessary, define the functions that the view uses in the appropriate event handlers. 
For more information, see Event handlers for the view object and the load event handler code in Example: creating a jQuery button view. If you selected Can Fire a Boundary Event in
the Overview properties, add code to fire the boundary events. To fire the
event, code the JavaScript to call
this.context.trigger(callback) at the appropriate time.

- Improving view performance

To improve the performance of a view, you can add custom Dojo build layers to it.
- Adding custom AMD modules

You can use custom AMD (Asynchronous Module Definition) modules in your views.
- Accessing a child view

The control ID is the unique ID of the control within the parent view. You can use the control ID to access a subview instance at run time.
- Configuring the design-time appearance of views

You can configure views to enhance the design-time experience for other interface developers who are reusing your views. By including icons and preview images, or for more advanced configurations, custom HTML and JavaScript, you can customize the appearance of your views to help interface developers visualize how the view will appear at run time.