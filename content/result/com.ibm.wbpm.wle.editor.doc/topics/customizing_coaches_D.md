# Specifying a custom CSS for a heritage coach (deprecated)

## About this task

The following procedure describes how to specify a custom style sheet for a heritage coach.

When you initially create a heritage coach, it uses the heritage coach CSS setting for the
process application or toolkit in which the heritage coach resides. The default heritage coach CSS
for process applications and toolkits is the coach\_designer.css file that is stored
in the System Data
toolkit.

## Procedure

1. Add the CSS file that you want to use to your current project
or to a referenced toolkit as described in Managing external files.
2. Open the service that contains the heritage coach that you want to work with and then click the
Coaches tab.
3. In the design area, click the top-level section of the heritage coach (named IBM® Business Automation Workflow Coach by default) and then click the
heritage coach option in the properties.
4. For the CSS Override field, click
the Select button and choose the CSS file that
you added in step 1. (You can click the New button
and add a CSS file as described in Managing external files.)
5. Save the heritage coach and then run the service to test the CSS overrides.