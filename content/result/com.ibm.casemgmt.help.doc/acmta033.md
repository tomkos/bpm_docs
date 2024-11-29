# Changing the saved solution locale after solution deployment

## Symptoms

The display names, such as case properties, case types,
tasks, and other solution artifacts are not preserved and are not
displayed correctly in the Case Client.
You can lose your translated display names.

## Causes

The solution was deployed to a target environment under
a locale that does not match the solution locale.

When you design and create a solution, you must decide what the solution locale
is. The solution locale refers to the locale of display names, such as case properties, case types,
activities, and other solution artifacts that you create with Case Builder. When you deploy the solution to a target environment
for the first time, you must deploy the solution under the same locale to ensure that the display
names are preserved.

The locale that
is used the first time that you deploy a solution persists in the
target object store for that solution. Future redeployments always
use the saved solution locale regardless the locale that you use for
redeployment.

## Resolving the problem

To prevent this problem, ensure that you deploy the
solution under the designated solution locale.

1. In the IBM® Administration Console for
Content Platform Engine,
browse to Target Object Store > Solution Deployments, right-click
your solution, and select Properties.
2. On the Properties tab, view the Configuration properties.
Change the value of the deploymentLocale property
to your locale code. For example, for German, change the default value,
deploymentLocale=en\_US, to deploymentLocale=de.
3. Deploy the solution again.