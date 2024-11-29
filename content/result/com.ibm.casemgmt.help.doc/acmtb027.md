# Unexpected results when you use different default values for the same property

## Symptoms

## Resolving the problem

Also, if you plan to use a default
value for a property, you must specify the default value for each instance of the property in the
view. Defining a default value for only one instance of a property that is used multiple times in a
view can also cause unpredictable behavior.

If you plan to set the default value in Properties
View Designer for a property that will be used in multiple instances, do not configure the default
value in Case Builder, in the case type, or by using a starting
document class. These other default value settings override the setting you specify in Properties
View Designer.