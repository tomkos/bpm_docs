<!-- image -->

# XPath extension functions for human tasks with parallel ownership

In addition to standard XPath functions described in the XPath
1.0 specification (http://www.w3.org/TR/xpath), you can use the following
functions, called extension functions, in your XPath expressions and
conditions.

- XPath extension functions for aggregating the results of human tasks with parallel ownership

Use result aggregation functions for human tasks with parallel ownership to specify how each field of the output message should be filled based on the outcome of the individual subtasks.
- Completion conditions for XPath functions for human tasks with parallel ownership

A completion condition defines when the set of subtasks that are associated with a parent task is considered to be complete. It is specified as a boolean XPath expression, which can refer to output data from finished subtasks, or other data obtained from helper functions, for example, the number of subtasks.