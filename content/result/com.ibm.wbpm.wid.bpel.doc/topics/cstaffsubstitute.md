<!-- image -->

# Substitution for absentees

A substitution policy defines how to deal with tasks and escalations
that are assigned to absent users and is defined when the task template
is modeled. The same policy is applied for all of the task roles that
are associated with a task template. After the task template is deployed,
you cannot change the policy.

If a user is absent, the substitution policy is applied to the
results of the people resolution to determine who receives the work
items instead of the absent user. It is applied only to task roles
that have people assignment criteria. This means that task originators,
starters, or owners are not subject to substitution. Similarly, substitution
is refreshed if the people assignment criteria get refreshed.

To limit the substitution in time, you can specify a start and
end point. If only a start point is specified, then the user will
be considered to be absent from the specified starting point.

- For every user that is present, the user itself is used.
- For every user that is absent, the first substitute that is present
is used.
- If none of the users and none of their substitutes are present,
then the default people assignment rules apply.

- For every user that is present, the user is used.
- Substitutes are not taken into account.
- If none of the users is present, then the original set of users
is used, that is, the fact that they are absent is disregarded.

As substitution is a processing step after people resolution, it
exhibits the same lifecycle as people resolution itself. For a given
task role (for example, Potential Owners), it is carried out, if a
People Assignment Criterion is associated with that role. Similarly,
it is refreshed if the People Assignment Criteria itself gets refreshed.