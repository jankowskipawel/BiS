data <- read.csv("napoje_po_reklamie.csv",sep=";")
pepsi <- data[['pepsi']]
fanta <- data[['cola']]

print("PEPSI: ")
print(summary(pepsi))
print("FANTA: ")
print(summary(fanta))