<!-- image -->

# How the business process rules manager works

Use the business process rules manager to perform the following tasks:

- Retrieve a copy of a business rule from the repository
- Browse and edit a business rule
- Publish a business rule to the repository

The following figure shows how the business rules manager calls and publishes rules.

Figure 1.  Business process rules manager sequence of events

<!-- image -->

After you log in to the business process rules manager, the following events occur when you
modify a business rule.

1. When you select a business rule, the business process rules manager accesses the business rule
group from the repository and stores it in the server memory as an original copy.
2. The business rule group and rule logic are available for editing.
3. You can save changes to a rule set, decision table, and business rule group as a copy in the
server memory.
4. You publish the local copy back to the data source. Alternatively, you can cancel the changes
with no updates being performed.