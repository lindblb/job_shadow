
library(dplyr)
library(purrr)
library(readxl)

# Where is the excel doc we are reading in?
FILE_LOCATION = "data/iterate.xlsx"

# I want to see all the sheets or tabs in it
SHEETS <- readxl::excel_sheets(FILE_LOCATION)

# Inspect them
SHEETS

# Read all the sheets into a "list"
raw_data <- purrr::map2(FILE_LOCATION, SHEETS, readxl::read_excel)

# Combine the sheets into one table
combined_tabs <- dplyr::bind_rows(raw_data)
combined_tabs

# Write to a new excel doc
readr::write_csv(combined_tabs, "combined_tabs.csv")
