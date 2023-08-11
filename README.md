# Box-Analytics-Data-cleaner
This tool cleans the usage analytics data from box storage service.

### Methodology
1.	Place all the data from the web scraper in the “data” folder.
2.	Run the script.
3.	The output files will be in the “cleaned files” folder.

### Functionality
1. Remove lines that are just descriptive of timeline and do not contain any relevant data.
2. Join the Location Data with its corresponding time and action data.
3. Match and remove any duplication of data caused by the web scraping flow.

### Error Handling
If you face any formatting errors are found this can be addressed by opening the file > save as > Change the encoding to ANSI or other python friendly formats.
