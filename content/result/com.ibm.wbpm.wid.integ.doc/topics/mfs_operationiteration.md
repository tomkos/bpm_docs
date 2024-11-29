<!-- image -->

# Operations and iterations of a conversation

Each iteration in a conversation is an operation in
the BPEL process mediation flow. Each operation has an input and an
output. Each input or output has a specific data type. For MFS applications,
the data types are generated from the message input descriptors (MIDs)
and message output descriptors (MODs) in your MFS source file. You
then create additional data types that contain information about the
conversation ID (the value of the convID property) and whether the
conversation has ended (indicated by the convEnded property value).

- The output of each iteration, in addition to passing the data
to the next iteration, must also pass along the conversation ID.
- The input to the last iteration must indicate that the conversation has ended.

To demonstrate the concepts, assume that you have the following
MIDs (IVTCBMI1\_Page1 and IVTCBMI2\_Page1) and MOD (IVTCBMO2) that are
generated as data type business objects from the IMS phonebook sample. Assume that you are creating
a mediation flow with three iterations, each with the following input
and output:

| Iteration (operation)   | Input          | Output   |
|-------------------------|----------------|----------|
| First iteration         | IVTCBMI1\_Page1 | IVTCBMO2 |
| Second iteration        | IVTCBMI2\_Page1 | IVTCBMO2 |
| Final iteration         | IVTCBMI2\_Page1 | IVTCBMO2 |

To start a conversation, the useConvID property must be
set to true. In order to uniquely identify the conversation in all
iterations, the conversation ID (the convID property) must be made
available to the business context. In addition, subsequent iterations
must be able to retrieve the convID value from the context. To end
a conversation, the conversation ended (convEnded) property must be
set to true. The property might be set by the client application,
or when the last iteration is called.

- At the end of the first iteration, the output includes the convID
information.
- Subsequent iterations retrieve the convID information from the
context as the input.
- Before the last iteration, the convEnded information is added
to the output for the client application to indicate to the last iteration
that the conversation has ended.

| Iteration (operation)   | Input                  | Output                      |
|-------------------------|------------------------|-----------------------------|
| First iteration         | IVTCBMI1\_Page1         | IVTCBMO2, convID            |
| Second iteration        | IVTCBMI2\_Page1, convID | IVTCBMO2, convID, convEnded |
| Final iteration         | IVTCBMI2\_Page1, convID | IVTCBMO2, convEnded         |

- A PersonIn2 data type is created to hold IVTCBMI2\_Page1 and convID
- A PersonOut data type is created to contain IVTCBMO2, convID,
and convEnded

| Iteration (operation)   | Input                              | Output                                  |
|-------------------------|------------------------------------|-----------------------------------------|
| First iteration         | IVTCBMI1\_Page1                     | PersonOut (IVTCBMO2, convID)            |
| Second iteration        | PersonIn2 (IVTCBMI2\_Page1, convID) | PersonOut (IVTCBMO2, convID, convEnded) |
| Final iteration         | EndConv (IVTCBMI2\_Page1, convID)   | PersonOut (IVTCBMO2, convEnded)         |

After these new data types are defined, use custom
mediation code to set the value of the convID and convEnded fields
by retrieving the information from the context.