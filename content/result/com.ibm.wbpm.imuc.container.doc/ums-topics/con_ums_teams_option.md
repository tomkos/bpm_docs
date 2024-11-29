# User Management Service Teams

The UMS Teams option is a microservice that manages global teams for Business Automation Workflow  apps and components.

## What are UMS Teams?

A team is a collection of users, groups, and other teams that already exist.  Unlike users and
groups, teams are not stored in LDAP. The nesting depth of teams is unlimited, but cycles are not
allowed. The UMS Teams option provides the team management capability, but does not perform
authorization on behalf of the apps and components, which apply their own authorization policies.
Teams can be associated with resources in the various Business Automation Workflow components, such as desktops in
Navigator or apps in App Engine to control authorization to these resources.

This approach has several advantages over using your company-wide user registry, such as LDAP,
groups directly:

- Teams can be short-lived or frequently changing, whereas user registry groups are often
long-living.
- Global teams can be defined and changed without modifying your company user registry.
- A company-wide administrator is not required to manage these business-oriented teams.
- Avoids the performance problems that can be caused when a company-wide user registry has too
many groups.

## Identifying teams across different environments

Because each environment (development, test, production) is connected to a different instance of
the UMS Teams server, when you move resources between environments the teams that are associated
with the resources are not automatically moved with the resources, so you must create corresponding
teams on the target environment, if they do not already exist. However, because creating a team in
multiple environments with the same team name and for the same purpose will have different unique
team IDs (UUID), it might not be easy to identify corresponding teams just by their display name,
which is not guaranteed to be unique, for example, many teams might be named "managers".

To avoid confusion, use team distinguished names (which are guaranteed to be unique in a given
environment) consistently across all your environments to identify teams that serve the same
purpose. This will make it easier to identify the correct team in a target environment and map it to
the resources that you deploy.

## Using multiple email addresses

When the user repository contains multiple email addresses for a user, by default, UMS Teams returns only
the primary email address of the user, for example when using the REST API call GET
/teamserver/rest/users. But you can search for users that match with an alternative email
address.

```
<extendedProperty dataType="String" name="emails" entityType="PersonAccount" multiValued="true" />
```

## Administrating UMS Teams

If you are an administrator of the UMS Teams feature, you can create and manage teams by using
either the Team Management UI or the UMS Teams REST APIs.

- Managing teams

 Containers: 
Administrators can use the Team Management page to view, create, modify, or delete teams. You can build a team out of users, groups, and other teams.
- User Management Service Teams access control

 Containers: 
You can control who is authorized to create User Management Service (UMS) teams, change a team, or read the details of a team either by using J2EE roles when installing the UMS Teams service, or, by specific teams whose members have particular access rights on other teams.
- User Management Service Teams REST API

 Containers: 
Your applications can access and administer User Management Service (UMS) teams by using REST calls.