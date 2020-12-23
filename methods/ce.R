require(mice)

path = '/Users/jinhwansuk/git/STA714_final/data'

for (i in 1:100){
  data <- read.csv(paste(path, '/train_test/nan/boston_nan_', as.character(i), ".csv", sep = ""),
                   header = TRUE, row.names = 1)
  
  data$RAD <- as.factor(data$RAD)
  res <- mice(data, m=5,
              method = c('pmm', 'pmm', 'polyreg', 'pmm', 'pmm', "", "", "", "", "", "", "", "", ""),
              visitSequence = "monotone")
  imputed.data <- complete(res, m=5)
  
  write.csv(imputed.data, paste(path, '/train_test/imp/ce5/ce_imp', as.character(i), '.csv', sep = ""))
  
}
res$imp
