<!-- image -->

# Business rule events

| Event Name                      | Event Nature          | Event Contents   | Type      |
|---------------------------------|-----------------------|------------------|-----------|
| br:WBI.BR.ENTRY                 | ENTRY                 | operationName    | string    |
| br:WBI.BR.EXIT                  | EXIT                  | operationName    | string    |
| br:WBI.BR.FAILURE               | FAILURE               | ErrorReport      | Exception |
| br:WBI.BR.FAILURE               | FAILURE               | operationName    | string    |
| br:WBI.BR.SelectionKeyExtracted | SelectionKeyExtracted | operationName    | string    |
| br:WBI.BR.TargetFound           | TargetFound           | operationName    | string    |
| br:WBI.BR.TargetFound           | TargetFound           | target           | string    |