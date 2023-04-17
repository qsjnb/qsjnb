#读入数据
a<-read.table("E:/R/data/file12.csv",sep=",",header = T)
x<-ts(a$output,start=1949)
#lm函数拟合
t1<-c(1:60)
t2<-t1^2
x.fit1<-lm(x~t1+t2)
summary(x.fit1)
#nls函数拟合
x.fit2<-nls(x~a+b*t1+c*t1^2,start = list(a=1,b=1,c=1))
summary(x.fit2)
y<-predict(x.fit2)
y<-ts(y,start = 1949)
plot(x,type = "p")
lines(y,col=2,lwd=2)