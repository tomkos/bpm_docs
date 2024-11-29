# Identifying your solution artifacts

In the credit card dispute solution, the document classes that you might need are a dispute form,
a transaction statement, or a correspondence letter. The people who will work on these document
classes might be the customer, a customer service representative, a dispute advisor, the merchant,
or a chargeback advisor.

- Receiving a form from a customer
- Initiating the case
- Tracking the case status
- Reviewing a document
- Requesting a copy of the sales
- Opening a dispute claim
- Opening a fraud investigation
- Generating correspondence
- Requesting a document

For the activity that initiates the process, you must create roles for the customer and the
customer service representative. This activity likely needs to be the first activity in the case
life cycle. This activity also could be an automatic activity that has no preconditions. As an
automatic activity with no preconditions, the activity will start when the case is started and can
even be chained to subsequent activities.

Create steps to map how the activity is implemented. The steps for that activity might be
answering a customer phone call, gathering customer information, retrieving customer data, or
providing supporting documentation. You can define rule steps to automatically determine process
routing or update a case according to a business rule. For example, you can add a rule step to
determine the customer rating, such as DIAMOND, GOLD, or SILVER, that is based on the total
transaction amount and how long the person has been a customer.

A precondition for the activity to start could be that the case was opened by the customer
service representative in the Case Client when receiving
the customer call.

Figure 1. Flow diagram of the activity: Initiating Case

<!-- image -->

After you identify the document classes, roles, and activities, decide which properties will make
up the solution. The properties for the credit card dispute cases might be card reason code,
customer ID, dispute priority, or exposure amount.

After you identify the properties of your solution, specify your decisions about document
classes, case types, steps, preconditions, and so on in Case Builder.