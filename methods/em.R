require(Amelia)

path = '/Users/jinhwansuk/git/STA714_final/data'

data <- read.csv(paste(path, '/boston_nan.csv', sep = ""), header = TRUE, row.names = 1)
a.out <- amelia(data, m = 1,ords = 'RAD')

write.csv(a.out$imputations$imp1, paste(path, '/em_imp.csv', sep = ""))
