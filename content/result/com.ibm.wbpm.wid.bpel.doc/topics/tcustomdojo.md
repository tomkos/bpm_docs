<!-- image -->

# Integrating JavaScript in HTML-Dojo
pages

## About this task

This topic provides a high-level view
on how to integrate JavaScript to
an HTML-Dojo page. To view a white paper that describes how to customize
an HTML-Dojo page, go to Customizing HTML-Dojo Forms for Human Tasks .

To
integrate JavaScript functions
to an HTML-Dojo page, complete the following steps:

## Procedure

1. Create a JavaScript with
the same name as the Dojo module, in the directory that matches the
package name. In the following example, the Dojo module is saved as form.js in
the company directory. dojo.provide("company.form");
	// The Task Information widget does not set the char-set attribute.
	// Therefore the script is processed in the encoding of the Heritage Process Portal space which is utf-8
	//
	// Calculate the number of the next year.
	//
		company.form.setDojoComponentToNextYear = function(id) {
			var comp = dijit.byId(id);
			var year = (new Date()).getFullYear() + 1;
			if (comp != null) {
			comp.attr("value",year);
	}
}
2. Add a script element that defines the
location of the package and the name of the module. The script element
is parsed. Only the dojo.registerModulePath and dojo.require statements
are recognized, and the task information widget converts the path
in the dojo.registerModulePath (package,path) statement to make it
relative to the location of the task form. <script type="text/javascript">
		dojo.registerModulePath("company","company");
		dojo.require("company.form");
</script>
3. In the script tag in step 2, ensure that the company.form
module is loaded by the OrderTicket.html form.

## Related concepts

- Before you begin: Client types and prerequisites

## Related tasks

- Defining user interfaces for a human task
- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)
- Preparing to extend generated JSF code
- Customizing clients
- Deploying a generated client to an external runtime environment

## Related reference

- Design considerations for user interface generation