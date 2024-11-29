# Event handlers

You can customize an event handler in the Behavior page of a view.

- The load event handler

The load function performs initialization logic before the view loads.
- The unload event handler

The unload function performs cleanup after the view has completed. The unload function is only called once during the lifecycle of the view.
- The view event handler

This view function performs logic such as populating the view with data before the user can see the view.
- The change event handler

The change function is called when there is a change in binding or configuration data.
- The collaboration event handler (deprecated)

The collaboration function overrides the default UI feedback behavior when multiple people work on the same view at the same time. In addition, any custom collaboration event fired during a collaboration session is delivered to the collaboration function, as the default behavior does not handle any custom collaboration events.
- The validate event handler

The validate function handles validation errors that are caused by the data in the view.