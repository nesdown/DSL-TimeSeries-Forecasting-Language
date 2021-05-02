<!-- Variable for setting the chart name -->
<chart_name> :== letter | word

<!-- A command displaying the chart on screen -->
<chart_show> :== "(" <chart_name> ")"

<!-- A command for creating the chart from time stamp -->
<chart_create> :== "(" <chart_name> ";" <time_stamp_name>")"

<!-- Chart commands for file -->
<chart_save> :== "(" <chart_name> ";" <file_name> ")"
<chart_load> :== "(" <chart_name> ";" <file_name> ")"

<!-- Multiline commands -->
<chart_add> :== "(" <chart_name> ";" <time_stamp_name>")"
<chart_remove> :== "(" <chart_name> ";" <time_stamp_name>")"