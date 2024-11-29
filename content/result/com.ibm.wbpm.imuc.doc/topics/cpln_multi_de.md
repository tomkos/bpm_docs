<!-- image -->

# Expanding your topology

## Adding cluster members

The easiest way to
expand your infrastructure is to add more cluster members to your
existing clusters. You can add cluster members to each cluster independently
or in combination, depending on where you see the need for growth.
In a single-cluster topology, you can expand the cluster (which provides
the application, support, and messaging capabilities). In
a three-cluster topology with separate application cluster, support
cluster, and messaging cluster, you can add new cluster members for
any one, any two, or all three clusters. By expanding your clusters
in this way, you can improve your application throughput.

- You plan to deploy new applications to your existing environment.
- You anticipate increased volume requirements for your existing
applications.
- You need more capacity for operational purposes, such as failover.

- You have applications or sets of applications that serve different
business purposes and you want to keep them distinct. If you deploy
these distinct applications to the same deployment environment, you
might introduce dependencies between otherwise unrelated business
domains. Dependencies can affect such things as maintenance schedules
and application availability when, for example, unrelated applications
are less reliable.
- After you analyze your performance characteristics, you realize
that planned deployments might push your system beyond the limits
of the current deployment target. They might introduce too many modules
from new applications or new versions of applications to run in the
existing memory space, or use your database tables too heavily.

For information about how to add cluster members using
the Deployment Environment wizard or the BPMConfig command,
see the topics Extending a network deployment environment using the Deployment Environment wizard (deprecated) and BPMConfig command-line utility.

## Adding cells

If you decide that expanding
your existing clusters is not an appropriate solution, you can create
another deployment environment in another cell. This approach provides
the following advantages:

- The most room for growth
- The most flexibility for expanded functional requirements
- Complete isolation for your applications

While this approach is similar to an approach where multiple
deployment environments are used, it removes the deployment manager
as a common point of failure. It also enables you to avoid sharing
Business Automation Workflow installations, which makes it easier to apply fixes and updates
to one environment at a time and provides more isolation for the applications.

To
create a new cell and Business Automation Workflow environment, you follow the same steps
used to set up the first environment. If desired, you can use new
unique names for the cell, deployment manager, and deployment environment.

## Adding deployment environments

If the previous
two options do not satisfy your requirements, there is a third alternative
for expanding your topology. You can create multiple independent deployment
environments for your applications in the same cell.

- You want to reuse complex configurations at the cell level. For
example, you want to set up multiple test environments quickly without
having to configure security or nodes each time.
- You want the convenience of a single IBM® Workflow
Center and
a single administrative console to manage multiple IBM Workflow
Server servers.
- You want to avoid the larger footprint associated with adding
cells.
- You must expand the capacity of your environment but adding cluster
members is not an appropriate solution.
- You want to isolate process applications into separate Java virtual
machines (JVMs), associating each application group with a specific
set of JVMs.

Only one Workflow Center deployment
environment is permitted for each cell, but multiple Workflow Server environments
are permitted. Although it is permitted to share the Workflow Center cell
with Workflow Server deployment
environments, it is not recommended due to upgrade complications.

When
you create additional deployment environments after creating the first
deployment environment, the cell-scoped configuration artifacts already
exist and they will be reused because they are shared. You create
the additional deployment environments in the same way that you created
the first deployment environment.

Generally, you should not
use multiple deployment environments for different environment types,
such as the Testing, Staging, and Production environment types. This
would force you to upgrade all deployment environments at the same
time and would introduce a single point of failure at the deployment
manager.

Running multiple deployment environments
in the same cell is an advanced topology that requires research and
planning. You can create additional Workflow Server deployment environments
with the Deployment Environment wizard or the BPMConfig command,
but you must ensure that all relevant considerations in this topic
have been taken into account.

- Considerations for multiple deployment environments in the same cell

Before you implement this advanced topology, there are several important things to consider.

## Related information

- Extending the network deployment environment using BPMConfig