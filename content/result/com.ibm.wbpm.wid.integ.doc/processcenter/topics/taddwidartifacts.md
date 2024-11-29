<!-- image -->

# Making operations visible to process applications

## About this task

For example, you may have an operation that provides business
intelligence data on a subject linked to a process application. By
making the operation visible, the process application can now use
that data.

## Procedure

To make operations visible to a process application,
complete the following steps:

1. Associate the module that contains the operations with
the process application.
2. Open the assembly editor and select an SCA export (that
is, an export with an SCA binding) that contains the operations that
you want to make visible to the process application.
3. In the Properties view, select the Binding tab.
Select the Make operations visible to IBM Process Designer check
box. All operations become visible.
4. Save your work. Once you use Refresh and Publish on
the process application or toolkit, a corresponding Advanced Integration
Service will be created in Process Designer which can be used in the
Process Designer business process. Note that deselecting
the check box removes the implementation.
You should read the Limitations when working with process applications and toolkits section as there
are some restrictions on implementations used with Process Designer.