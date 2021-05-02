<!-- Basic data for time series initialization -->
<time_series_name> :== letter | word
<!-- Please note that there are two variants of time-series format -->
<time_series_format> :== "wide" | "long"

<!-- Simple notation for console input -->
<input> :== <console_data>

<!-- Size of the time-series being saved into special length -->
<get_size> :== "(" <time_series_name> ")"
<!-- It is possible to manipulate with data as well -->
<change_time_format> :== "(" <time_series_name> ";" <time_series_format> ")"

<!-- File manipulation functions. We use toolkit module here -->
<create_from_file> :== "(" <time_series_name> ";" -toolkit.file-<file_name> ")"
<save_to_file> :== "(" <time_series_name> ";" -toolkit.file-<file_name> ")"

<!-- It is possible to initialize time-series from input as well -->
<create_from_input> :== "(" <time_series_format> ";" <input> ")"


