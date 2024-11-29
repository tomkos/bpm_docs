<!-- image -->

# Invoking different versions of a BPEL process

A timestamp is used to determine the currently valid version of
a BPEL process on the process server. If the BPEL process is deployed
from Workflow Center as
part of a process application, the timestamp is the deployment date
of the process. For a BPEL process that is deployed by exporting an
EAR file from Integration Designer,
the timestamp corresponds to the valid-from date that is specified
for the process in the BPEL process editor, or it is set when the
process is deployed.

## Early binding

With early binding, the decision
on which version of a process is invoked is made either during modeling,
or when the process is deployed. The client always invokes the statically-bound
version of a process, even if a newer version of the process exists.

An
example of early-binding is an SCA wire. If you wire a stand-alone
reference to a BPEL process component, every invocation of the process
using this reference is targeted to the specific version of the process
component.

## Late binding

Late binding has the advantage
that clients always use the currently valid version of a process without
you having to change the client application. With late binding, the
decision on which version of a process is invoked happens dynamically
when the client invokes the process. In this case, the version of
the process that is currently valid is used. To apply late binding
to subprocesses, in Integration Designer in the
parent process specify the name of the subprocess template. This template
is used at the reference partner to choose the currently valid version
of the subprocess.

- The currently valid process template. This template is used for
new process instances.
- Process templates that are no longer valid. These templates are
still used for existing long-running process instances.
- Process templates that become valid in the future according to
their valid-from date. These process templates apply only to BPEL
processes that were deployed using Integration Designer.

- Use late binding only between BPEL processes in different process
applications, and not between BPEL processes in the same process application.
- Target processes of late binding
    - A target process must not be contained in a toolkit. A toolkit
can be deployed many times as part of different process applications.
If the toolkit contains a BPEL process, this results in different
processes with the same name that are not versions of each other.
Late binding chooses the latest deployed version of the target process
regardless of which process application it belongs to.
    - Do not use the same name for a BPEL process that is deployed as
part of a process application, and a BPEL process that is not part
of a process application unless they are versions of each other.
    - If a target process is part of a branch other than the main branch,
late binding chooses the latest deployed version of the target process
regardless of which branch it belongs to.
    - The process name must be unique across all process applications.
If two processes in different process applications have the same name,
they are considered to be different versions of the same process.
In this case, the version of the process with the latest timestamp
is chosen as the target process.