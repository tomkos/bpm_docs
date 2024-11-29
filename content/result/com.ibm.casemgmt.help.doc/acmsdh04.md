# Case types

Case types define the activities, document classes to support the
activities, activity steps, and roles that must complete the steps to solve a business
problem.

The case type also includes property views and client-side human service views that are displayed
to the caseworker. Related case types make up a solution.

An example of case type is a loan application. A loan application case in the Case Client contains detailed information
such as correspondence, activities, policies, and events that the caseworker or case teams
collaborate on to resolve and close the case. Case workers and case managers work together on
cases.

- Attributes such as the name, description, prefix, and identifier of your case type. The unique
case type identifier can be either assigned by the system or you can specify it
yourself.
- Starting document class: You can specify a starting document class. When a document of this
class is added to the repository, a new case instance is automatically created.
- Custom activity creation: You can enable custom activity creation, which allows users to add
quick tasks to the case. You can enable users to add documents and attachments that are in a
repository other than the case management object stores.
- Default layouts for case pages: For the Add Case and Case
Details pages, you can choose the default layout to be a page type or a client-side human
service view. For the Split Case page, the default layout can only be of the Split Case page type.

- You can assign properties to the case type and decide which properties are displayed in the
client views. When you assign properties to case type, you can either assign existing properties
that were defined at the case solution level, or you can add new properties. You can also order and
reorder the case properties.
- The choice list icon  now appears next to case and activity properties that are linked to a choice list. When
editing case and activity properties, the unique identifier is shown to help identify the solution
of the case type. Both the choice list and unique identifier help distinguish the reused
properties.

- When cases are designed with a predefined complex folder structure, they can take a longer time
to create and initialize. To maintain a reasonable response time during the case creation, limit the
complexity of your predefined case folder structure to ten or fewer subfolders.
- If your solution requires cases with a more complex subfolder structure, the best practice is to
create the subfolders later, after the case is initialized. You can add subfolders programmatically,
as part of an automatic activity process, or on demand by a user, as needed.