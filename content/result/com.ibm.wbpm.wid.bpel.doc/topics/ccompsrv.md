<!-- image -->

# BPEL process compensation

Compensation has at times been described as a means of undoing
an action, but this isn't necessarily accurate. More specifically,
it is a service that is executed when a state is reached in your process
that you have deemed to be undesirable. The goal is not always to
return to a previous condition, but instead it is to maintain a balanced
and consistent state and to compensate for any committed operations
that conflict with this state.

There are two types of compensation: business compensation which
occurs outside of a transaction, and technical compensation that
occurs within.

## Business compensation

- This type of compensation is used in a long-running process where
an operation has already been committed, and cannot be reversed. Business
compensation is another operation that, when executed, will create
a balanced state where both business partners are satisfied.

- For example, if something goes wrong at any time during a typical
business transaction such as the one described in transactional processes,
it is a simple matter of replacing the object on the store shelf,
and halting all communication between the purchaser and the vendor.
If however, the transaction has been committed (money has been exchanged
and a receipt issued), then cancelling it is not possible, as it has
already taken place. You cannot simply return the object to the shelf
from whence it came. A completely different procedure (a refund) must
take place to return the conditions to a balanced state. The operations
that have already taken place have to be compensated for in order
to return to a situation in which both partners are satisfied. It
is not necessarily exactly the same state that existed before (for
example, if the customer paid in cash, they may receive a store credit
in return), but nonetheless it is one that is balanced and consistent.

- If either the customer or the vendor are unhappy, then business
compensation has not been successful.

## Technical compensation

- Technical compensation is used in transactions that fail before
they have been committed and one of the operations cannot be reversed
by the transaction rollback. For example, imagine that, in the example
described in transactional processes, the customer had requested that
the object be personalized in some way. The vendor complies, but before
money is exchanged, something unexpected happens, and the transaction
is canceled. The object cannot simply be returned to the shelf, another
procedure must be executed to take into consideration the personalization
that took place.

- In another example, imagine that in your process, one of the
activities within a transaction sent out an email, but the transaction
was canceled before it was committed. You cannot undo the sending
of an email, so you must compensate in some other way.

## Choosing the appropriate compensation for your business
process

There are two ways in which you can compensate a
BPEL processes. Here are some suggestions on how to choose the one
that is best for you.

- If you do not have IBM® extensions
enabled for this process, then you CANNOT USE compensation pairs and
MUST use a compensation handler. The compensation tab in the business
process editor is an IBM enhancement
of the BPEL programming language, and so will not be available if
this option was disabled when the process was initially created.
- You cannot use a compensation handler with a microflow. Since
microflows run within a single transaction, you must use the compensation
tab of the BPEL process editor to store the original properties of
each invoke activity in the event that the process fails.

So, if you are designing a long running process, then
you can use either of these options. If the compensation characteristics
of each activity are fairly simple (in that compensation can be achieved
in a single step), then consider using compensation pairs for each
of these activities. If, however, you require compensation that makes
use of more complicated logic, asign a compensation handler to each
activity, and populate it with the necessary objects.

## Example

- Compensating activities in a long-running process

In a long-running process, each transaction within it is committed individually. To set up compensation, you need to specify how to deal with each activity should it fail.
- Compensating a microflow

In a microflow, the entire process executes within a single transaction. To set up compensation for a microflow, you store the original properties for each of the invoke activities within the microflow so that the original data can be restored if the process cannot be committed and must be rolled back.
- Choosing the appropriate compensation for your process

There are two ways in which you can compensate a business processes. Here are some suggestions on how to choose the one that is best for you.
- Working with BPEL extensions

In IBM Integration Designer you can use extensions with the existing Business Process Execution Language (BPEL).
- Best Practice: When to not use the BPEL extensions

The BPEL extensions exclusive to the IBM Integration Designer BPEL process editor provide such a significant enhancement to the BPEL language that you may wonder why not to use them. Here are some possibilities.

## Related concepts

- Fault activities
- Raising faults
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Using fault handlers
- Continue processing upon unhandled faults
- Typing fault variables