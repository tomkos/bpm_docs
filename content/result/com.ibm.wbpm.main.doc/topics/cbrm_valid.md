<!-- image -->

# Validation

The validation that occurs when making changes through the API classes is only a proper subset of
the overall validation that occurs during serviceDeploy or when editing the artifacts in WebSphere®
Integration Developer. This is due to the constraints that are already placed on the business rule
group in limiting which aspects are editable at run time. The user of the classes can validate the
business rule group selection table, rule set or decision table whenever it is needed (the rule
group component itself is not editable at run time). When a business rule group is published the
rule group selection table, rule sets and decision tables will be validated before being published
to the repository.

If the artifacts are invalid, a ValidationException will be thrown with a list of the validation
problems. The different validation problems are documented in the Exception Handling section.