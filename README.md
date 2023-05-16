# Notes #

Github does not support files larger than 100mb. The comments CSV is >200mb.

Because of this, the original file of all comments, requested at 05/16/2023 08:43 AM ET, is archived in a zip file.

Extract the file first to use the script.

The script will output a CSV file of just the sample. It will add 4 columns:

- Row Number: This will become the first column, and corresponds with the row number in the original file

Three columns to indicate sentiment (a value of 1 labels the sentiment as matching that column):

- Supports/Not Far Enough: The comment supports the rule change OR says the rule change did not go far enough in including trans identified individuals. 
- Opposes Rule: The comment opposes the rule change because the it goes too far in including trans identified individuals. 
- Unknown: Unable to identify the sentiment of the comment.