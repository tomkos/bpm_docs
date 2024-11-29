<!-- image -->

# Limitations of batch testing in headless IBM Business Automation
Workflow

Some known limitations are:

- Problems in testing component test projects there were created
before Version 7.0
- Problems in testing component test projects that reference adapter
bindings

These limitations are discussed in the following sections.

## Problems in testing component test projects that were
created before Version 7.0

The serviceDeploy command does
not recognize IBM Integration
Designer component
test projects that were created before Version 7.0. As a result,
the command will not generate the Java source files that are required
for deployment.

When you import a version 6.2 or 6.1.2 component
test project into Integration Designer, or when
you open a 6.2 or 6.1.2 workspace with a component test project, the
project will automatically be migrated to version 7.0 and serviceDeploy
will successfully build the project.

## Problems in testing component test projects that reference
adapter bindings

The serviceDeploy command does not generate
the required Java source files for component test projects that reference Integration Designer adapter
bindings.

To perform batch testing of component test projects
that reference adapter bindings, use Integration Designer to package
and export your application, as described in the topic Using Ant scripts for testing in headless IBM Integration Designer and
its subtopics.