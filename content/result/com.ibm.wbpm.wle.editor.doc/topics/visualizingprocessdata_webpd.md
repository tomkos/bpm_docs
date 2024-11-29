# Visualizing process data

A process uses variables and business objects to contain the data that flows in and out of its
activities. When you design a process, you can map the local variables and apply tag groups to
elements of a process, and you can create a visual representation of this data for the process. A
tag group is a key-value pair that you can use to associate a service in a process. The procedure
for defining tag groups is similar to the procedure for defining regular tags. However in a tag
group, a group of similar and related values can be grouped together under a single key. For
example, the various stages in a software development lifecycle such as In
development, Available, and Retired can be created under
the group Lifecycle Stage.

Tag groups are displayed as labels above the activities in the data visualization diagram. The
tag groups are applied to services within a process. All the activities that are mapped to the
tagged services are displayed with appropriate labels in the diagram. The activities in the selected
process that use the same tag groups display same-color labels. Where an activity is mapped to more
than one tag group, the labels that contain the tag group are stacked above each other in a tab. You
can click the tab to display all the labels above an activity.

You can click a subprocess within a process in the data visualization diagram to visualize that
subprocess. The parent process and all its subprocesses can be displayed according to breadcrumb
selections at the top in the browser window.

- Visualize process data variables

Select and visualize the local input, output, or private variables used in a process.
- Visualize process tag groups

Select and visualize the tag groups defined for a process.