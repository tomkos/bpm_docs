# Framework managed versus view managed content for coaches

There are times when you might want to override the default behavior of the framework when a
coach is rendered. For example, when a view is bound to data that is an array, the framework creates
a view for each index element in the array. You might want to create views for a different set of
elements, in which case you can choose the option to let the view manage its own content.

1. Open the view, and switch to Layout.
2. Click the content box on the editor.
3. Under Properties, click the option The View will manage its own
content.
4. You can write your custom code in a callback method such as load() to manage
the content. For more information, see View managed coaches

## Framework managed content

- If the content box inherits a data binding that is an array, the framework clones the DOM node
of the content box n times where n is the number of elements
of the data binding array. A view is created inside the content box for each index element in the
array.
- If the content box inherits a data binding that is not an array, the framework creates views for
the enclosed contents.

## View managed coaches

1 Initialize and render the sub-views:
    - If the content box inherits a data binding that is an array, the view typically does thefollowing in one of its callback methods, for example load() :
        - The view deeply clones the DOM node of the content box n times, where
n is the number of elements of the data binding array.
        - Performs initialization logic as required, for example add/remove/update/decorate the content
of the cloned node.
        - Invokes the framework method this.context.createView()
- If the content box inherits a data binding that is not an array, the view does the following inone of the its callback methods, for example load() :
    - Performs initialization logic as required
    - Invokes the framework method this.context.createView()
2 Add/delete content dynamically:

- Add content (for example add new row in table)
    - Create the new binding object and add it to the binding array using DataBinding API
    - Invoke the framework method this.context.createView()
- Delete content (for example delete row in table)

- delete the binding object for that row directly or indirectly
- Invoke the framework method this.context.deleteView()