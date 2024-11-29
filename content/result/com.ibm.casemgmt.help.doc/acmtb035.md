# Percent signs (%) and underscores (\_) do not work in case property filters

When you build a case, you can enter a string value in the in-basket widget to find work items
that contain the specified string in their property values. However, percent signs and underscores
create unexpected results if you use them in a filter value.

If you include a percent sign or an underscore in a filter value, no error message is displayed.
However, any percent sign or underscore is treated as a wildcard. Rather than returning work items
that have a percent sign or an underscore in their property values, the filter returns all work
items that have a string with any character in place of the percent sign or underscore.