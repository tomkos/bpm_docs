# Stop mediation primitive

## Introduction

The Stop mediation primitive
stops a particular path in the flow.

The Stop mediation primitive
has one input terminal (in) and no output terminals.
The input terminal accepts messages and consumes them without generating
any exception information.

## Usage

You can use the Stop primitive to
stop a particular path through a mediation flow, without generating
an exception; the message is consumed by the runtime environment with
no further processing. Wiring a normal output terminal to a Stop primitive
results in the same runtime behavior as leaving the terminal unwired;
wiring a fail terminal to a Stop primitive
causes exceptions to be silently consumed, rather than propagated.

- Stop mediation primitive properties

The Stop mediation primitive has no properties.