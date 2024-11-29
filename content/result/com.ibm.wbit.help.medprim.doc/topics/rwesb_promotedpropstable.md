# Promoted properties table

## Table of promotable properties

The follow
tables shows the properties you can promote. Any
promoted property is also a dynamic property, if the property is in
the top-level request, response, or fault flow.

| Mediation primitive     | Promotable properties                             | Promotable properties                             |
|-------------------------|---------------------------------------------------|---------------------------------------------------|
| Custom Mediation        | Value (in User Properties)                        | Value (in User Properties)                        |
| Database Lookup         | Key column name                                   | Key column name                                   |
| Database Lookup         | Key path                                          | Key path                                          |
| Database Lookup         | Message element (in Data Elements)                | Message element (in Data Elements)                |
| Database Lookup         | Table name                                        | Table name                                        |
| Database Lookup         | Validate input                                    | Validate input                                    |
| Endpoint Lookup         | Binding type                                      | Binding type                                      |
| Endpoint Lookup         | Classification                                    | Classification                                    |
| Endpoint Lookup         | Export                                            | Export                                            |
| Endpoint Lookup         | Match policy                                      | Match policy                                      |
| Endpoint Lookup         | Module                                            | Module                                            |
| Endpoint Lookup         | Name                                              | Name                                              |
| Endpoint Lookup         | Namespace                                         | Namespace                                         |
| Endpoint Lookup         | Registry name                                     | Registry name                                     |
| Endpoint Lookup         | Value (in User Properties)                        | Value (in User Properties)                        |
| Endpoint Lookup         | Version                                           | Version                                           |
| Event Emitter           | Enabled                                           | Enabled                                           |
| Event Emitter           | Transaction mode                                  | Transaction mode                                  |
| Fail                    | Error message                                     | Error message                                     |
| Fail                    | Root                                              | Root                                              |
| Fan In                  | Count (decision type)                             | Count (decision type)                             |
| Fan In                  | Timeout                                           | Timeout                                           |
| Fan In                  | XPath (decision type)                             | XPath (decision type)                             |
| Fan Out                 | Batch Count                                       | Batch Count                                       |
| Gateway Endpoint Lookup | Classification                                    | Classification                                    |
| Gateway Endpoint Lookup | Lookup XPath                                      | Lookup XPath                                      |
| Gateway Endpoint Lookup | Registry name                                     | Registry name                                     |
| Gateway Endpoint Lookup | Value (in User Properties)                        | Value (in User Properties)                        |
| HTTP Header Setter      | Validate input                                    | Validate input                                    |
| JMS Header Setter       | Validate input                                    | Validate input                                    |
| Mapping                 | Mapping file                                      | Mapping file                                      |
| Mapping                 | Root                                              | Root                                              |
| Mapping                 | Validate input                                    | Validate input                                    |
| Message Element Setter  | Validate input                                    | Validate input                                    |
| Message Element Setter  | Value (in Message Elements)                       | Value (in Message Elements)                       |
| Message Filter          | Distribution mode                                 | Distribution mode                                 |
| Message Filter          | Enabled                                           | Enabled                                           |
| Message Filter          | Pattern (in Filters)                              | Pattern (in Filters)                              |
| Message Logger          | Enabled                                           | Enabled                                           |
| Message Logger          | Level                                             | Level                                             |
| Message Logger          | Logging type                                      | Logging type                                      |
| Message Logger          | Root                                              | Root                                              |
| Message Logger          | Transaction mode                                  | Transaction mode                                  |
| Message Validator       | Enabled                                           | Enabled                                           |
| Message Validator       | Root                                              | Root                                              |
| MQ Header Setter        | Validate input                                    | Validate input                                    |
| Policy Resolution       | Policy scope                                      | Policy scope                                      |
| Policy Resolution       | Propagate mediation policy to response flow       | Propagate mediation policy to response flow       |
| Service Invoke          | Async timeout                                     | Async timeout                                     |
| Service Invoke          | Retry count                                       | Retry count                                       |
| Service Invoke          | Retry delay                                       | Retry delay                                       |
| Service Invoke          | Retry on                                          | Retry on                                          |
| Service Invoke          | Try alternate endpoints                           | Try alternate endpoints                           |
| Service Invoke          | Use dynamic endpoint if set in the message header | Use dynamic endpoint if set in the message header |
| Set Message Type        | Validate                                          | Validate                                          |
| SLA Check               | Consumer ID                                       | Consumer ID                                       |
| SLA Check               | Context ID                                        | Context ID                                        |
| SLA Check               | Endpoint                                          | Endpoint                                          |
| SLA Check               | Registry Name                                     | Registry Name                                     |
| SLA Endpoint Lookup     | Consumer ID                                       | Consumer ID                                       |
| SLA Endpoint Lookup     | Context ID                                        | Context ID                                        |
| SLA Endpoint Lookup     | Endpoint Classification                           | Endpoint Classification                           |
| SLA Endpoint Lookup     | Registry Name                                     | Registry Name                                     |
| SLA Endpoint Lookup     | Value (in Additional Parameters)                  | Value (in Additional Parameters)                  |
| SOAP Header Setter      | Validate input                                    | Validate input                                    |
| Trace                   | Destination                                       | Destination                                       |
| Trace                   | Enabled                                           | Enabled                                           |
| Trace                   | File                                              | File                                              |
| Trace                   | Literal                                           | Literal                                           |
| Trace                   | Root                                              | Root                                              |
| Type Filter             | XPath Element                                     | XPath Element                                     |
| UDDI Endpoint Lookup    | Business Name                                     | Business Name                                     |
| UDDI Endpoint Lookup    | Match Policy                                      | Match Policy                                      |
| UDDI Endpoint Lookup    | Registry Name                                     | Registry Name                                     |
| UDDI Endpoint Lookup    | Service Name                                      | Service Name                                      |

