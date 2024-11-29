<!-- image -->

# Completion tab: Human Task editor

- In the upper fields use the arrows to set the number of Days, Hours, Minutes and Seconds.
- In the lower field you can enter a time in the format 5d12h30m10s,
where d represents days, h hours, m minutes and s seconds.

- Percentage of workers - the task will be considered complete when
a percentage of task owners have completed their subtasks. You can
select the percentage of workers who must be finished before the task
ends.
- One disapproval - a task which requires every owner to approve
can be considered complete if a single owner disapproves. If any owner
responds with False, this is taken to be a
disapproval.
- One approval - a task which requires only that one owner approves
can be considered complete as soon as such a response is received.
If any owner responds with True, this is taken
to be an approval.
- Percentage of approval - If a certain percentage of responders
responses evaluate to true then the task can be stopped.
- Majority reached - if a majority of potential owners returns the
same response then the task can be stopped. This option is useful
when a decision is to be reached by a vote.