<!-- image -->

# Service Business Exception handling

Service Business Exceptions are defined on the service interface.

Component developers should take care to declare the possible exceptions
that may be thrown, so that the consuming service can handle them.
For example, a business fault to a banking application would include Invalid
Account Number, or Insufficient Funds as business exceptions.
So the application that calls the service needs to include logic to
handle a situation where they have passed in an invalid account number,
or where they tried to transfer $100 but there was only $50 in the
account. These are the types of business errors that a calling application
is designed to handle. The IBM® Integration
Designer business
exceptions are returned to the client to catch and handle appropriately.

When handling business service exceptions, service consumers should
implement the client such that it will perform one of the following
actions for a declared business exception:

1 Catch the exception and create the appropriate Service BusinessException for the calling application. This could mean includingthe original exception in the new exception (wrapping it). This ismost often done when the calling module does not have the same BusinessExceptions as the service that it is calling. Here is an example ofthe flow catching an exception and creating a Service Business Exceptionfor the calling application:
    1. Module A has SBE MoneyTransferFailed
    2. Module B has SBE InsufficientFunds
    3. Module A calls Module B and
gets InsufficientFunds exception
    4. Module A must create a new exception MoneyTransferFailed,
which may have a place where a string defining the original error
of insufficient funds can be included.
2. Catch the exception and perform alternate logic.