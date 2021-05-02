<!-- Input values, the name of the error -->
<error_name> :== letter | word

<!-- Custom reason user inputs throwing an error -->
<reason_name> :== letter | word

<!-- Error code number -->
<error_code> :== digit | [0-999]

<!-- Set of commands to be handled on errors -->
<command_set> :== <commands> & [1 | 1-10]

<!-- Throw and Catch grammar -->
<throw> :== <error_name> "(" <reason_message> ")"
<catch> :== "(" <command_set> ")"