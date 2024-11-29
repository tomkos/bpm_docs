<!-- image -->

# Key concepts for BPEL business processes

Authoring of business processes is an integral aspect of IBM® Integration
Designer.
Business processes provide the primary means through which enterprise
services are integrated. Even users who do not have programming skills
can use IBM Integration Designer
to compose integrated business solutions. You can easily create and
develop a business process in an intuitive graphical programming environment
called the BPEL process editor, and deploy it to a separate runtime
environment.

- An example of a simple business process
- Transactional business processes
- Interruptible business processes
- Asynchronous business processes
- Correlations
- Compensation

## An example of a simple business process

Let
us begin with an example of a simple business process. This figure
illustrates the steps involved when a vendor sells an item to a customer.

Figure 1. A simple real-world business process

<!-- image -->

<!-- image -->

In this simple example, you have all the basic
concepts of a business process. Not every business process is this
simple. In the next few sections, the processes become more complicated,
the examples go into greater detail, and show you how business processes
can match real-life behavior.

## Transactional business processes

A
concept that you have to understand when you developing business processes
is transactions.

In the real world, a transaction
is the activity that takes place between the parties involved in a
business process that work toward the larger business goal. Sometimes,
the entire business process is considered to be just one transaction.
Other times, it is the smaller series of transactions that, when added
together, create the whole.

In fact, you have already been exposed
to a transaction. Take a look at the simple business process example
again, as shown here with a few minor additions.

Figure 2. A
simple business transaction

<!-- image -->

There are a few new terms added to the figure, the most important
of which is the term committed. This is a key concept
in understanding what a transaction is. Simply put, a transaction
is not complete until it has fully completed and the results locked
in place. Take a look at the figure again, and you'll note that at
any time before commitment, the whole process could be canceled easily
without complication. However, once it has been committed it can no
longer be undone so simply, and the actions that took place must instead
be compensated. This term will be discussed in more detail
later in this topic.

Essentially, all business processes consists
of at least one transaction, but this alone does not make a process transactional.
To be transactional, the process must be composed of a number of individual
transactions, and these transactions can be composed either of one
single activity, or a group of activities. Each activity in your process
must belong to exactly one transaction, and each activity must commit
its operation before the processing continues. The importance of transactions
relate to the concept of compensation (see below) as they are predefined
points where the business process can be stopped either to record
all accumulated activities, or to roll it back to a previous point.

## Interruptible business processes

Processes
can be interruptible in that they consist of more than one transaction,
and so are designed to pause periodically, or non-interruptible where
they run without stopping at all.

When a business process is
interruptible, it is long running, and the process will stop at specific
activities (where an end of a transaction boundary has been set) and
will not continue until an appropriate action has taken place.

When
a process is paused, it is waiting. You decide what it waits for.
For example, you may decide that it needs instruction from a human
before continuing, or you may decide that it cannot proceed until
it has specific input from a partner.

The next two examples
are interruptible business processes.

## Asynchronous business processes

As
we discussed earlier, a partner interacts with a business process
with the purpose of receiving a message in response to a request.
When this response does not come back immediately, it is called an asynchronous business
process.

Consider the following example:

Figure 3. An asynchronous
business process

<!-- image -->

In this figure, our customer is still interested in the same
object as before, but it is not physically in the vendor's store.
An order is placed for the object and rather than receiving it directly
from the vendor, the customer receives it in the mail at a later time.
In this business process, the customer sends a request to the vendor,
and the response comes from somewhere else.

For another example,
think of a synchronous process as a telephone, and an asynchronous
process as the postal system. When you are having a conversation on
the phone, you send and receive messages instantaneously using the
same connection. If you were to send the same message in a letter
using the postal service, it would be delivered in one manner, and
its response returned in another.

## Correlations

Thus far, the examples
in this topic have been fairly simple, at least as far as the vendor
is concerned. In a typical business however, a vendor will usually
be using the same business process with more than one customer, and
will often have to work with multiple customers at the same time.
With so much going on, it is easy to lose track of the status of these
interactions, so the vendor uses correlations to distinguish
the customer in their initial interaction so that they can recognize
each other in the future. A correlation is the record that the vendor
uses to keep track of multiple partners in the same business process.

Consider
the following example:

Figure 4. A business process that uses
correlations to identify customers

<!-- image -->

In this example, a customer goes to the vendor's store looking
for a specific item that is ultimately sold out. Accordingly, the
vendor issues a rain-check to the customer so that when there is sufficient
stock, the customer can return and the vendor will be able to pick
up the business process where it left off. The vendor is essentially
assigning a token to the customer that is used to identify the customer
when the transaction resumes.

It is important to note that the
vendor is able to manage multiple tasks, and does not hang in a single
business process waiting for it to conclude at the expense of all
other activity. Instead, while they are waiting for the object to
arrive, the vendor conducts similar business, using the same business
process, with other customers.

## Compensation

Compensation is an
action that is executed when a state is reached in your process that
you have deemed to be undesirable. The goal is not always to return
to a previous condition, but instead it is to maintain a balanced
and consistent state and to deal with any committed operations that
conflict with this state.

Business compensation is used in a
transactional process where an operation has already been committed,
and cannot be reversed. For example, if anything goes wrong during
the simple business transaction example, it is a simple matter of
replacing the object on the vendor's shelf, and halting all communication
between the purchaser and the vendor. If, however, the transaction
has been committed, then cancelling it is not possible and you cannot
simply return the object to the shelf and walk away.

Figure 5. Business compensation of a simple
business process

<!-- image -->

- Invocation styles

With SCA, you can invoke service components using synchronous and asynchronous programming styles. You can assemble modules into overall solutions where asynchronous channels between service components and modules can increase the overall throughput and flexibility of the system.
- Synchronous-over-asynchronous invocation

Avoid using synchronous-over-asynchronous invocation, which occurs when a component synchronously calls another component that has an asynchronous implementation.
- Choosing between long-running processes and microflows

To determine which type of process best suites your needs, you need to understand the basic differences between microflows and long-running processes.
- Working with BPEL extensions

In IBM Integration Designer you can use extensions with the existing Business Process Execution Language (BPEL).
- Invocation scenarios

You create an invocation within a service so that the service can call another service to use in your solution.
- Choosing between a BPEL process editor and a business state machine editor

You can model a Business Process Execution Language (BPEL) process application using either the BPEL process editor or the business state machine editor.
- Customizing process terminology

You can use the Business Process Execution Language (BPEL) process editor labels for activities and elements.
- Process templates

A BPEL process template is a process definition that is deployed and installed in the runtime environment.
- Process instances

A process instance is the instantiation of a process template.

## Related concepts

- Working with BPEL extensions
- Choosing between long-running processes and microflows
- Best Practice: When to not use the BPEL extensions

## Related tasks

- Compensating activities in a long-running process
- Compensating a microflow

## Related reference

- Server tab: BPEL process editor