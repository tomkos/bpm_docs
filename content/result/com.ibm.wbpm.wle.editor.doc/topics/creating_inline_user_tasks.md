# Working with inline user tasks

## About this task

## Procedure

1. Create a process. An inline user task is automatically generated and is wired into the
process.  
The UI generated for an inline user task is based on the default page template that is included
in the UI toolkit. However, you can configure a custom template to modify the inline user task.
Information about templates for inline user tasks is found in the topic Configuring coach templates for inline user tasks.
2. If you need another inline user task, select it from the palette and wire it into the
process.
3. Go to Variables, and create the required input, output, and private
variables. These variables will be used to simultaneously create the interface and data map for the
inline user task. See Variable types.
4. In the process diagram, select the inline user task and then open the Data
Mapping properties. At this point, the properties content differs from that of a regular
user task because there is no interface yet.
5 In the Data Mapping properties, add input and output variables and definethe interface by completing the following substeps: You can expose a process variable as an input, output, or both. Input variables will begenerated as read-only fields in the UI.Note: When you select a child parameter of a variable for aninput or output mapping, the parameter is mapped to or from the ANY type. If the inline task isconverted to a stand-alone implementation, the type of the generated variable will be replaced withthe actual data type at the time of the conversion. Note: Inline user task pages areautomatically generated for the variables. If you change a variable in theVariables page, the variable is automatically changed in the DataMapping properties. Any changes to the mapping causes a regeneration of the affected pagein the backing client-side human service.
    1. Beside the Input Mapping section, click the Add a new
input icon (+) to add the input variables. This opens a list of
the variables that you defined.
    2. In the list, select a variable. It is added under the Input Mapping
section.
    3. If you need to add more variables to the input mapping, click the Add a new
input icon (+) again. (You can delete any input variable from the
mapping by clicking the X icon to the right of the variable name.)
    4. Beside the Output Mapping section, click the Add a new
output icon (+) to add the output variables. This opens a list of
the variables that you defined.
    5. In the list, select a variable. It is added under the Output Mapping
section. (You can delete any output variable from the mapping by clicking the
X icon to the right of the variable name.)
    6. If you need to add more variables to the output mapping, click the Add a new
output icon (+) again.

## What to do next

- Configuring page templates for inline user tasks

The user interface (UI) generated for an inline user task is governed by the data that is exposed to the task as well as the page template that is associated with it. The generated UI is based on the data types that are exposed to the inline user task with a layout based on the provided template. The default template included in the UI toolkit is used or a custom template can be configured for the process or individual task.
- Converting inline user tasks to use stand-alone implementations

When you have finished adding inline user tasks, you can convert one or more of them to use a stand-alone implementation. This is especially useful for developing advanced user interfaces. Essentially, this transforms an inline user task into a regular user task with an associated and editable client-side human service.