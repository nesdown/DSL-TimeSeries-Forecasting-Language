<!-- Basic data for time series initialization -->
<vector_name> :== letter | word

<!-- File manipulation functions. We use toolkit module here -->
<create_from_file> :== "(" <vector_name> ";" -toolkit.file-<file_name> ")"
<save_to_file> :== "(" <vector_name> ";" -toolkit.file-<file_name> ")"

<!-- It is possible to initialize time-series from input as well -->
<create_from_input> :== "(" <vector_format> ";" <input> ")"

<!-- length of the vector being saved into special variable -->
<get_length> :== "(" <vector_name> ")"
