# Setting up a team retrieval service

## About this task

A team retrieval service can use custom defined input
parameters to resolve a set of team members and team managers.

## Procedure

To create a team that is dynamically resolved, complete the following steps in the
designer:

1 Open the designer.
    1. In the library, click the plus sign (+) next to the Teams
category.
    2. In the New Team window, enter a name for the team and click
Finish.
2 In the team editor, under Behavior , choose to specify team membersby using a service. You can select an existing service flow create a new one that isenabled for use as a team retrieval service:

1. Click New, specify the name of the new service flow, and click
Finish to complete the wizard.
For more information, see Creating a service flow.
2. Enter a suitable name for the service, for example, Claims Team Retrieval
Service.
3. Click the Variables tab.
The mandatory input and output variables are already present and are locked. Additional input
parameters can be populated by the team itself. The team can assign static values and environment
variables that are passed as data into the additional input variables.Limitation: Updating shared business objects in a team retrieval service is not supported
when the same shared business object is updated within the same execution unit in the process
beforehand. Shared business objects can either be saved explicitly or automatically by enabling
"Automatically sync shared business objects" in the team retrieval service. In general, consider a
team retrieval service conceptually as a read-only service flow.
Important: If you
want to use this dynamic team as the managers of another team, you can use only additional input
parameters that have default values that are defined for them.
4. Select the Diagram tab and provide the implementation of the service.
Based on the input parameters, the service must return a Team object that contains
a list of team members. It can also include the name of a team of managers, and the name of the team
(this parameter is ignored).
For example: // get a new team object
var resultTeam = new tw.object.Team();
var members= [];
// push members (users and groups) into the array
members.push("Group1");
members.push("User1");
// set members in result team
resultTeam.members=members;

// set the result team
tw.local.team = resultTeam;
5 If you want the results of the service to be cached for each combination of input parametervalues, select the Overview tab, then in the Service ResultCache section, select Enable caching of service results todisplay the cache configuration fields. By default, caching is disabled.
    - When caching is disabled, the results caching section is not displayed.
    - When caching is enabled, the results caching section is displayed. By default, the cached
results for each combination of input parameter values are stored for 12 hours. To change the
caching period, use the Days, Hours,
Minutes, and Seconds fields to select the duration
that you want. Important: Depending on the size of the results,
you might need to tune the size of the service results cache to avoid memory problems. By default,
the cache stores up to 4096 results. You can change the size of the cache by setting a different
value for <service-result-cache-size> in the
100Custom.xml file, inside the <server
merge="mergeChildren"> section. 
Limitation: The
results cache setting works only for top-level services or service flows. When a service is called
by another service, the results cache setting for the nested service is ignored and the results for
the nested service or linked service flow are not cached.
3 To use an existing team retrieval service, complete thefollowing steps. If the team retrieval service that you selected requires extraparameters, then the Team Retrieval Service Input Mapping sectionis displayed.

1. Click Select. A selection dialog
is displayed that lists all existing services that match the team
retrieval service template.
2. Select the team retrieval service that you want to use.
4. Click Save or Finish Editing.

## Results