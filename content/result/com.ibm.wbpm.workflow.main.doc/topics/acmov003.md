# Scenario: Automobile insurance claims

## Problem

Automobile insurance claims can
involve input and supporting documentation from many sources, including
the claim submitter, the repair shop, the police, and other official
sources of information about vehicle value or road conditions. In
addition, different analysts are often required to evaluate and add
information to an insurance claim during processing. All documentation
and claim information must be available and easily accessible to enable
adjustors to properly evaluate and resolve the claim.

Individual
claims can vary greatly. This variability can require case workers
to start discretionary processes, to involve new roles, and to change
how and when activities are completed as the claim is routed through
the organization.

## Solution

Javier, a business analyst at the
automobile insurance company, is working on making the automobile
claims process more consistent. Javier uses Case Builder to design
a solution with activities that involve multiple steps. He creates
roles for each step in the claims process, and assigns permission
to the roles for the groups of employees who perform the activities
at each stage in the process.

- Claim properties, such as policy number and accident details
- Roles, such as claims adjustor or fraud investigator
- Case types, such as general claims, claims with injury, or major
loss claims.

In addition, Case Builder enables
Javier to create a flexible solution. He can quickly change roles,
processing, or add activities when they are needed. He can also use
business rules to automatically update claim properties, such as to
calculate a new premium after a claim is filed.

## Scenario

Carly is driving on a roadway when
her car strikes a large object. Although she is not hurt, her car
is too damaged to drive. The police arrive, and a tow truck is dispatched.
When Carly calls her insurance company, customer service representative
Chris opens a case for her claim. He uses a First Notice of Loss (FNOL)
form to record the information. When he enters her home phone number,
many of the form fields are automatically populated with her data
that is retrieved from the system.

Chris asks about her location,
and tells her to have the tow truck driver take her damaged car to
a specific nearby repair shop. The case information is forwarded to
the car repair shop. Chris tells Carly how to use a PDF form  that
is available on the insurance company's website to provide details
about the accident. He gives her the case  number that was generated
when he opened her case. She will include the case number on the form.

Chris
recalls a memorandum about recent fraudulent claims involving collisions
with roadway debris. He creates a discretionary activity to involve
a fraud investigator in the claim.

Later, Carly downloads the
PDF form from the insurance company's website and enters the accident
details and the case number. She mails the form back to the insurance
company. Javier is using IBM Datacap to automatically
scan and index the form into the case. Because this action is set
as a precondition on Chris's activity to review the claim, he is notified
when the form is added to the case. Also, on the company website,
Carly uses her case number to access a tool for uploading photographs
of her damaged car.

John, the agent at the car repair shop,
receives notification about the case. He creates an activity to provide
an estimate for repairs. John makes sure that the $4500 estimate for
repair does not exceed the value of the car and submits the estimate
to the insurance company. He uses Carly's contact information to let
her know that the estimate was submitted.

The case is routed
to Lisa, an adjustor. She reviews the case and the supporting documents,
including the police report and the photographs of the damage. The
estimate is below the threshold for investigation, and the fraud investigator
has set the flag for possible fraud to false. Lisa approves the claim.

After
the claim is approved, an activity is triggered to automatically calculate
the new premium for Carly. The new premium is calculated according
to a business rule that evaluates whether the accident was caused
by negligence, the number and severity of any other claims that Carly
filed during the last few years, and the type of policy.

After
the case is closed, the insurance company receives a report from the
police that a freight company was charged with dropping the object
that caused Carly's accident. Lisa reopens Carly's case. She contacts
Javier, who adds a new role to the system called recovery expert.
The recovery expert creates new activities to attempt to reclaim the
cost of the repairs from the freight company.

Because of the
flexibility of this case management system, case workers can resolve
problems more quickly and efficiently, and customers can close their
claims more easily.