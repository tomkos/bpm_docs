<!-- image -->

# Assembling services: Customer enquiry example

This example shows how you can assemble a service to process
a customer enquiry.

<!-- image -->

- CustomerQuery accepts a customer ID as input and invokes other
services to obtain customer's portfolio data and the current stock
price. This service also calculates the stock values and returns them
with the portfolio information.
- CustomerInfo accepts a customer ID as input and returns the stocks
and number of shares owned by the customer.
- StockQuote accepts a stock symbol as input and returns the stock's
price.

The three components require implementations that perform
the processing. For example, the CustomerQuery component can be a
business process that retrieves the customer portfolio information
and stock price.

- CustomerQueryInterface provides the getCustomerPortfolio operation,
which accepts CustomerID as input and returns the stocks (array) and
shares (array) owned by the customer and their values (array).
- CustomerInfoInterface provides the getCustomerInfo operation,
which accepts CustomerID as input and returns the stocks (array) and
shares (array) owned by the customer.
- StockQuoteInterface provides the getStockQuote operation, which
accepts StockSymbols (array) as input and returns the price (array)
of the stocks.

- One to the interface on the target component, CustomerInfo
- Another to the interface on the target component, StockQuote

<!-- image -->

The implementations of components that are used in a module's
assembly reside within the module. Components belonging to other modules
can be used through imports. Components in different modules can be
wired together by publishing the services as exports that have their
interfaces, and then dragging the exports into the required assembly
diagram to create imports.

You can add a stand-alone references node to provide access to
the CustomerQuery service. This structure helps you to create JavaServer
pages that use the stand-alone references to access CustomerQuery.
In the assembly editor, the node for the stand-alone references has
an arrow icon, . The following image shows the addition
of the stand-alone references to access the CustomerQuery service:

<!-- image -->

You can make the CustomerQuery service available to other modules
by creating an export. The following image shows the export, CustomerQueryExport,
which is created from the CustomerQuery component's interface:

## Related concepts

- Workspaces
- Creating modules and libraries

## Related tasks

- Organizing projects using integration solutions
- Creating and wiring components
- Working with implementations
- Adding notes
- Setting assembly editor preferences
- Finding errors in the assembly diagram