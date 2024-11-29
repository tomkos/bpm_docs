# Considerations for selecting a topology

When you select a topology pattern, consider the following factors:

- Available hardware resources
- Application invocation patterns
- Types of business processes that you
plan to implement (interruptible versus non-interruptible)
- Individual scalability requirements
- Administrative effort involved

The Application, Remote Messaging, and Remote Support topology pattern
is the preferred topology for IBM® Business Process
Manager Server, but the choice ultimately depends upon your individual requirements.

For information on the components, features, and functionality
available in each of the IBM Business Automation Workflow
configurations, see  IBM Business Automation Workflow editions.

## Condensed topology pattern selection criteria

Consider
the information listed in the following table, which is a quick guide
to selecting your production topology. This table provides a condensed
list of the advantages and disadvantages of each of the topology patterns.

For information about which BPM products support the supplied topology patterns, see 
Topology patterns and supported product features.

| Consideration                                           | Topology Pattern                       |                                                                                                                                                                        |
|---------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Consideration                                           | Single cluster                         | Application, Remote Messaging, and Remote Support                                                                                                                      |
| Number of clusters to maintain                          | One cluster for all components         | Three clusters: One cluster for applications One cluster for support infrastructure One cluster for messaging                                                          |
| Hardware requirements                                   | Can be implemented on limited hardware | Most hardware intensive                                                                                                                                                |
| Asynchronous interactions                               | Use should be minimal                  | Ideal environment for asynchronous interactions                                                                                                                        |
| Long-running processes, state machines, and human tasks | Use should be minimal                  | Ideal environment for interruptible processes, state machines, and human tasks                                                                                         |
| Administrative burden                                   | Relatively small                       | Requires most administrative effort                                                                                                                                    |
| Scalability                                             | All components scaled at the same rate | Easiest to scale  All functions separated  Messaging cluster scalability still limited (benefit comes when other Business Automation Workflow products are introduced) |

## Related information

- Topology patterns and supported product features