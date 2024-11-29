# Example: applying a custom theme

By default, a new process application uses the Carbon theme. This theme
contains all of the definitions used by the UI views. This example creates a theme that is based on
the Carbon theme and modifies two variables to change the appearance of many
views. The example then opens the Hiring Sample to change its theme to the new custom theme to
demonstrate how changing the theme changes how the Hiring Sample looks.

1. Open the Hiring Sample in the Process Designer.
2. Create a theme called Custom Theme by copying the
Carbon theme. For information, see Creating
Themes.
3. In the Design page of the theme editor, change the following
variables:
Table 1. Variable changes for the Custom Theme

Variables
Old Value
New Value

@bpm-color-primary in Base Settings
#0062ff
#277554

@bpm-input-bg in Forms
#f3f3f3
#d9ece3

The example views update to show the effect of these changes. For example, the example
button is now green.
4. Click Save or Finish Editing.
5. Open the process app settings for the Hiring Sample. In the Coach Designer
Settings section, change the theme to the new theme and then save your change. The save
triggers generating the CSS that Process Designer
uses to display the views in the layout.
6. To see the effect of changing the theme, open the Create Position Request client-side human
service and then open the Create position request page. The CSS generation takes time so a delay
might occur before you see the effect, which looks like the screen capture:

<!-- image -->