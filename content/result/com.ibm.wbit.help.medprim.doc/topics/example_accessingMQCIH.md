# Example:
Accessing MQCIH header data

## Context

## Requirements

## Basic flow of events

1. The
MQExport receives an inbound MQ request message, or the MQImport receives
an inbound MQ response message. The message contains an MQCIH header.
2. The MQExport or MQImport uses the MQCIH header data binding to
parse the
message, and propagates the data into the SCA MQHeader.
3. Within
a mediation, the MQCIH header data can be obtained from the MQHeader.
The MQHeader has a value field, containing the MQCIH structure.

## Results