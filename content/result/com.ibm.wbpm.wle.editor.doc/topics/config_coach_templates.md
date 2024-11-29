# Configuring page templates for inline user tasks

## About this task

To create a custom template, you can copy the default template
into your app. Alternatively, you can use the process editor to create a new template that copies
the default template (when the UI toolkit is included in the process app), as described in the
instructions below. All templates associated with an inline user task must include the following
content boxes that will contain the generated user interface for exposed variables:

- Input Contains all inputs to the inline user task. The control ID for the
input must be TaskInput.
- Output Contains all outputs from the inline user task. The control ID for
the output must be TaskOutput.

If one or both of the control IDs are not specified, the corresponding UI will be generated
on the main page.

## Procedure

To configure a custom page template for inline user tasks:

1. Open your process.
2 Choose one of the following options:
    - If you want to configure a new custom page template that applies globally to all inline usertasks, complete the following steps: Alternatively, if one or more custom page templates already exist for inline user tasks, youcan choose Select to select an existing page template rather than configure anew one. Regardless of whether you configure a new custom page template or select an existing one,the custom page template will govern all inline user tasks in the process and override the defaultpage template from the UI toolkit.
        - Switch to Views.
        - Expand Inline Tasks and select Default View
Template.
        - Under User Interface: Inline Tasks View Template, click
New. The New Inline Task View Template wizard opens.
        - Specify a name.
        - Click Finish. The name of the new custom page template is displayed
beside the View template label.

Alternatively, if one or more custom page templates already exist for inline user tasks, you
can choose Select to select an existing page template rather than configure a
new one. Regardless of whether you configure a new custom page template or select an existing one,
the custom page template will govern all inline user tasks in the process and override the default
page template from the UI toolkit.

- If you want to configure a new custom page template that only applies to an individualinline user task, complete the following steps: Alternatively, if one or more custom page templates already exist for inline user tasks, youcan choose Select to select an existing page template rather than configure anew one. Regardless of whether you configure a new custom page template or select an existing one,the custom page template will govern the individual inline user task and override the default pagetemplate or any global custom page template that is specified in the Views page.
    - In the process diagram, select the inline user task for which you want to configure a new custom
page template.
    - Switch to General, and click New. The New
Inline Task View Template wizard opens.
    - Specify a name.
    - Click Finish. The name of the new custom page template is displayed
beside the View template label.

Alternatively, if one or more custom page templates already exist for inline user tasks, you
can choose Select to select an existing page template rather than configure a
new one. Regardless of whether you configure a new custom page template or select an existing one,
the custom page template will govern the individual inline user task and override the default page
template or any global custom page template that is specified in the Views
page.