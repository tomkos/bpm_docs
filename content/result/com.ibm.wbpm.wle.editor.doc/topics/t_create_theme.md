# Creating and updating themes

## About this task

The
BPMUpdateCommand updates the target process application or toolkit snapshot with
the theme definitions of a source project. There are many ways that you can use the command but the
steps in following procedure provide a suggestion on how to use the command efficiently.

## Procedure

To create a theme:

1. Click the plus sign next to User Interface and then select
Theme.
2. Specify the name of the new theme.
3. Select whether you want to copy an existing theme from the current project or dependent toolkit
or import a theme.

Important: If you are importing a theme, ensure that it contains all the variables and
the comments and metadata. If the theme does not contain these variables and you use UI views, an
error occurs when the system generates CSS for the process application. For this reason, base your
theme on the Carbon theme or another theme that you know has all of the
variables. The variables start with bpm and they are reserved.

After you click Finish, the editor opens the new
theme.
4 In the theme editor, assign values to theme variables. The value can be a specific value, a formula, another variable, or a combination of thesetypes. For example, @bpm-neutral: #586464 defines the value to a specific colorwhile @bpm-link-color: @bpm-color-primary; defines the value with the value ofanother variable. The Design page and the Source page react to changesmade in the other. For example, you add the following variable to the Source page //|EM|{"group":"My Group","type":"color"}|DE|@my-color: #0d1122; //|EEM| Ifyou go to the Design page, you can see a My Group category that contains amy-color variable.
    - In the Design page, change the value for one or more variables. Many
variables have a swatch that you can click and then choose a value from a picker. The sample views
update to display the new values. If you hover over a view, you can see the specific variables that
affect that view and its current values.
    - In the Source page, assign a value to each theme variable that you want
to change. If you have custom views that you want to add dynamic styling to, add variables for that
styling. The variables are in Less format:@variableName: value;If you want
to display a custom theme variable in the Design page, add metadata like the
following example:
                                //|EM|{"group":"PREVIEW\_GROUP\_BASE\_SETTINGS","order":"010020","type":"color"}|DE|
@bpm-neutral-darker:  #2d3737;  //|EEM|The
group is the name of the category that contains the variable. In the example,
PREVIEW\_GROUP\_BASE\_Settings is a key to a value in a localization resource (Base
Settings) but it can be an ordinary string.

```
//|EM|{"group":"My Group","type":"color"}|DE|
@my-color:            #0d1122;      //|EEM|
```

5. Click Save or Finish Editing.

To maximize the benefits of updating the look of a process application without having to
redeploy it:

1. Create a toolkit to contain all of the themes that your process applications or toolkits will
use.
2. Create a dummy or empty process application that has a dependency on the theme toolkit.
3. For each process application or toolkit, create a dependency on the theme toolkit.
4. Deploy the process applications as well as the dummy process application.
Deploying the dummy process application also deploys the theme toolkit.
5 When you want to update the theme for all of the process applications:
    1. Update the theme toolkit and deploy a new snapshot of the dummy application.
    2. Run the BPMUpdateTheme command using the new dummy application snapshot as
the source for the new definitions.
Likely you would script using the command to update all of the running process
applications.
For information about the command, see BPMUpdateTheme command

## Results