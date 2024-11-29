# Business objects and variables

Each variable has its own type and scope. All variables you create must be declared before you
can start using them.

- Variable types

You can use the variable types provided by the system toolkits, such as the System Data toolkit, or you can create custom business objects, depending on the requirements of the business data included in your process.
- Variable scope

All variables declared for a process or service flow in the designer are local variables.
- Creating business objects

When no system data toolkit variable types or business objects match your specifications, you can create custom variable types called business objects.
- Declaring and passing variables

Variables capture the business data that is passed from step to step in a process.
- XSD generation pattern for business objects

When you create a business object, which is also referred to as a custom variable type, an XML Schema Definition (XSD) is generated. Understanding the generation rules and some suggestions for business object creation can be helpful when your business objects will be used with IBM Integration Designer.
- Using complex variables and lists in JavaScript

You must initialize all complex variables and all lists (arrays) before you can use them in a process, service, or service flow. After the variable is initialized, you can access and modify its properties. You can access predefined properties and functions to perform several operations.
- Creating exposed process values (EPVs)

You can create exposed process values (EPVs) to define a set of variables you want to expose to specific users. These variables can be modified by the users while instances of a process are running. For example, if you create a process to handle expense reimbursement, you may want to enable supervisors to change the allowed amounts for daily expenditures, or the dollar amount that coincides with various levels of approvers. By creating EPVs, you can provide this type of flexibility, allowing users to adjust specific variable values as constants, thereby affecting the flow of all running process instances, task assignments, and so on.
- Setting variables in pre and post assignments

You can set pre and post assignments for variables when you want to assign a value to a variable immediately before or after an activity or event runs.
- Making business data available in searches and views

Before business users can search for business data across process instances or within task lists, you need to configure each variable in the designer to be visible in Workplace or Process Portal.