<!-- image -->

# Creating versions of your process to be used with SCA components
and exports

## About this task

<!-- image -->

This diagram shows how to construct a system
that will allow you to work with versions of a BPEL process in a system
where SCA wiring is used. The key to this solution is a proxy process that
is a BPEL process that acts as a connection (or intermediary) between
the caller and the long running process that will potentially be versioned.
The caller uses early binding to invoke the proxy process, the proxy
process uses late binding to invoke the actual process. Thus the interaction
between the caller and the actual process is implicitly late bound.
When there are multiple versions of this process in the runtime environment,
the proxy will automatically link to the most recent one.

Follow
these steps to create a proxy process for the actual process, and
then eventually create a new version of your process by copying its
enclosing module and adjusting its valid-from dates. These steps assume
that you have already created the BPEL process that you seek to version.

## Procedure

1 Create a proxy process as follows:
    1. Create a BPEL process that will only invoke an operation
on the long running process that you will be versioning, and then
return a response from it.
    2. Late-bind this proxy to your existing process (the one
that you intend to create a version of), by adding a new Reference
Partner to it. Then, click the Description tab,
and enter the component name of your process in the Process
Template field. This step will likely cause
a CWSCA8015W warning that you can safely ignore since
this target will by dynamically selected in the runtime environment.
    3. In the Assembly editor, wire the appropriate caller
to the new proxy process. This may be an SCA export, a
stand-alone reference, or another SCA component within this module.
If the caller is another process (within the same module, or in a
separate module) the proxy process is not needed as it can directly
use late binding.
2 Make sure that the actual process is exported if it iscalled by the proxy process across module boundaries. If an SCA exportis needed, add it as follows: This is all that is needed to create the version. Whenit is actually needed, proceed with the final steps in this topicas shown below.

1. Open your process in the Assembly Editor.
2. In the Assembly Diagram, right-click the process and
select Generate Export > SCA
Binding.
3. Save your work, and close the editor.
3 Make a copy of the module that contains the original versionof your process as follows:

1. Close all editors.
2. In the Business Integration view,
right-click the module and select Copy.
3. Right-click any white-space within the same view, and
select Paste.
4. Save the file. The new module name appears
in the assembly editor.
4 Configure a date from which the copied BPEL process willbe valid, as follows:

1. In the new copy of the module, open the BPEL process
in the editor, and click an empty area to choose the process as a
whole.
2. In the Details tab of the properties area, enable Select
date (UTC) when the process becomes valid. If
this check box is clear, then a valid-from date is implicitly specified
so that the process becomes valid as soon as the module is installed.
3. Configure the calendar fields to specify the date and
time when the runtime engine is allowed to create instances of this
process. Calendar values are represented in Coordinated
Universal Time (UTC).
5. Save your work.
6. You can deploy this new module as you would any other module.

## Example