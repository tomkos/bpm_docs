<!-- image -->

# Implementing an Advanced Integration service

When you implement an Advanced Integration service, you decide
where the implementation is located. The location impacts how the
service is managed and deployed. You can generate the implementation
in a separate module from the toolkit or process application that
contains the service definition. Or, you can generate the implementation
in the same process application or toolkit as the service definition.
For more information, see the article Implementing the facade pattern using IBM BPM Advanced.

Keeping the implementation in the same module is consistent with
releases earlier thanBusiness Automation Workflow 8.5.6.
This pattern is also useful if you want the advanced services versioned
along with the process application.

Separate the implementation from the service definition if you
want to keep Process Designer logic
separate from Integration Designer logic,
so that automatic deployment does not impact Process Designer logic.
To call a BPD, you must follow the steps for a stand-alone module
as described in Creating an import to start a BPD in a stand-alone module. Also,
you must manage your own deployment and versioning. For more information
on versioning, see Versioned modules and libraries

- Implementing an Advanced Integration service in a separate module

If you have defined an Advanced Integration service (AIS) in a toolkit, you can choose to separate the implementation of the AIS from the service definition by using a wizard to create the basic components that you need.
- Implementing an Advanced Integration service in the same process application or toolkit

If a process application in your workspace requires an Advanced Integration service (AIS), you can use a wizard to create the basic components that you need. You can choose to generate the implementation in the same process application or toolkit as the service definition.