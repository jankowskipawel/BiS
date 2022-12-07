wzr_csv <- read.csv("Wzrost.csv", header = FALSE, sep=",")

data_wzr <- as.numeric(wzr_csv[1,])

print("WZROST: ")
print(mean(data_wzr))
print(sd(data_wzr))
print(mad(data_wzr))
print(var(data_wzr))
print(min(data_wzr))
print(max(data_wzr))