# Form widget (deprecated)

The Form widget incorporates forms that are
designed in a form application such as IBM® Forms. To use the Form widget,
you must configure it to use a specific form template (or localization
proxy) or to use a form attachment (a form data document, form template,
or localization proxy). You can also edit the settings for the Form
widget to customize event handling for the widget.

You can configure more than one instance of this page to create a page for each step (work item)
of an activity. Or, you can use the same page for each step, depending on your requirements. If you
want to use a different configuration for each step in an activity, make copies of the appropriate
IBM Business Automation
Workflow page, and then configure a copy for
each step.

You can wire the Form widget to a custom widget so
that the custom widget can read and write property values. You can
also use the Form widget on a page that contains the Properties widget.

## IBM Business Automation
Workflow pages that include this
widget by default

You can configure more than one instance of this
page to create a page for each role. For example, you can configure
a page for a case worker and another one with different fields for
a manager.

- Configuring the Form widget to use a form template (deprecated)

When you configure the Form widget to use a form template, workers can use the widget to create a case or to view and modify the property values for a case or step (work item). The data in the form is mapped to step parameters and case properties. A form data document is not saved.
- Configuring the Form widget to use a form attachment (deprecated)

When you configure the Form widget to use a form attachment, workers can use the widget in place of the Properties widget to view and edit the property values for a step (work item). When the worker completes or saves the step, a form data document is saved and attached to the step. You can configure the Form widget to use a form attachment only when you use the Form widget on the Form Attachment Work Details page in the Step Pages space.
- Form widget events (deprecated)

The Form widget publishes and handles events to display case and work item properties in a form for users to view and edit.