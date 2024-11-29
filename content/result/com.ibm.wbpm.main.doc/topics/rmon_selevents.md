<!-- image -->

# Selector events

| Event Name                        | Event Nature          | Event Contents   | Type      |
|-----------------------------------|-----------------------|------------------|-----------|
| sel:WBI.SEL.ENTRY                 | ENTRY                 | operationName    | string    |
| sel:WBI.SEL.EXIT                  | EXIT                  | operationName    | string    |
| sel:WBI.SEL.FAILURE               | FAILURE               | ErrorReport      | Exception |
| sel:WBI.SEL.FAILURE               | FAILURE               | operationName    | string    |
| sel:WBI.SEL.SelectionKeyExtracted | SelectionKeyExtracted | operationName    | string    |
| sel:WBI.SEL.TargetFound           | TargetFound           | operationName    | string    |
| sel:WBI.SEL.TargetFound           | TargetFound           | target           | string    |