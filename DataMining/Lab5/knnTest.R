iris <- read.csv(url("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"), header = FALSE)
names(iris) <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species")
income <- read.csv(file="income_te.csv", header = TRUE)
income

summary(iris)

install.packages("data.table")
require(fread)
library(fread)
data <- fread("income_te.csv", select = c("age","education_cat","capital_gain","capital_loss","hour_per_week"))


iris

install.packages("class")
install.packages("FNN")
install.packages("KNN")

normalize <- function(x) {
num <- x - min(x) 
denom <- max(x) - min(x)
return (num/denom) }

YourNormalizedDataSet <- as.data.frame(lapply(income, normalize))

iris_norm <- as.data.frame(lapply(income[1:15], normalize))
summary(iris_norm)

require(FNN)
set.seed(1234)

ind <- sample(2, nrow(income), replace=TRUE, prob=c(0.67, 0.33))
ind

income.map <- c("Male"=1, "Female"=2)    
y <- income.map[as.character(income)]
y

income.training <- income[ind==1, (1:15)] 
income.test <- income[ind==2, (1:15)] 
income.training
income.test


income.trainLabels <- income[ind==1, 1:15] 
income.testLabels <- income[ind==2, 1:15]
income.trainLabels
income.testLabels
cl = income.trainLabels[,1]
knn(income.trainLabels, income.testLabels, cl, k = 5)
income_pred <- knn(train = (income.training), test =(income.test), cl = income.trainLabels, k=3)
income_pred

install.packages("gmodels")
library(gmodels)

CrossTable(x = income.testLabels, y = income_pred, prop.chisq=FALSE)



