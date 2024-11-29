### Methods

### Parent

### Helpers

<!-- image -->

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| JSON Structure of the Object                                                                                                                                                                                                                                                                                                                                                                                                         | JSON Structure of the Object   | JSON Structure of the Object   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------------|
| {     		  "geometry": {},    		    	  	    "location" : {    			    	  	    	  	   "A": -- ,     			    	  	    	  	   "F":--     		    	  	   }    			  	   },      			  "html\_attributes": {    			 	  	  	     "icon": --,     			 	  	  		 "id": --,     			 	  	  		 "name": --      			  },     			  "opening\_hours": --,    		 	  	  	  "place\_id": --,    		 	  	  	  "types": {} ,    		 	  	  	  "vicinity" : --     		  } |                                |                                |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name      | Type      | Default   | Description                                                                                                                                          |
|-----------|-----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| latitude  | {decimal} |           | the latitude of the location                                                                                                                         |
| longitude | {decimal} |           | the longitude of the location                                                                                                                        |
| search    | {object}  |           | this object contains the items radius and types of businesses that you are searching for. Max radius is 15km.  For acceptable types, see Place Types |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |