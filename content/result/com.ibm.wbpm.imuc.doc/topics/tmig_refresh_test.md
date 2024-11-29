# Testing the IBM Business Automation Workflow upgrade

## About this task

Although the first option in the following procedure is usually enough, other testing methods can
identify additional problems before they affect your production systems. If you have not upgraded
for a while or had trouble with production upgrades, you might want to consider the other options
when you are planning to upgrade.

## Procedure

- Upgrade the test Workflow Server environmentsfirst and test your existing applications. When you are upgrading a set of environments that consist of a Workflow Center , a production Workflow Server , and one or more test Workflow Server environments, roll out the upgradesincrementally. See Performing a rolling upgrade . By upgrading the test Workflow Server environments first, you can validate theupgrade procedure and test that your existing applications still work well at the new level.Limitations:
    - This testing method does not detect problems that are related to environment-specific data. For
example, corrupted IBM Installation
Manager or database
data that is only in your production system will not be noticed until you upgrade your production
system.
    - If you are upgrading from a previous release, you cannot test with updated system toolkits until
you upgrade all your environments.
    - If there are problems specific to Workflow Center, you will find them only after you upgrade all your environments.
- Set up a temporary Workflow Center for
testing.

 If you can set up a temporary Workflow Center,
you can test for problems with Workflow Center
before you upgrade your production environment. If you are upgrading from a previous release, you
can import your snapshots and test them with the updated system toolkits. After you complete your
testing, discard the test Workflow Center and note
the changes that you must make in your normal Workflow Center system after you finish the upgrade.
- Test the upgrade by using production database data.

Some database-specific problems can be found only when the production data is used. You can use
this test method to identify and correct problems that might exist in your production database
without multiple outages.
- Test the upgrade by using installation data from an
existing installation.

This testing method checks for corruption in Installation Manager or Business Automation Workflow installation data that might prevent a
successful upgrade. You can use this method to identify and correct problems in your production
installation data without requiring multiple outages.