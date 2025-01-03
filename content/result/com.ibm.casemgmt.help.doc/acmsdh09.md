# Document classes

You define document classes to group similar documents and the information about the documents
that are related to the case. You can create as many document classes and properties as needed.

| Document class and description                                                                                          | Properties related to this document class                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Policy documents, such as the written automobile policy and formal changes to the policy                                | Deductible amount, effective date of the policy, expiration date of policy, policy number, policy type, vehicle identification                              |
| Application forms, such as the initial written application form                                                         | Customer address, customer given name, customer family name, customer phone number, date of application, policy number, policy type, vehicle identification |
| Claim forms, such as a claim for a broken windshield                                                                    | Claim number, customer given name, customer family name, date of loss, policy number, type of loss, vehicle identification                                  |
| Repair estimation documents, such as an estimate for a new windshield from a glass repair company                       | Claim number, customer given name, customer family name, estimate total, repair item, vendor name,                                                          |
| Damage assessment documents, such as the report from insurance claim evaluator or photographs of the damaged windshield | Claim number, customer given name, customer family name, date of loss, vehicle identification, vehicle replacement value                                    |
| Correspondence, such as letters sent to the customer about the claim                                                    | Claim number, customer given name, customer family name, date of loss, vehicle identification                                                               |
| Proof of ownership, such as the automobile registration from a state licensing agency or a bill of sale                 | Claim number, customer given name, customer family name, date of loss, vehicle identification, vehicle license plate number                                 |

When you create a document class, you assign a name and description for the document class. The
name is displayed to case workers in the Case Client. Case Builder automatically creates a unique identifier for the document
class.

You can assign one or more properties that provide information about the document to a document
class, and you can assign the same property to more than one document class. In the automobile claim
example, several document classes use the claim number property to associate a document with a
specific claim number.

If properties are required for multiple document classes, create the properties at the solution
level so that you can quickly add them to each document class. Although a property can be shared by
many document classes within a solution, you can define unique values for the default value,
required, and hidden settings for each document class. The values that you set at the document class
level override any settings at the solution level.

If you want to set the Read-only value for a document class, you must do so at the Step
Properties level of the task by using Step Designer.

For example, for the policy document class in the example, the policy number property is a
required property because each policy must have a unique number. For the application form document
class, the policy number is not known when the application form is submitted, and the policy number
is added later after the application is processed. The policy number is not a required property for
the application form document class.

You can also reuse document classes that were imported into the development environment from the
IBM®
FileNet® P8 domain where you will be deploying this solution into
production. You cannot modify reused document classes and they are not re-created during solution
deployment.

You can create a document class that is based on an existing document class. The new
child document class inherits all the properties that are defined for the parent document class. For
the document classes listed in Table 1, you might first create a parent claim document with the
following properties: Claim number, customer given name, customer family name. You could then create
the document classes for claim forms, repair estimations, correspondence, and proof of ownership
based on the parent document. Note that you cannot customize the inherited properties for a child
document class.