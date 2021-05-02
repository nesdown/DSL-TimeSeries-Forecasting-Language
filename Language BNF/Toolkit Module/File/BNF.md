<!-- Here we describe all possible variable names and values to be used. -->
<variable_name> :== letter | name

<!-- To reach correct decomposition, we build the file link out of several primitive structures -->
<address> :== <variable_name>
<time_series_name> :== <variable_name>
<file_link> :== <address>

<!-- Process format is a way of interacting with the document -->
<process_format> = w | r
<open> :== "(" <file_link> ";" <process_format> ")"

<!-- Read and write syntax is the same: the first one is time-series data, next -  file link -->
<read> :== "(" <time_series_name> ";" <file_link> ")"
<write> :== "(" <time_series_name> ";" <file_link> ")"