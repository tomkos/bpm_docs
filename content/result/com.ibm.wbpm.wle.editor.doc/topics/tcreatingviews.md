# Developing reusable views

## About this task

You can create a view by using the designer interface. The new view can be in a toolkit or in a
process application. To reuse the
view in multiple process applications, consider creating the view in a toolkit, which makes the view available to all process applications that use that
toolkit. However, keep in mind that if someone edits the view, the changes apply to all instances of
that view. Fixes can be picked up by all users of the view, but changes can also have unintended
consequences in other process applications. To limit your changes to a particular process
application, consider creating the view in that process application.

To develop more complex views, you can use sets of views that include standard user interface
elements such as text fields, images, and so on.

## Procedure

1. Click the plus sign next to User Interface and select
View from the list of components.
2. Specify the name of the new view. Unless you are basing the new view on a template, start with
a blank view.

Restriction: The name of the view must be a valid JavaScript ID with the following exceptions: it can have spaces and it cannot have
underscores. That is, you can use names like My View or
MyView, but you cannot use names like My\_View or
default; default is a reserved word in JavaScript.

After you click Finish, the editor opens the new
view.
3. To enable your view to be used in process applications that run on multiple devices, select Intended
for use on multiple devices either on the New View window when you
are creating the view, or in the Overview properties of the view after it has
been created.
4. Under Overview, provide information about the view.
For information about adding tags, documentation, and icon images, see Providing information about views.
5. Switch to Behavior and define the behavior for the view.
For information about adding behavior to your view, see Defining view behavior.
6. Switch to Variables and define the variables that the view uses.
For information about defining the data used by the view and defining how users can customize
it, see the topics Adding variables to views and User-defined events.
7. Switch to Layout and define what the view displays to users.
For information about adding views and other items to the view, see Defining the contents of views.
8. To apply a custom styling to the view instances displayed by your view, in the
Layout properties, add CSS classes and attributes as HTML properties to these
instances. Define the CSS classes and attributes in a CSS file and upload that file as an included
script in the Behavior properties. As a temporary measure, you can use the
inline CSS field to see the impact of the class and attribute definitions as you develop them.

Important: Ensure that the names of the CSS classes do not collide with the names of the
views. A collision can lead to unpredictable styling at run time because the view name is
automatically added for scoping purposes to the class attribute of the view wrapper
div.
9. Review the look of the view and how it functions. Based on the review, repeat steps 3 - 7 to
make the appropriate adjustments to the view or the items it contains or refers to. Keep iterating
through reviews and updates until you have the results that you want.
10 Test your view:
    1. In a client-side human service or heritage human service, add the view to a page.
    2. Wire the page in the service diagram.
If you cannot trace from the start node to the page, connect the page to appropriate nodes in
the flow.
    3. Bind the variables that the view uses to appropriate data.
    4. Review the configuration for the view and update it if necessary.
    5. To play the client-side human service or heritage human service in the inspector or designer,
click Run
.

- Providing information about views

You can help people use a view by making it easier to find and providing information about it.
- Categorizing views

The view palette enables you to dynamically sort and categorize views.
- Defining view behavior

You can define the behavior and appearance of a view by adding JavaScript and styles and by defining functions in its event handlers.
- Adding variables to views

You can define the data used by the view and the ways in which users can configure it.
- Defining the contents of views

You can define what a view displays to users at run time.
- Calling services from views

You can invoke Ajax services or service flows from views. The coach framework calls the services by using workflow REST APIs in taskless mode.
- Generating URLs of managed assets

Managed assets are images, style sheets, AMD modules or other assets that are part of a view, but are developed outside of the desktop Process Designer. To access these assets from a coach, you might need to use a global JavaScript function to generate the URL of the asset. For example, to generate a URL for an AMD module which is contained in a zip file.
- Generating a unique ID for a view

In some situations you might want to use the ID attribute for your DOM elements within a view. However, all DOM IDs must be globally unique. For example, during collaboration the default highlighting behavior is implemented based on a unique DOM ID. To ensure a unique ID, you can use the $$viewDOMID$$ placeholder keyword. At run time, this keyword will be replaced by the view DOM ID.