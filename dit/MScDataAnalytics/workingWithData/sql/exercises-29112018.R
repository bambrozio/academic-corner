# http://b-tierney.com/msc-working-with-data/wwd_wk5/
# http://b-tierney.com/wp-content/uploads/2018/10/L5-1-R_and_Databases.pdf
setwd("~/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics/workingWithData/sql/")

install.packages("RJDBC")
library("RJDBC")

# Might be needed to perform in the terminal: 
# sudo ln -f -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib

# Create connection driver and open connection to the database
# First, download the ojdbc from Oracle website
jdbcDriver <- JDBC(driverClass="oracle.jdbc.OracleDriver", classPath="/usr/local/bin/ojdbc7.jar")

dbConn <- dbConnect(jdbcDriver, 
                    "jdbc:oracle:thin:@//redwood.ict.ad.dit.ie:1521/pdb12c.ict.ad.dit.ie",
                    "bambrozio", "d16128063")

myTables <- dbGetQuery(dbConn, "select * from all_tables where owner = 'BAMBROZIO'")
myTables

# With prepare statement:
dbGetQuery(dbConn, "select * from all_tables where owner = ?", "BAMBROZIO")

dbListFields(dbConn, 'STUDENT') 

dbExistsTable(dbConn, "CARS", "BAMBROZIO")

tableData <- dbReadTable(dbConn, "CARS" )
tableData


cars <- mtcars
dbWriteTable(dbConn, "CARS", cars)
carsData <- dbReadTable(dbConn, "CARS")
dim(carsData)

dbWriteTable(dbConn, "CARS", cars, append=TRUE, overwrite=FALSE)
carsData <- dbReadTable(dbConn, "CARS")
dim(carsData)
