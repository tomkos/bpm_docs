<!-- image -->

# Example Scenario

Dynamic endpoint selection is a rules-based router pattern that
can be used to find a required service provider endpoint from a pre-configured
list of endpoints. It exposes a well-defined and self-contained set
of SOA services known as business services. These business services
represent high level, horizontal business functions such as Activate
Service, Perform Customer Order Feasibility and Check Credit Status.

Let us consider a scenario of creating a customer billing account for a subscribed Telecom
service such as a Triple-Play product bundle that includes VoIP, IPTV, High-Speed DSL whose accounts
are maintained in different back-end systems. This is a common pattern among communication service
providers that offer multiple telecommunications products and services and bundle them as well for
their customers.

A simple rule for selecting an endpoint resembles one of the following:

- When CustomerOrder.productType equals 'VoIP' Then
Invoke Create Billing Account for VoIP Provider
- When CustomerOrder.productType equals 'High-Speed DSL'
Then Invoke Create Billing Account for High-Speed DSL Provider
- When CustomerOrder.productType equals 'IPTV' Then
Invoke Create Billing Account for IPTV Provider

- Business rules employing decision tables can be constructed easily using a rules implementation
functionality or a tool such as IBM WebSphere Business Process Rules Manager or IBM® Operational Decision
Manager business rules management system
(BRMS). However for constructing rules, it is a prerequisite to have a rules vocabulary model
defined.
- Rules vocabulary can be constructed manually or by importing
schemas from a pre-defined data model provided as part of IBM BPM
Telecom Pack.
- The data model packaged as part of IBM BPM Telecom Pack follows
a common industry standard known as Shared Information Data Model
(SID) defined by the Tele Management Forum (TMF).