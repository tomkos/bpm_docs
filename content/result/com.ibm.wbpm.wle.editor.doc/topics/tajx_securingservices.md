# Modeling secure services

## About this task

- Use the optional checkAuthorization Boolean flag that some JavaScript APIs
provide. If checkAuthorization is set to true, the
authorization check is delegated to the JavaScript API, and only information that the current user
is authorized to access is
returned.instance.retrieveTaskList(properties, maxRows, beginIndex, timezone, true); // authorization is done by JS API
- Use the getAvailableActions() method on a resource to determine whether the
current user is authorized to perform a specific action. Continue only if the specified action is
shown in the result.var actions = instance.getAvailableActions();
		if (actions != null) {
		    for (var i = 0; i < actions.length; i++) {
		        if (actions[i] == "ACTION\_VIEW\_INSTANCE") {
		            // do whatever you want to secure, 
				// e.g. retrieve instance-specific information
		        }
		    }
		}
- Check the user's group membership to determine the user's
authorization.var group = tw.system.org.findParticipantGroupByName(roleName);
		if (tw.system.user.isInParticipantGroup(group)) {
			// do whatever you want to secure, 
			// e.g. retrieve team information
	}