# Event handlers for views

When a page runs, the views that it contains have a lifecycle that they follow independently.
The lifecycle consists of a number of stages with their associated event handlers. Composite views
are views that contain other views. When a composite view enters a stage, its sub-views enter the
same stage. Within a stage, however, the event handlers for the composite view and the event
handlers for its sub-views are called in a specific order.

|   Stage | Event Handlers                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       1 | load                                         | When the coach runs, the HTML is generated first and then the load() function is called to perform initialization logic, such as defining variables. The load() function is only called once. For composite views, during the load() call, each sub-view's load() is invoked before the composite view's load().                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|       2 | view                                         | After initialization is completed, the view() function is called before the user sees the view. The view() function typically performs logic to determine what a user sees when the view is rendered. For example, you can show or hide labels depending on the visibility setting. Similar to the load() function, each sub-view's view() is invoked before the composite view's view()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|       3 | change collaboration (deprecated) validation | All of the functions at this stage of the lifecycle can occur in any order and can occur multiple times. The change() function reacts to changes in binding or configuration data. If the change() function is not implemented, the view() function is called. The collaboration(event) function is called if it is implemented, when multiple people work on the same view at the same time. If collaboration(event) function is not implemented, the default collaboration view logic, which is to outline the view DOM node, takes effect. The validate(event) function is called when a boundary event occurs and its Fire Validation property is set to Before. The event is an error event or clear event. The validate(event) function uses the error event to decorate the view to show that it has non-valid data. It uses the clear event to remove the decoration. |
|       4 | unload                                       | The unload() function is called when the view is removed from the page. For example, when the user deletes a view inside a table row or clicks away from the page. The unload() function performs any required cleanup, and recursively invokes the unload() function on all sub-views. The parent view's unload() method gets called before the child view's unload() method. The unload() function is only called once.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |