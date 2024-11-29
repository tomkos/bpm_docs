# Scenario: Upgrading a customized case management solution

An IBM business partner, PartnerA, builds a case management solution for the insurance industry.
PartnerA names the solution InsuranceSolution and bases the solution on a standard case solution
that IBM provides. After InsuranceSolution gets great reviews from industry analysts, PartnerA sells
its solution to a number of customers, including a large insurance company, CompanyB.

While using InsuranceSolution, CompanyB realizes that it needs to customize the solution to meet
the specific requirements of its organization. In particular, CompanyB wants to add a property, a
role, and a task, and it wants to add a choice to an existing choice list.

PartnerA advises CompanyB to make the additions to a copy of InsuranceSolution, not to customize
the original solution itself. So CompanyB makes a copy of the solution, gives the copy a different
name (InsuranceSolution\_CompanyB) and prefix, makes the desired additions to the copy, and then
deploys the copy.

When PartnerA releases a new version of its case management solution, CompanyB imports it. The
new version (InsuranceSolution2) overwrites the previous version (InsuranceSolution). As a
safeguard, CompanyB makes a copy of its own customized solution (InsuranceSolution\_CompanyB) and
archives it. CompanyB then compares InsuranceSolution2 with InsuranceSolution\_CompanyB, updates
InsuranceSolution\_CompanyB based on the reported differences, and deploys the newly revised
copy.