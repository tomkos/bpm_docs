<!-- image -->

# Tutorial: Relationship manager administration

This tutorial demonstrates the basic functions of the IBM® Business Automation Workflow relationship
manager. Relationships are used to correlate identifiers from different
environments for the same item of data. For example, in one environment,
states are identified by two-letter abbreviations (AZ, TX). In another
environment, different abbreviations are used (Ariz., Tex.). A relationship
would be created to correlate "AZ" in the first environment to "Ariz"
in the second environment.

The sample relationship referenced here correlates customer IDs.
Many business applications maintain databases of customers, and most
of these applications assign their own ID to each customer. In an
enterprise environment, the same customer likely has a different ID
in each business application. In this tutorial, a relationship is
defined to correlate customer IDs. The relationship name is "SampleCustID".
Two roles are defined for this relationship. One role is for the Customer
Information System (CIS), and the other role is for the General Ledger
(GL) application. This relationship was created by the relationship
services sample along with the roles and a small amount of sample
data.

The relationship manager is designed to add, modify, and remove
role instances of a relationship instance as well as add, modify,
and remove relationship instances. IBM Integration
Designer should
be used to create and deploy new relationship definitions. The definitions
are stored as XML files that are deployed as part of a Java EE application
to a particular server.

## Objectives of this tutorial

After completing
this tutorial, you will be able to change the values of relationship
instances.

## Time required to complete this tutorial

This
tutorial requires approximately 10 minutes to complete.

## Prerequisites

This tutorial uses a relationship
that is created by the relationship services technical sample. Before
following the steps of this tutorial, go to the samples gallery and
perform the steps described in the relationship services sample to
create the required relationship and roles.

- Example: Changing the values of a relationship instance

For a relationship instance, the values of key attributes can be changed on the Relationship Instances page of the administrative console. This example shows the use of that page to change a value for a relationship instance.