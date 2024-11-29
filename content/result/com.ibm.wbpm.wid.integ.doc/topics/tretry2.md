<!-- image -->

# Retrying the same service

## About this task

Note that for a
Service Invoke primitive, nothing should be wired to its fault terminals.

| Property Name                                 | Should be set to                                                                                                                              |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Retry On                                      | Any one of  Any fault Modeled fault Unmodeled fault                                                                                           |
| Retry Count                                   | Any integer greater than 0. If set to 0, no retry attempts will be made.                                                                      |
| Use dynamic endpoint & Try alternate endpoint | Both set to FALSE (unchecked). If TRUE (checked) and there are alternate endpoints defined in the SMO Header, other services will be invoked. |