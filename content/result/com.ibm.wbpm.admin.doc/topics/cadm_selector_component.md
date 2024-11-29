<!-- image -->

# Overview of selector components

Selector components provide a single interface to a service that may change results based on
certain criteria. The selector component includes an interface and a selector table. Based on the
criteria, the selector table determines which component (named the target component) processes the
request. The server returns the processing result provided by a target component to the client.

When building a business process, the solution architect identifies the need for a selector
component and defines the interface and selector table that the selector component uses to complete
processing. The tasks involved in developing a selector component are described in the IBM® Integration
Designer documentation.

Administering a selector component consists of tasks related to the selector component or tasks
related to the selector table.

- Displaying selector components

Displaying selector components is the first step in administering selector components. From the display you can export any or all of the selector components or display the selector tables which make up the selector components.
- Displaying selector tables

Displaying selector tables is the first step in administering the tables. The resulting display is a list of target components from which you can alter the processing criteria, change the target component that runs for a specific criterion, add a new target component or delete a target component from the table, thereby removing a criterion.
- Changing target components

Changing target components allows you to alter selector component processing by either changing the selection criteria for a specific target component, changing the target component for a selection criteria, or changing both the selection criteria and the target component.
- Adding target components

Add a target component when you need additional processing for a different selection criterion than currently exists in the selector table.
- Deleting target components

Deleting target components alters selector component processing by removing the entry in the selector table for a specific selection criterion.
- Exporting selector components using the administrative console

Export selector components when you have made changes to the selector tables. This will create a file that you can import into your development environment, thereby keeping the development artifacts synchronized with the actual production system artifacts.
- Importing selector components using the administrative console

Import selectors in order to update installed selector components without reinstalling an application.

## Related concepts

- Considerations for modules containing business rules and selectors
- Overview of business rules
- Business process rules manager

## Related information

- Business Rules