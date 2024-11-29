# Searches and saved searches in the Work dashboard

## User rights on saved searches

By default, any user can create a saved search directly from the
Dashboards section in the navigation pane or from the Saved Search
Editor in the Work page. For example, you might want to save a
search that includes specific business data for your tasks, or that shows your high priority tasks.
You can search on strings or on filters, or combine both.

Administrators can restrict the rights to create and update saved searches to a user or group of
users. For more information, see Administering Process Portal searches and saved searches.

## Full-text search

After you enter
a string and you click Search
, the search starts running and is case-insensitive. The filter that you defined is not
added to the saved search even if you click Save. To include the filter in
the saved search, add it to the filter criteria by clicking Move to filter
criteria, then Save.

Full-text search is supported differently depending on whether Process Portal runs in federated
environment or not. For more information, see Federation considerations for Process Portal.

## Filtering on columns

By default, the Filter Criteria fields are hidden. To display them, click
the visibility icon , which is shown only if the user has the appropriate permissions. Users who are not
authorized to create saved searches can still use the quick-filter field to run ad-hoc searches. For more information about Process Portal action policies, see
Configuration properties for action policies.

- All: All tasks that you are authorized to see.
- Available: Available tasks that you can claim. You claim a task to be
able to start working on it.
- Claimed: Tasks that you have claimed and can work on.
- Claimed and available: (Default) A combined list of your claimed and
available tasks.
- Completed: Tasks that you have already completed.

To refine your search even further, you can use multiple filters in one saved search definition
and you can use the Search field for a full-text search, as explained in
Full-text search.

## More about filters

Some filters have a specific behavior.

<!-- image -->

On date filters, results are more accurate if you specify an interval by using a
combination of Before and After operators.

## Sharing searches

- Whether you work in a federated or nonfederated environment, when you duplicate a saved search,
the new search is a personal search. The criteria are duplicated but not the search
name and sharing status.
- In federated environments, saved searches can be shared with everyone or with teams that are
defined by processes deployed on federated systems version 8.6.0, 18.0.0.1, or later.

## Results