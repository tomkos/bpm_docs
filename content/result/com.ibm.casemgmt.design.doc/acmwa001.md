# Configuring your environment to show display names in Case Client

## About this task

The following widgets and dialogs can show a user's display name when the option for showing the
display name is enabled:

- In-basket widget
- Case List widget
- Document and History tabs in the Case Information widget
- Properties widget
- Timeline Visualizer widget
- Comment history in the Add Comment dialog
- Custom Activity Editor dialog

Dialogs for reassigning users can also show the user's display name.

## Procedure

1 Enable the Show the display name setting in the Case Client plug-in:
    1. From the Administration View of IBM Content
Navigator, click
Plugins > Business Automation Workflow Case client
plug-in.
    2. Click Edit to open the configuration section for the
plug-in.
    3. In the configuration section, select Show the display name instead of the
login name.
    4. Save your changes.
2. Configure the appropriate User Display Name Attribute in Content Platform Engine for the directory provider
attribute that corresponds to the display name that you plan to display at run time. For example, a
common directory provider attribute that stores a display name for the user is
displayName. For more information about how to configure the
User Display Name Attribute for your directory provider configuration, see
Directory service providers in the Content Platform Engine documentation.