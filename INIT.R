
PACKAGES <- c(
  "dplyr",
  "purrr",
  "readxl",
  "readr",
  "reticulate"
)

install.packages(PACKAGES)

library(reticulate)

reticulate::py_install(c("beautifulsoup4", "requests"))