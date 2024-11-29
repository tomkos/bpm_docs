# Modeling process execution paths in BPDs (deprecated)

## Before you begin

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process
definition (BPD) in the Designer view.
3. From the palette, click to select the Sequence Flow tool.
4. In your process diagram, click the first modeling construct
(normally the start event), and then click the construct that follows
the start event in the process flow. The Sequence Flow tool connects
the two items.
5 Continue creating sequence flows as needed. If more thanone sequence flow leaves the same modeling construct, the first oneyou add is the default sequence flow. Subsequent sequence flows thatoriginate from the same construct are only followed under certainconditions. To specify the conditions under which a non-default pathis followed:
    1. Select the sequence flow in the diagram.
    2. In the Behavior section of the
Properties view, specify the condition under which the process execution
follows this sequence flow. The default sequence flow is
followed whenever the conditions specified for the non-default flows
are not met. Conditions for all outgoing sequence flows other than
the default sequence flow are required or mandatory.
6. When you are finished establishing the process flow, click
the Selection Tool in the palette or press Esc to
switch back to normal selection mode in the process diagram.