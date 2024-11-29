# Synchronous Transaction Rollback mediation primitive

## Introduction

The Synchronous Transaction
Rollback primitive has one input terminal (in),
one output terminal (out) and one fail terminal
(fail).  If you start the mediation flow using
a synchronous invocation style and the  Synchronous Transaction Rollback
primitive is called, the current transaction is rolled back, the out terminal is fired,
and flow processing continues. If you start the mediation flow using
an asynchronous invocation style and the Synchronous Transaction Rollback
primitive is called, the fail terminal is fired
and an error shows which indicates that the Synchronous Transaction
Rollback primitive has been called in an asynchronous flow. In this
case, the transaction is not rolled back.

Another way of rolling
back a transaction in a mediation flow is by using the Fail primitive,
which stops the flow and sends an unmodelled fault back to the client. With the
 Synchronous Transaction Rollback primitive, you explicitly roll back
the transaction and flow processing continues.

## Usage

Use the Synchronous Transaction Rollback
primitive if you want to explicitly roll back the current transaction
in a mediation flow, as part of an error handling routine. For example,
if an error has occurred when calling out to a target service, the
Synchronous Transaction Rollback primitive can be used to roll back
a change made to a database before the callout failed, and a modeled
fault can be returned to the client.

You can
use the Synchronous Transaction Rollback mediation primitive to roll
back the current transaction under certain conditions. For example,
if you wire an output terminal of a Message Filter mediation primitive
to a Synchronous Transaction Rollback mediation primitive, the transaction
is rolled back if the filter condition occurs.

- Synchronous Transformation Rollback mediation primitive properties

The Synchronous Transaction Rollback mediation primitive has no properties.