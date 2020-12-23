require(Amelia)

path = '/Users/jinhwansuk/git/STA714_final/data'
data <- read.csv(paste(path, '/train_test/nan/boston_nan_', as.character(i), ".csv", sep = ""),
                                    header = TRUE, row.names = 1)

for (i in 1:100){
  data <- read.csv(paste(path, '/train_test/nan/boston_nan_', as.character(i), ".csv", sep = ""),
                   header = TRUE, row.names = 1)
  a.out <- amelia(data, m = 5,ords = 'RAD')
  res <- (a.out$imputations$imp1
          +a.out$imputations$imp2
          +a.out$imputations$imp3
          +a.out$imputations$imp4
          +a.out$imputations$imp5)/5
  write.csv(res, 
            paste(path, '/train_test/imp/em5/em_imp', as.character(i), '.csv', sep = ""))
  
}
