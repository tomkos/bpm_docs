<!-- image -->

# Overview

This Stock Quote sample addresses the business need of a financial services company that
provides an interactive web-based stock market service to its customers.

The company wants to differentiate itself from its competition by offering tiered levels of
service. The company's goal is to offer delayed stock quotes to their standard customers and
real-time quotes to their premium customers, that is, customers who pay a subscription.

- Offer the delayed and real-time stock quote services as a single service, which dynamically
determines which external service to invoke based on the customer's subscription level.
- If the real-time service is unavailable, route requests to the delayed service without affecting
the running application.