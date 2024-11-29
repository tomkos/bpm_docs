# Comparing solutions

## About this task

To address the unique requirements of their organizations, customers might choose to
customize the case management solutions that they use. When these customers upgrade their case
management solutions, they do not want to lose any changes that they previously made to the
solutions. Using the results of the solution comparison report, customers can update their
customized case management solutions after they upgrade.

## Procedure

To compare solutions:

1. Log in to Case Builder.
2. Find one of the solutions that you want to compare and click More Actions > Compare.

Important: The solutions that you want to compare must be committed.
Tip: If you plan to compare two versions of the same solution, select the older version
first.
3 Select the other solution that you want to compare and click OK . Ignore solution prefixes Solution prefixes are unique; no two solutions have the same prefix. Ignore GUIDs of the objects Object GUIDs are unique; no two objects have the same GUID.
    - Leave this option selected to hide the prefixes of the solutions being compared.
    - Clear this option to see the prefixes of the solutions being compared.
    - Leave this option selected to hide the GUIDs of the objects being compared.
    - Clear this option to see the GUIDs of the objects being compared.
4 View the results of the comparison in the messages area of the ManageSolutions page. High-level information High-level information is provided for the following items: Detailed information More detailed information (such as actual values) is provided for the following items: In the results, the solution for which you selected theCompare action is referred to as Solution 1, and the solution that you arecomparing it to is referred to as Solution 2. The results include information about what items aredifferent between solutions: Modified The item exists in both solutions, but its value is different in each solution. Missing The item is missing in Solution 1 (that is, the item exists only in Solution 2). Found The item exists only in Solution 1 (that is, the item is missing in Solution 2). Tip: The messages area is dynamic and always displays the most recent message. To giveyourself time to thoroughly review the results of the comparison, copy the results to a text file.If the comparison results in the message area are overwritten before you can review them on-screen,run the comparison again. Restriction: The solution comparison detects changes that were made to objects that arevisible in Case Builder only. It doesn't detect changes made byIBM®FileNet® Process Designer to Content Platform Engine objects such as event logs, queues, and rosters.

- Pages
- Rules
- Activity workflows
- Views

- Case properties
- Case types
- Choice lists
- Content Platform Engine configuration values
- Document classes
- In-baskets
- Roles
- Activity properties
- Activities

- Scenario: Upgrading a customized case management solution

If your organization uses a customized case management solution, you need to have an upgrade plan, which ensures that your customizations aren't overwritten from one release of the case management solution to the next. This scenario shows you one way to upgrade a case management solution, compare the new and the customized solutions to identify differences, and then use the resulting report to update your customized solution.