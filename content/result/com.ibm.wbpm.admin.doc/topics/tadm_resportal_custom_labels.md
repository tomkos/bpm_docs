# Customizing labels and hover helps in Process Portal

## About this task

Because Process Portal is
translated into several languages, all the strings that are used for
labels and hover help text are stored in a localization resource bundle.
The bundle contains keys for each of the strings and the string value.
When you change a label or hover help text, you must add the new string
to the resource bundle, and assign it a key. You can then use the
key when you customize the corresponding label or hover text in the
client-side human service.

## Procedure

This example shows you how to customize the Process Portal client-side
human services to change the hover help for the Main Menu button
() from "Main Menu" to "Launcher". The button is a configuration
option in the Action Bar control, which is in the RESPONSIVE\_PORTAL
client-side human service.

1. In Workflow Center, open
the Process Portal application
in the Process Designer.
2 Add the new hover text string to the Process Portal resourcebundle:
    1. In the library, click User Interface,
and then Localization Resource > ResponsivePortal.
    2. In the Translation Keys and Default Values section,
add a new key for the new hover text string. For example,
for the new hover text for the Main Menu button,
you could use newMainMenuText for the key and Launcher as
the value.
3 Customize the client-side human service:

1. On the Overview tab for the Process Portal application,
click the RESPONSIVE\_PORTAL client-side human service.
2. On the Coaches tab, click Portal to display the coach views, and
then double-click anywhere in the coach views pane.
3. Click the Action Bar coach view to display its properties.
4. On the Configuration tab, click Select for
the Left button title option, and from the
Business Data Localization Resources list, choose the key that matches
the new hover text. In this example, choose newMainMenuText from
the list. The value of the Left button title option
is now ResponsivePortal.newMainMenuText.
4. Save your changes.

## Results