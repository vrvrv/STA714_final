require(mice)

path = '/Users/jinhwansuk/git/STA714_final/data'

data <- read.csv(paste(path, '/boston_nan.csv', sep = ""), header = TRUE, row.names = 1)
data$RAD <- as.factor(data$RAD)
res <- mice(data, m=1,
            method = c('pmm', 'pmm', 'polyreg', 'pmm', 'pmm', "", "", "", "", "", "", "", "", ""),
            visitSequence = "monotone")
data$RM <- res$imp$RM
