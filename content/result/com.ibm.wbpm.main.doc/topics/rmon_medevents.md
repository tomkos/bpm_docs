<!-- image -->

# Mediation events

| Event Name                                   | Event Nature               | Event Contents             | Type                       |
|----------------------------------------------|----------------------------|----------------------------|----------------------------|
| OperationBinding element                     | OperationBinding element   | OperationBinding element   | OperationBinding element   |
| ifm:WBI.MEDIATION.OperationBinding.ENTRY     | ENTRY                      | InteractionType            | string                     |
| ifm:WBI.MEDIATION.OperationBinding.ENTRY     | ENTRY                      | TicketID                   | string                     |
| ifm:WBI.MEDIATION.OperationBinding.ENTRY     | ENTRY                      | Source                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.ENTRY     | ENTRY                      | Target                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.EXIT      | EXIT                       | InteractionType            | string                     |
| ifm:WBI.MEDIATION.OperationBinding.EXIT      | EXIT                       | TicketID                   | string                     |
| ifm:WBI.MEDIATION.OperationBinding.EXIT      | EXIT                       | Source                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.EXIT      | EXIT                       | Target                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.FAILURE   | FAILURE                    | InteractionType            | string                     |
| ifm:WBI.MEDIATION.OperationBinding.FAILURE   | FAILURE                    | TicketID                   | string                     |
| ifm:WBI.MEDIATION.OperationBinding.FAILURE   | FAILURE                    | Source                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.FAILURE   | FAILURE                    | Target                     | string                     |
| ifm:WBI.MEDIATION.OperationBinding.FAILURE   | FAILURE                    | ErrorReport                | Exception                  |
| ParameterMediation element                   | ParameterMediation element | ParameterMediation element | ParameterMediation element |
| ifm:WBI.MEDIATION.ParameterMediation.ENTRY   | ENTRY                      | Type                       | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.ENTRY   | ENTRY                      | TransformName              | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.EXIT    | EXIT                       | Type                       | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.EXIT    | EXIT                       | TransformName              | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.FAILURE | FAILURE                    | Type                       | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.FAILURE | FAILURE                    | TransformName              | string                     |
| ifm:WBI.MEDIATION.ParameterMediation.FAILURE | FAILURE                    | ErrorReport                | Exception                  |