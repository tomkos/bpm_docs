<!-- image -->

# Versioning business state machines

- In the likelihood that your business state machine will need to
be modified over time, but its callers will not. In such a case, you
will want the existing callers to be able to seamlessly pickup the
newest version of the business state machine the moment it becomes
effective.
- You have a solution where multiple versions of the same business
state machine must coexist. Although the solution as a whole cannot
be uninstalled and reinstalled, you will need to be able to deploy
new versions of the business state machine in such a way as to ensure
that existing instances remain undisturbed, and are allowed to run
their course.

To create a version of a business state machine, it is important
that you plan ahead. Specifically, you will need to consider how the
client interacts with the business state machine, and how the business
state machine itself is set up. To allow for seamless introduction
of new versions, it is a good idea to anticipate the need ahead of
time, and set things up in the manner described in the associated
topics.

## Differentiating business state machine versions

1. same component name
2. same target namespace
3. different valid-from date

- interface specifications of different versions need to remain
the same
- correlation sets specifications of different versions need be
the same

Of critical importance, the two versions must have the
same name and namespace, but have different valid-from dates.
In addition, where applicable, they must also have the same interface,
and correlation set specifications. In other words, it is with different
valid-from dates that multiple versions of the same business state
machine are distinguished. In practice, the runtime engine could use
a new version of a business state machine that is set to become valid
today, even if an older version of that business state machine was
still being used.

## Invoking a business state machine

When a
client invokes a business state machine, that client can be configured
either to choose a specific version each time, or to pick up the currently
valid version of the business state machine. This is the basic concept
behind early binding and late binding.

With early
binding, a client is hard-wired to a business state machine
in such a way as to force a continued relationship between the two
of them, even if another version of the business state machine becomes
available. In contrast, with late-binding the relationship
between the client and the business state machine is dynamic in
that it is resolved in the runtime environment.

In other words,
if the caller instantiates a business state machine using early binding,
a specific version of the business state machine is used to create
that instance, and if they use late binding, the currently valid version
of the business state machine is used.

- Using SCA wiring

- Through the partner link extension in cases where a process that
is acting as a client calls another business state machine.

## Example

## Related concepts

- Ad hoc collaboration
- Before you begin: Client types and prerequisites

## Related tasks

- Supporting other languages

## Related reference

- Description tab: business state machine editor
- Details tab: BPEL process editor
- Details tab: business state machine editor

## Related information

- Customizing behavior with visual snippets