| Component    | Promotable properties                             |
|--------------|---------------------------------------------------|
| Callout node | Async timeout                                     |
| Callout node | Invocation style                                  |
| Callout node | Retry count                                       |
| Callout node | Retry delay                                       |
| Callout node | Retry on                                          |
| Callout node | Try alternate endpoints                           |
| Callout node | Use dynamic endpoint if set in the message header |

## Runtime considerations

The value of certain
promotable properties is displayed by IBM® Integration
Designer as
a text value, but by the runtime administrative console as an integer.
If you update these properties from the administrative console, you
must specify the integer values.

| Mediation Primitive   | Property                                    | Text Value                                                          | Integer Value                |
|-----------------------|---------------------------------------------|---------------------------------------------------------------------|------------------------------|
| Endpoint Lookup       | Match policy                                | Return all matching endpoints                                       | 0                            |
| Endpoint Lookup       | Match policy                                | Return first matching endpoint and set routing target               | 1                            |
| Endpoint Lookup       | Match policy                                | Return all matching endpoints and set alternate routing targets     | 2                            |
| Endpoint Lookup       | Match policy                                | Return endpoint matching latest compatible service version          | 3                            |
| Event Emitter         | Enabled                                     | True                                                                | true (Boolean)               |
| Event Emitter         | Enabled                                     | False                                                               | false (Boolean)              |
| Event Emitter         | Transaction mode                            | Default                                                             | 0                            |
| Event Emitter         | Transaction mode                            | Existing                                                            | 1                            |
| Event Emitter         | Transaction mode                            | New                                                                 | 2                            |
| Fan Out               | Batch Count                                 | check for asynchronous responses after all messages have been fired | 0                            |
| Fan Out               | Batch Count                                 | check for asynchronous responses after {n} messages have been fired | Integer value greater than 0 |
| HTTP Header Setter    | Validate input                              | True                                                                | true (Boolean)               |
| HTTP Header Setter    | Validate input                              | False                                                               | false (Boolean)              |
| JMS Header Setter     | Validate input                              | True                                                                | true (Boolean)               |
| JMS Header Setter     | Validate input                              | False                                                               | false (Boolean)              |
| Message Filter        | Distribution mode                           | First                                                               | 0                            |
| Message Filter        | Distribution mode                           | All                                                                 | 1                            |
| Message Filter        | Enabled                                     | True                                                                | true (Boolean)               |
| Message Filter        | Enabled                                     | False                                                               | false (Boolean)              |
| Message Logger        | Enabled                                     | True                                                                | true (Boolean)               |
| Message Logger        | Enabled                                     | False                                                               | false (Boolean)              |
| Message Logger        | Level                                       | Severe                                                              | 0                            |
| Message Logger        | Level                                       | Warning                                                             | 1                            |
| Message Logger        | Level                                       | Info                                                                | 2                            |
| Message Logger        | Level                                       | Config                                                              | 3                            |
| Message Logger        | Level                                       | Fine                                                                | 4                            |
| Message Logger        | Level                                       | Finer                                                               | 5                            |
| Message Logger        | Level                                       | Finest                                                              | 6                            |
| Message Logger        | Logging type                                | Database                                                            | 0                            |
| Message Logger        | Logging type                                | Custom                                                              | 1                            |
| Message Logger        | Transaction mode                            | Same                                                                | 0                            |
| Message Logger        | Transaction mode                            | New                                                                 | 1                            |
| Message Validator     | Enabled                                     | True                                                                | true (Boolean)               |
| Message Validator     | Enabled                                     | False                                                               | false (Boolean)              |
| MQ Header Setter      | Validate input                              | True                                                                | true (Boolean)               |
| MQ Header Setter      | Validate input                              | False                                                               | false (Boolean)              |
| Policy Resolution     | Policy scope                                | Module                                                              | 0                            |
| Policy Resolution     | Policy scope                                | Target Service                                                      | 1                            |
| Policy Resolution     | Policy scope                                | Intersection                                                        | 2                            |
| Policy Resolution     | Propagate mediation policy to response flow | False                                                               | false (Boolean)              |
| Service Invoke        | Retry on                                    | Never                                                               | 0                            |
| Service Invoke        | Retry on                                    | Any fault                                                           | 1                            |
| Service Invoke        | Retry on                                    | Modeled fault                                                       | 2                            |
| Service Invoke        | Retry on                                    | Unmodeled fault                                                     | 3                            |
| SOAP Header Setter    | Validate input                              | True                                                                | true (Boolean)               |
| SOAP Header Setter    | Validate input                              | False                                                               | false (Boolean)              |
| Trace                 | Enabled                                     | True                                                                | true (Boolean)               |
| Trace                 | Enabled                                     | False                                                               | false (Boolean)              |
| UDDI Endpoint Lookup  | Match policy                                | Return all matching endpoints                                       | 0                            |
| UDDI Endpoint Lookup  | Match policy                                | Return first matching endpoint and set routing target               | 1                            |
| UDDI Endpoint Lookup  | Match policy                                | Return all matching endpoints and set alternate routing targets     | 2                            |

| Component    | Property   | Text Value      |   Integer Value |
|--------------|------------|-----------------|-----------------|
| Callout node | Retry on   | Never           |               0 |
| Callout node | Retry on   | Any fault       |               1 |
| Callout node | Retry on   | Modeled fault   |               2 |
| Callout node | Retry on   | Unmodeled fault |               3 |