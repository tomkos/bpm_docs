# Using team services to define dynamic teams

## The structure of teams

Each team has a name,
a list of members (users or groups) and, optionally, the name of a
team of managers. Only the managers can perform managerial actions,
but managers can also be members of the team that can perform an activity.
Teams can be associated directly with activities, or assigned as default
teams to lanes. Because any team can be assigned as the managers of
another team, it is possible to define teams to reflect the managerial
structure of your organization.

When a team is resolved dynamically by a team retrieval service or filtered by
a team filter service, the service flow must return a Team object. The
returned Team object consists of a list of team members in the
members field and the optional fields; name for
the name of the team (which is ignored), and managerTeam
for the name of the team of managers.

## Team retrieval service

Instead of defining static teams, with fixed members and fixed managers, you can create teams
whose members and managers are dynamically resolved by a team retrieval service. The team retrieval
service receives the name of the team as a string parameter, and returns the resolved team as a
Team object. If necessary you can add extra input parameters that
are required to resolve the team.

When you assign an activity to a team that is defined by a team retrieval service that uses extra
parameters, you must define which environment variables or literal values are mapped onto each extra
input parameter. If you want the team to be used as the managers of another team, you can only use
additional input parameters that have default values that are defined for them.

## Team filter service

There are times when you do not want the whole team to be assigned to a task, but rather a subset
of the team. You can create team filter services to implement assignment policies. The team filter
service takes the initially resolved team as a parameter and must return the filtered team as a
Team object. If necessary you can add extra input parameters that are required to
filter the team.

For example, to implement a separation of duties policy, you might need to remove the user who
performed the previous activity from the list of users who can perform the next activity. In that
case, the filter service needs an input parameter for the user ID that is to be removed from the
input team.

If, for example, insurance claims above a certain threshold can be handled only by particular
team members, you might create a filter named High claim value team
filter that uses an input parameter claimValue to filter
out any users that are not qualified to work high value claims.

## Caching team service results

If appropriate, you can enable results caching for any team service. When enabled, the results of
top-level service flows are cached for unique combinations of input parameter values to improve
performance. By default, results are refreshed after 12 hours, but this value can be changed. By
default, the cache stores up to 4096 results. If the service flow is called and the number of cached
results exceeds the defined cache size, the least recently used result is removed so that there is
space for the new result.