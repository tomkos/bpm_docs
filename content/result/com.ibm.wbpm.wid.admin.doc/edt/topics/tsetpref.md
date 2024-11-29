<!-- image -->

# Setting preferences for the event definition editor

By default, the user-definable preferences for the event
definition editor are already optimized for working with event definitions.
However, in the course of your event definition tasks, you may find
that you want to change some preferences.

## About this task

- Enabling or disabling incremental validation in the event definition editor

In the event definition editor, incremental validation is disabled by default. This means that validation rules are not enforced (and validation errors are not displayed) as you work with an event definition in the event definition editor. However, when you attempt to save the event definition, validation rules will be enforced regardless of whether incremental validation is disabled. A preference is provided that enables you to choose whether you want incremental validation enabled or disabled by default.
- Enabling multiple event definition capability in the event definition editor

By default, the event definition editor enables you to create or edit a single event definition for each event definition file. Although it is generally considered a best practice to have only one event definition for each file, you can nonetheless set a preference that will enable you to add or edit multiple event definitions in a single file from within the event definition editor. This might be necessary if you are working with older event definition files that contain multiple event definitions and you want to edit them simultaneously in the event definition editor and perhaps add or remove event definitions in the file.
- Disabling prompts for generated event definitions in the event definition editor

When you open an event definition that was generated using the event definition generator rather than created using the event definition editor, you receive a prompt that warns you that any changes that you make to the event definition in the event definition editor will be overwritten the next time you use the event definition generator to regenerate the event definition. However, you can set a preference to disable the prompt.
- Enabling debug trace logging in the event definition editor

A debug trace log contains problem determination information that is helpful to IBM support personnel. By default, debug trace logging is not enabled when you are working with the event definition editor. However, you can set an event definition editor preference to enable debug trace logging.