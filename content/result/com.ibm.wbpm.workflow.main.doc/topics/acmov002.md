# Scenario: Financial services credit card dispute resolution

## Problem

Banks that issue credit cards are
seeing a significant increase in dispute cases. In addition, regulatory
reform and an increased focus on customer satisfaction put more pressure
on banks to handle each case as efficiently as possible. The banks
require a solution that enables them to process each incoming dispute
and decide whether to forward it to the credit card company for chargeback.

Credit
card companies have strict requirements for how cases can be submitted.
The bank solution must provide accurate and appropriate information
to the credit card company to ensure efficient processing.

## Solution

A business analyst at the bank,
Anna, studies the requirements of the credit card company's dispute
process. She determines the types of  information that the credit
card company requires to process a dispute. Anna uses the IBM Business Automation
Workflow tools
to quickly design and create a solution that helps the bank representatives
capture all of the required information in a case and attach additional
records and documents to the case. Anna determines what roles must
be involved in processing dispute and fraud cases, and she assigns
permissions to different groups based on those roles.

## Scenario

Jane, a credit card customer of
the bank, buys a table from an online merchant for $400. The table
is not delivered within three weeks as the merchant promised. Jane
sends email and calls the merchant. However, no one responds. Because
she used her credit card for the transaction, Jane calls the bank
for help.

Jane enters her account information by using the automated
phone system. As a result, her call is routed to Nicole, a senior
customer service representative. When Jane explains the situation,
Nicole opens a case to track the dispute. She finds the purchase transaction
for the table from Jane's account and adds the record to the new case.
Nicole forwards the call and the case to a dispute agent, Frank.

During
his conversation with Jane, Frank enters data into the case by using
a form that captures details about the transaction, the merchant,
and the customer. When Jane says that she can provide a copy of the
receipt and delivery agreement, Frank creates an activity in the case
to follow up on requesting the document. Frank tells Jane that he
will investigate further, and adds Jane's preferred contact method
to the case. When the call ends, a recording of the call is automatically
added to the case as a document.

Frank uses Case Client as an interface.
This interface is customized to Frank's job as a case worker. The
interface provides a comprehensive view of the case, the tools to
review details of the case, and the ability to take actions based
on his findings. After some research, Frank discovers that the merchant
has gone out of business. He adds a comment to the case about this
discovery. Frank is notified that the online receipt and delivery
agreement have arrived from Jane. These documents automatically get
added to the case and are available for Frank to review.

Frank
decides to process a chargeback against the merchant. He starts an
activity that gathers the relevant details of the case, formulates
the chargeback request, validates that the information is correct
and complete, and forwards it to the credit card company. Frank also
creates an activity in the case for his supervisor Richard to review
the case and determine whether any action must be taken based on the
fact that the merchant is no longer in business.

Frank's supervisor
Richard reviews the case. He notices Frank's comment that the merchant
has gone out of business. He uses the IBM Business Automation
Workflow case
analytics tool to search for cases against the merchant to determine
whether other customers are affected. He also analyzes recent transactions
involving the merchant to determine the bank's level of exposure.

Based
on this analysis, Richard decides to set up a subteam to handle any
disputes involving this merchant. He sends a change request to Anna,
the business analyst, to modify the solution to incorporate this new
team. From his Case Client environment,
Richard requests that a letter be sent to affected customers to inform
them of their dispute rights. Richard also sends an alert to his team
of advisors to inform them of the situation. He then completes his
review of the case.

Anna receives Richard's change request.
To satisfy the new requirement, Anna designs a new role for the subteam
in the solution and adds a new rule. When customers call with disputes
that involve this merchant, the new rule routes the disputes to the
new team. By using the IBM Business Automation
Workflow tools,
Anna can implement the changes in a few minutes. She can then easily
test the solution changes before deploying them to the production
system.

Because the credit card company implemented an efficient
case management process, Jane's and other customer's requests can
be more quickly resolved.