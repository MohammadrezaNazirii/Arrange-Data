## frequency table
data<-read.table(file="C:/Users/ASUS/Desktop/University/Semester 3/amar/project/nahaii/continues data/input2.txt")
str(data)
data<-data$V1
head(data)

decimalplaces <- function(x) {
  if ((x %% 1) != 0) {
    nchar(strsplit(sub('0+$', '', as.character(x)), ".", fixed=TRUE)[[1]][[2]])
  } else {
    return(0)
  }
}
dvec<-vector()
for(i in 1:length(data)){
  dvec[i]<-decimalplaces(data[i])
}
unig_d<-1/(10^max(dvec))
U_d<-0.5*unig_d
U_d
n<-length(data)
#tedad rade
num<-round(1+3.322*log10(n))
num
max_val<-max(data)
min_val<-min(data)
Range_d<-(max_val+U_d)-(min_val-U_d) 
step_val<-ceiling(Range_d/num*10)/10
step_val
#taiin rade ha
data_break<-seq(min_val-U_d,max_val+U_d,step_val)
if(length(data_break)<(num+1)){data_break<-c(data_break,(data_break[num]+step_val))}
for(i in 1:length(data_break)){
  data_break[i]<-data_break[i] + U_d
}
data_break
#mid-point(markaz rade ha)
midpoint<-seq((min_val-U_d)+step_val/2,(max_val+U_d)+step_val/2,step_val)
midpoint
x<-cut(data,breaks=data_break, dig.lab = 4)
x
#taiin rade ha
y<-table(x)
y
#jadval faravani
df<-data.frame(y)
df
#add mid-point to table
df$midpnt<-midpoint
df
#add ralative frequency to table
  df$rf<-df$Freq/n
  df
View(df)
####
#add cumulative frequency to table
df$F<-cumsum(df$Freq)
df
#add relative cumulative frequency to table
df$rF<-df$F/n
df
View(df)
###################
#Pie
df$pie<-round(360*df$rf,1)
df
###################
# mean
Wmean<-sum(df$midpnt*df$Freq)/n
Wmean
Gmean<-(prod(df$midpnt^df$Freq))^(1/n)
Gmean
Hmean<-n/sum(df$Freq/df$midpnt)
Hmean

#variance
Var<-sum(df$Freq*(df$midpnt-Wmean)^2)/(n-1)
Var
Sd<-sqrt(Var)
Sd
CV<-Sd/Wmean
CV

## Histogram
data<-read.table(file="C:/Users/ASUS/Desktop/University/Semester 3/amar/project/nahaii/continues data/input2.txt")
str(data)
data<-data$V1
hist(data, nclass=num, main="Histogram plot", col="blue")


##Box Plot
boxplot(data)

