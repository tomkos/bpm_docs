<!-- image -->

# Build it Yourself

## Learning objectives

- Import the Hello World Part 1 sample.
- Create an integration solution.
- Create new interfaces for the process and the human task.
- Create a new module to contain the process and human task components.
- Populate the new module with the process and human task components,
as well as the import and export components.
- Create the human task implementation.
- Create the business process implementation.

- Import the Hello World Part 1 sample

To build the Hello World Part 2 sample application, you need the Hello World Part 1 sample application in your workspace. If you did not build the Part 1 sample yourself and you did not import the ready-made version of the Part 1 sample, you should import it into your workspace now.
- Create an integration solution

When you have numerous projects, it is helpful to group related projects together using an integration solution. Integration solutions are simply "super projects" that are used to reference other projects. They enable you to more easily test a group of related projects and work with them in a team environment. To help you visualize the relationships between the projects in an integration solution, IBM Integration Designer provides an integration solution editor.
- Create new interfaces

Your business process needs an interface of its own that takes a string for the caller's gender as input and returns the final concatenated result string.
- Create a new module

A module is required to hold the components that are necessary for defining your business process.
- Populate the module

In the assembly editor for the new HelloWorldProcess module, you now need to add the business process component, human task component, and import components.
- Create the human task implementation

You will now create the implementation of the human task component.
- Create the business process implementation

You will now create the implementation of the business process component, which is more complex than the implementation of the human task.