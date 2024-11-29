<!-- image -->

# exportBusinessRuleArtifacts.jacl script

This function is useful when you are exporting the business rules and selector components for
				multiple applications at one time.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
-f exportBusinessRuleArtifacts.jacl
target\_ns
component
user
[-zipf filename]
```

## Required parameters

## Optional parameter

## Example

The following script exports the
business rules and selector components from the component named OnlineOrder
in the test.oo.brules namespace.

```
wsadmin -f exportBusinessRuleArtifacts.jacl
	http://test.oo.brules OnlineOrder admin
	-zipf c:/artifacts/onlineorder.zip
```