# Defining external properties by using the Script Adapter widget

## About this task

## Procedure

To define external properties by using the Script Adapter widget:

1. Define an external properties collection in the model layer as a single object.

For example, provide a collection of property
objects:var model = {
    properties: {
        "name": {
            id: "name",
            type: "string",
            value: "Rip Van Winkle"
        },
        "age": {
            id: "age",
            type: "integer",
            value: 200
        },
    },
}
2. Implement the definition, retrieval, and persistence of external properties by using custom
code. Typically, this custom code is implemented in the Script Adapter widget.

Your custom code can call the bind method of the PropertyCollectionController class, as shown
below, to include your external properties collection in the set of properties that are associated
with the view. You can bind as many collections as you wish. Specify a unique collection identifier
for each collection.controller.bind(collectionId, collectionName, model);
The PropertyCollectionController class supports standard model signatures with which it can bind
implicitly. In some cases, your application might need to support a non-standard model signature
that is associated with your application. If so, you can provide an Integration object as part of
the binding to instruct the controller how to interact with the associated
model.controller.bind(collectionId, collectionName, model, integration);
The PropertyCollectionController class automatically updates the state of the model as changes
occur within the view.
3. Set up wiring for the Script Adapter widget.

It is important to specify an incoming event for the Script Adapter widget that is loaded before
the actual widget loads on the page. For example, for the Add Cases page, wire the Script Adapter
widget to the Page Container's 'Send new case information' event. Similarly, you can use the Page
Container's 'Send case information event' for the Case Details page and the Page Container's 'Send
work item' event for the Work Details page. These events allow the Script Adapter widget to execute
the JavaScript code so that the external properties are bound to the Properties widget before it is
loaded.
4. Use external properties that are defined by using a model object.

The following example illustrates the definition of a typical collection of external properties
of various data types.
{
    properties: {
        "description": {
            id: "description",
            name: "Description",
            label: "Description",
            type: "string",
            cardinality: "single",
            value: "description here"
        },
        "price": {
            id: "price",
            name: "Price",
            label: "Price",
            type: "float",
            cardinality: "single",
            value: 22.2
        },
        "booleantest": {
            id: "booleantest",
            name: "booleantest",
            label: "booleantest",
            type: "boolean",
            cardinality: "single"
        },
        "datetimeTEST": {
            id: "datetimeTEST",
            name: "datetimeTEST",
            label: "datetimeTEST",
            type: "datetime",
            cardinality: "single"
        },
        "quantityINT": {
            id: "quantityINT",
            name: "quantityINT",
            label: "quantityINT",
            type: "integer",
            cardinality: "single"
        },
        "total": {
            id: "total",
            name: "Total",
            label: "Total",
            type: "float",
            cardinality: "single",
        },
        "MyMultiInteger": {
            id: "MyMultiInteger",
            type: "integer",
            cardinality: "multi",
            value: [1, 2, 3]
        },
        "multiCategory": {
            id: "multiCategory",
            name: "MultiCategory",
            label: "MultiCategory",
            type: "integer",
            cardinality: "multi",
            choices: [{
                    label: "Small",
                    value: 0
                },
                {
                    label: "Large",
                    value: 1
                }
            ]
        }
    }
}
5. Create an Integration object.

Creating a custom Integration object is useful when you are working with a third-party model
object with a different signature than the default signature that is supported by the controller.
Some examples include an incoming JSON object from a web service or an object from within your
existing model layer. You can create a custom Integration object that tells the controller how to
map its attributes to fields of the custom object.
 The following script demonstrates how to create the Integration object that is used for such a
binding. The bold below shows the parts that are important to note for custom integration
configuration.// Create the external properties model with the custom model signature.
var model = {
    props: {
        "PhoneNumber": {
            symbolicName: "PhoneNumber",
            name: “Phone Number”,
            type: "string",
            multiValue: false,
            value: "949-559-2213"
        }
    }
};

// Create a custom integration object for the custom model signature.
var integration = new Integration();
integration.mergeConfiguration(basicIntegrationConfiguration);
integration.mergeConfiguration(customIntegrationConfiguration);

// Add a binding for the external properties to the controller.
collectionController.bind("External", "External", model, integration);
 The following script illustrates the custom integration configuration object that is required
for the custom integration in the previous script. Typically, this configuration object is
implemented in a separate Dojo module. Merge the basic integration configuration before you merge
your custom integration configuration as shown in the previous
script.var customIntegrationConfiguration = {
    bindings: {
        collection: {
            attributes: {
                properties: {
                //Get the properties from the "props" member of the model.
                    get: "props"
                        }
            }
        },
        property: {
            attributes: {
                common: {
                    id: {
                         //Get the id from the "symbolicName" member of
                         //the model object.
                         get: "symbolicName"
                    },
                    cardinality:
                          // Compute the cardinality from the "multiValue"
                          //member of the model object.
                          get: function(model) {
                              return model.multiValue ? "multi" : "single";
                    }

                }
            }
        }
    }
}