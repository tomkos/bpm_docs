# Enabling optimization for coaches

## About this task

As an example, for human services that are
exposed as dashboards whose content is mostly read-only, the enabled coach optimization ensures that
no data is sent back to the server to be processed. For a more complex content, where both read-only
and editable content is displayed in the user interface, the enabled optimization ensures that only
the coach variables that are changed by the user are sent back and processed. No data is sent back
for the read-only content.

- Use the isOptimizeCoachBoundaryEvent setting only with heritage human
services.
- Initialization of variables by the framework when a coach is loaded is not considered a user
change. Therefore, initialization changes to formerly uninitialized variables that receive an
explicit default value when the coach is loaded are not sent back for processing.
- For correct coach modeling, it is recommended that you do not rely on the
coach initialization of variables. Instead, you should explicitly initialize all the variables that
are bound to coaches to the appropriate default values. Alternatively, you can make adjustments for
the fact that variables might not be initialized after the coach step in the human service.

## Procedure

To enable the coach optimization, complete the following steps:

1. Open the administrative console and click Resources > Resource Environment > Resource Environment Provider
2. On the Resource environment providers page,
click Mashups\_ConfigService.
3. Under Additional Properties, click Custom properties.
The list of custom properties opens.
4. Click New to add a new property
with the name isOptimizeCoachBoundaryEvent.
5. Set the value of the new isOptimizeCoachBoundaryEvent property
to true, and then click OK.
6. Save your changes to the master configuration.
7. Restart the application server instance.

## Results