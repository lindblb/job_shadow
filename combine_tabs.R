
library(dplyr)
library(purrr)
library(readxl)


FILE_LOCATION = "data/iterate.xlsx"

SHEETS <- readxl::excel_sheets(FILE_LOCATION)

SHEETS

raw_data <- purrr::map2(FILE_LOCATION, SHEETS, readxl::read_excel)

combined_tabs <- dplyr::bind_rows(raw_data)
combined_tabs

# Write to a new excel
write.csv(combined_tabs, "combined_tabs.csv")
