# Overview of troubleshooting

- What are the symptoms of the problem?
- Where does the problem occur?
- When does the problem occur?
- Under which conditions does the problem occur?
- Can the problem be reproduced?

The answers to these questions typically lead to a good description
of the problem, and that is the best way to start down the path of
problem resolution.

## What are the symptoms of the problem?

- Who, or what, is reporting the problem?
- What are the error codes and messages?
- How does the system fail? For example, is it a loop, hang, lock
up, performance degradation, or incorrect result?
- What is the business impact of the problem?

## Where does the problem occur?

Determining
where the problem originates is not always simple, but it is one of
the most important steps in resolving a problem. Many layers of technology
can exist between the reporting and failing components. Networks,
disks, and drivers are only a few components to be considered when
you are investigating problems.

- Is the problem specific to one platform or operating system, or
is it common for multiple platforms or operating systems?
- Is the current environment and configuration supported?

Remember that if one layer reports the problem, the problem
does not necessarily originate in that layer. Part of identifying
where a problem originates is understanding the environment in which
it exists. Take some time to completely describe the problem environment,
including the operating system and version, all corresponding software
and versions, and hardware information. Confirm that you are running
within an environment that is a supported configuration; many problems
can be traced back to incompatible levels of software that are not
intended to run together or have not been fully tested together.

## When does the problem occur?

Develop a detailed
timeline of events leading up to a failure, especially for those cases
that are one-time occurrences. You can most simply do this by working
backward: Start at the time an error was reported (as precisely as
possible, even down to the millisecond), and work backward through
the available logs and information. Typically, you need to look only
as far as the first suspicious event that you find in a diagnostic
log; however, this is not always simple to do and takes practice.
Knowing when to stop looking is especially difficult when multiple
layers of technology are involved, and when each has its own diagnostic
information.

- Does the problem happen only at a certain time of day or night?
- How often does the problem happen?
- What sequence of events leads up to the time that the problem
is reported?
- Does the problem happen after an environment change, such as upgrading
or installing software or hardware?

Responding to these types of questions can provide you
with a frame of reference in which to investigate the problem.

## Under which conditions does the problem occur?

- Does the problem always occur when the same task is being performed?
- Does a certain sequence of events need to occur for the problem
to surface?
- Do any other applications fail at the same time?

Answering these types of questions can help you explain
the environment in which the problem occurs and correlate any dependencies.
Remember that just because multiple problems might have occurred around
the same time, the problems are not necessarily related.

## Can the problem be reproduced?

- Can the problem be re-created on a test machine?
- Are multiple users or applications encountering the same type
of problem?
- Can the problem be re-created by running a single command, a set
of commands, a particular application, or a stand-alone application?