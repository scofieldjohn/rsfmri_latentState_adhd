


library(ggplot2)
library(ez)
library(car)
library(MOTE)
library(cowplot)
library(reshape2)
options(scipen = 999)
setwd("C:/Users/jel7c5/OneDrive - University of Missouri/John PhD Mizzou/Research/EP/Resting-state functional connectivity sex differences/adhd/adhd200")#setwd("C:/Users/jel7c5/Desktop/adhd200")
theme = theme(panel.grid.major = element_blank(), 
              panel.grid.minor = element_blank(), 
              panel.background = element_blank(), 
              axis.line = element_line(colour = "black"), 
              legend.key = element_rect(fill = "white"),
              text = element_text(size = 15))

ITI_data1 = read.csv('ITI_data_combined1.csv')
ITI_data2 = read.csv('ITI_data_combined2.csv')
ITI_data3 = read.csv('ITI_data_combined3.csv')
ITI_data4 = read.csv('ITI_data_combined4.csv')
ITI_data5 = read.csv('ITI_data_combined5.csv')

ITI_data_sd1 = read.csv('ITI_data_combined_sd1.csv')
ITI_data_sd2 = read.csv('ITI_data_combined_sd2.csv')
ITI_data_sd3 = read.csv('ITI_data_combined_sd3.csv')
ITI_data_sd4 = read.csv('ITI_data_combined_sd4.csv')
ITI_data_sd5 = read.csv('ITI_data_combined_sd5.csv')

colnames(ITI_data1) = c('ID','ITI','TYPE')
colnames(ITI_data2) = c('ID','ITI','TYPE')
colnames(ITI_data3) = c('ID','ITI','TYPE')
colnames(ITI_data4) = c('ID','ITI','TYPE')
colnames(ITI_data5) = c('ID','ITI','TYPE')
colnames(ITI_data_sd1) = c('ID','ITI','TYPE')
colnames(ITI_data_sd2) = c('ID','ITI','TYPE')
colnames(ITI_data_sd3) = c('ID','ITI','TYPE')
colnames(ITI_data_sd4) = c('ID','ITI','TYPE')
colnames(ITI_data_sd5) = c('ID','ITI','TYPE')

ITI_data1$partno = 1:nrow(ITI_data1)
ITI_data2$partno = 1:nrow(ITI_data2)
ITI_data3$partno = 1:nrow(ITI_data3)
ITI_data4$partno = 1:nrow(ITI_data4)
ITI_data5$partno = 1:nrow(ITI_data5)
ITI_data_sd1$partno = 1:nrow(ITI_data_sd1)
ITI_data_sd2$partno = 1:nrow(ITI_data_sd2)
ITI_data_sd3$partno = 1:nrow(ITI_data_sd3)
ITI_data_sd4$partno = 1:nrow(ITI_data_sd4)
ITI_data_sd5$partno = 1:nrow(ITI_data_sd5)

ITI_data1$sex = ifelse(ITI_data1$TYPE == 'fa','F',
                      ifelse(ITI_data1$TYPE == 'fc','F',
                             ifelse(ITI_data1$TYPE == 'ma','M','M')))
ITI_data1$diag = ifelse(ITI_data1$TYPE == 'fa','A',
                       ifelse(ITI_data1$TYPE == 'fc','C',
                              ifelse(ITI_data1$TYPE == 'ma','A','C')))
ITI_data2$sex = ifelse(ITI_data2$TYPE == 'fa','F',
                       ifelse(ITI_data2$TYPE == 'fc','F',
                              ifelse(ITI_data2$TYPE == 'ma','M','M')))
ITI_data2$diag = ifelse(ITI_data2$TYPE == 'fa','A',
                        ifelse(ITI_data2$TYPE == 'fc','C',
                               ifelse(ITI_data2$TYPE == 'ma','A','C')))
ITI_data3$sex = ifelse(ITI_data3$TYPE == 'fa','F',
                       ifelse(ITI_data3$TYPE == 'fc','F',
                              ifelse(ITI_data3$TYPE == 'ma','M','M')))
ITI_data3$diag = ifelse(ITI_data3$TYPE == 'fa','A',
                        ifelse(ITI_data3$TYPE == 'fc','C',
                               ifelse(ITI_data3$TYPE == 'ma','A','C')))
ITI_data4$sex = ifelse(ITI_data4$TYPE == 'fa','F',
                       ifelse(ITI_data4$TYPE == 'fc','F',
                              ifelse(ITI_data4$TYPE == 'ma','M','M')))
ITI_data4$diag = ifelse(ITI_data4$TYPE == 'fa','A',
                        ifelse(ITI_data4$TYPE == 'fc','C',
                               ifelse(ITI_data4$TYPE == 'ma','A','C')))
ITI_data5$sex = ifelse(ITI_data5$TYPE == 'fa','F',
                       ifelse(ITI_data5$TYPE == 'fc','F',
                              ifelse(ITI_data5$TYPE == 'ma','M','M')))
ITI_data5$diag = ifelse(ITI_data5$TYPE == 'fa','A',
                        ifelse(ITI_data5$TYPE == 'fc','C',
                               ifelse(ITI_data5$TYPE == 'ma','A','C')))

ITI_data_sd1$sex = ifelse(ITI_data_sd1$TYPE == 'fa','F',
                       ifelse(ITI_data_sd1$TYPE == 'fc','F',
                              ifelse(ITI_data_sd1$TYPE == 'ma','M','M')))
ITI_data_sd1$diag = ifelse(ITI_data_sd1$TYPE == 'fa','A',
                        ifelse(ITI_data_sd1$TYPE == 'fc','C',
                               ifelse(ITI_data_sd1$TYPE == 'ma','A','C')))
ITI_data_sd2$sex = ifelse(ITI_data_sd2$TYPE == 'fa','F',
                       ifelse(ITI_data_sd2$TYPE == 'fc','F',
                              ifelse(ITI_data_sd2$TYPE == 'ma','M','M')))
ITI_data_sd2$diag = ifelse(ITI_data_sd2$TYPE == 'fa','A',
                        ifelse(ITI_data_sd2$TYPE == 'fc','C',
                               ifelse(ITI_data_sd2$TYPE == 'ma','A','C')))
ITI_data_sd3$sex = ifelse(ITI_data_sd3$TYPE == 'fa','F',
                       ifelse(ITI_data_sd3$TYPE == 'fc','F',
                              ifelse(ITI_data_sd3$TYPE == 'ma','M','M')))
ITI_data_sd3$diag = ifelse(ITI_data_sd3$TYPE == 'fa','A',
                        ifelse(ITI_data_sd3$TYPE == 'fc','C',
                               ifelse(ITI_data_sd3$TYPE == 'ma','A','C')))
ITI_data_sd4$sex = ifelse(ITI_data_sd4$TYPE == 'fa','F',
                       ifelse(ITI_data_sd4$TYPE == 'fc','F',
                              ifelse(ITI_data_sd4$TYPE == 'ma','M','M')))
ITI_data_sd4$diag = ifelse(ITI_data_sd4$TYPE == 'fa','A',
                        ifelse(ITI_data_sd4$TYPE == 'fc','C',
                               ifelse(ITI_data_sd4$TYPE == 'ma','A','C')))
ITI_data_sd5$sex = ifelse(ITI_data_sd5$TYPE == 'fa','F',
                       ifelse(ITI_data_sd5$TYPE == 'fc','F',
                              ifelse(ITI_data_sd5$TYPE == 'ma','M','M')))
ITI_data_sd5$diag = ifelse(ITI_data_sd5$TYPE == 'fa','A',
                        ifelse(ITI_data_sd5$TYPE == 'fc','C',
                               ifelse(ITI_data_sd5$TYPE == 'ma','A','C')))



ITI_data1$sex = factor(ITI_data1$sex)
ITI_data1$diag = factor(ITI_data1$diag)
ITI_data2$sex = factor(ITI_data2$sex)
ITI_data2$diag = factor(ITI_data2$diag)
ITI_data3$sex = factor(ITI_data3$sex)
ITI_data3$diag = factor(ITI_data3$diag)
ITI_data4$sex = factor(ITI_data4$sex)
ITI_data4$diag = factor(ITI_data4$diag)
ITI_data5$sex = factor(ITI_data5$sex)
ITI_data5$diag = factor(ITI_data5$diag)
ITI_data_sd1$sex = factor(ITI_data_sd1$sex)
ITI_data_sd1$diag = factor(ITI_data_sd1$diag)
ITI_data_sd2$sex = factor(ITI_data_sd2$sex)
ITI_data_sd2$diag = factor(ITI_data_sd2$diag)
ITI_data_sd3$sex = factor(ITI_data_sd3$sex)
ITI_data_sd3$diag = factor(ITI_data_sd3$diag)
ITI_data_sd4$sex = factor(ITI_data_sd4$sex)
ITI_data_sd4$diag = factor(ITI_data_sd4$diag)
ITI_data_sd5$sex = factor(ITI_data_sd5$sex)
ITI_data_sd5$diag = factor(ITI_data_sd5$diag)



FO_comb_dat = read.csv('hmm2_frac_occ_common.csv')

ITI_data1$sub = FO_comb_dat$sub
ITI_data2$sub = FO_comb_dat$sub
ITI_data3$sub = FO_comb_dat$sub
ITI_data4$sub = FO_comb_dat$sub
ITI_data5$sub = FO_comb_dat$sub
ITI_data_sd1$sub = FO_comb_dat$sub
ITI_data_sd2$sub = FO_comb_dat$sub
ITI_data_sd3$sub = FO_comb_dat$sub
ITI_data_sd4$sub = FO_comb_dat$sub
ITI_data_sd5$sub = FO_comb_dat$sub

ITI_noout1 = subset(ITI_data1, abs(scale(ITI_data1$ITI)) < 3)
ITI_noout2 = subset(ITI_data2, abs(scale(ITI_data2$ITI)) < 3)
ITI_noout3 = subset(ITI_data3, abs(scale(ITI_data3$ITI)) < 3)
ITI_noout4 = subset(ITI_data4, abs(scale(ITI_data4$ITI)) < 3)
ITI_noout5 = subset(ITI_data5, abs(scale(ITI_data5$ITI)) < 3)
ITI_noout_sd1 = subset(ITI_data_sd1, abs(ITI_data_sd1$ITI) < 3)
ITI_noout_sd2 = subset(ITI_data_sd2, abs(ITI_data_sd2$ITI) < 3)
ITI_noout_sd3 = subset(ITI_data_sd3, abs(ITI_data_sd3$ITI) < 3)
ITI_noout_sd4 = subset(ITI_data_sd4, abs(ITI_data_sd4$ITI) < 3)
ITI_noout_sd5 = subset(ITI_data_sd5, abs(ITI_data_sd5$ITI) < 3)


ITI_noout1$sex = factor(ITI_noout1$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout2$sex = factor(ITI_noout2$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout3$sex = factor(ITI_noout3$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout4$sex = factor(ITI_noout4$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout5$sex = factor(ITI_noout5$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout1$diag = factor(ITI_noout1$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout2$diag = factor(ITI_noout2$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout3$diag = factor(ITI_noout3$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout4$diag = factor(ITI_noout4$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout5$diag = factor(ITI_noout5$diag, levels = c('A','C'), labels = c('ADHD','Control'))

ITI_noout_sd1$sex = factor(ITI_noout_sd1$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd2$sex = factor(ITI_noout_sd2$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd3$sex = factor(ITI_noout_sd3$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd4$sex = factor(ITI_noout_sd4$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd5$sex = factor(ITI_noout_sd5$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd1$diag = factor(ITI_noout_sd1$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout_sd2$diag = factor(ITI_noout_sd2$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout_sd3$diag = factor(ITI_noout_sd3$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout_sd4$diag = factor(ITI_noout_sd4$diag, levels = c('A','C'), labels = c('ADHD','Control'))
ITI_noout_sd5$diag = factor(ITI_noout_sd5$diag, levels = c('A','C'), labels = c('ADHD','Control'))


## FA
#estimated = actual
# 1 = 5
# 2 = 2
# 3 = 4
# 4 = 3
# 5 = 1

## FC
# 1 = 2
# 2 = 4
# 3 = 3
# 4 = 1
# 5 = 5

## MA
# 1 = 2
# 2 = 4
# 3 = 1
# 4 = 5
# 5 = 3

## MC
# 1 = 5
# 2 = 4
# 3 = 3
# 4 = 1
# 5 = 2

new1 = data.frame(rbind(
  subset(ITI_noout5, TYPE == 'fa'),
  subset(ITI_noout2, TYPE == 'fc'),
  subset(ITI_noout2, TYPE == 'ma'),
  subset(ITI_noout5, TYPE == 'mc')
))
new2 = data.frame(rbind(
  subset(ITI_noout2, TYPE == 'fa'),
  subset(ITI_noout4, TYPE == 'fc'),
  subset(ITI_noout4, TYPE == 'ma'),
  subset(ITI_noout4, TYPE == 'mc')
))
new3 = data.frame(rbind(
  subset(ITI_noout4, TYPE == 'fa'),
  subset(ITI_noout3, TYPE == 'fc'),
  subset(ITI_noout1, TYPE == 'ma'),
  subset(ITI_noout3, TYPE == 'mc')
))
new4 = data.frame(rbind(
  subset(ITI_noout3, TYPE == 'fa'),
  subset(ITI_noout1, TYPE == 'fc'),
  subset(ITI_noout5, TYPE == 'ma'),
  subset(ITI_noout1, TYPE == 'mc')
))
new5 = data.frame(rbind(
  subset(ITI_noout1, TYPE == 'fa'),
  subset(ITI_noout5, TYPE == 'fc'),
  subset(ITI_noout3, TYPE == 'ma'),
  subset(ITI_noout2, TYPE == 'mc')
))

new1x = data.frame(rbind(
  subset(ITI_noout_sd5, TYPE == 'fa'),
  subset(ITI_noout_sd2, TYPE == 'fc'),
  subset(ITI_noout_sd2, TYPE == 'ma'),
  subset(ITI_noout_sd5, TYPE == 'mc')
))
new2x = data.frame(rbind(
  subset(ITI_noout_sd2, TYPE == 'fa'),
  subset(ITI_noout_sd4, TYPE == 'fc'),
  subset(ITI_noout_sd4, TYPE == 'ma'),
  subset(ITI_noout_sd4, TYPE == 'mc')
))
new3x = data.frame(rbind(
  subset(ITI_noout_sd4, TYPE == 'fa'),
  subset(ITI_noout_sd3, TYPE == 'fc'),
  subset(ITI_noout_sd1, TYPE == 'ma'),
  subset(ITI_noout_sd3, TYPE == 'mc')
))
new4x = data.frame(rbind(
  subset(ITI_noout_sd3, TYPE == 'fa'),
  subset(ITI_noout_sd1, TYPE == 'fc'),
  subset(ITI_noout_sd5, TYPE == 'ma'),
  subset(ITI_noout_sd1, TYPE == 'mc')
))
new5x = data.frame(rbind(
  subset(ITI_noout_sd1, TYPE == 'fa'),
  subset(ITI_noout_sd5, TYPE == 'fc'),
  subset(ITI_noout_sd3, TYPE == 'ma'),
  subset(ITI_noout_sd2, TYPE == 'mc')
))





#### ANOVA
ezANOVA(data = new1, wid = partno,
        between = .(sex, diag), dv = ITI, type = 3) #ns
ezANOVA(data = new2, wid = partno,
        between = .(sex, diag), dv = ITI, type = 3) #sex
ezANOVA(data = new3, wid = partno,
        between = .(sex, diag), dv = ITI, type = 3) #sex
ezANOVA(data = new4, wid = partno,
        between = .(sex, diag), dv = ITI, type = 3) #sex
ezANOVA(data = new5, wid = partno,
        between = .(sex, diag), dv = ITI, type = 3) #ns



(t1m = with(new1, tapply(ITI, list(sex),mean,na.rm=T)))
(t1s = with(new1, tapply(ITI, list(sex),sd,na.rm=T)))
t1l = with(new1, tapply(ITI, list(sex), length))
d.ind.t(t1m[1],t1m[2],t1s[1],t1s[2],t1l[1],t1l[2])$d

(t2m = with(new2, tapply(ITI, list(sex),mean,na.rm=T)))
(t2s = with(new2, tapply(ITI, list(sex),sd,na.rm=T)))
t2l = with(new2, tapply(ITI, list(sex), length))
d.ind.t(t2m[1],t2m[2],t2s[1],t2s[2],t2l[1],t2l[2])$d

(t3m = with(new3, tapply(ITI, list(sex),mean,na.rm=T)))
(t3s = with(new3, tapply(ITI, list(sex),sd,na.rm=T)))
t3l = with(new3, tapply(ITI, list(sex), length))
d.ind.t(t3m[1],t3m[2],t3s[1],t3s[2],t3l[1],t3l[2])$d

(t4m = with(new4, tapply(ITI, list(sex),mean,na.rm=T)))
(t4s = with(new4, tapply(ITI, list(sex),sd,na.rm=T)))
t4l = with(new4, tapply(ITI, list(sex), length))
d.ind.t(t4m[1],t4m[2],t4s[1],t4s[2],t4l[1],t4l[2])$d

(t5m = with(new5, tapply(ITI, list(sex),mean,na.rm=T)))
(t5s = with(new5, tapply(ITI, list(sex),sd,na.rm=T)))
t5l = with(new5, tapply(ITI, list(sex), length))
d.ind.t(t5m[1],t5m[2],t5s[1],t5s[2],t5l[1],t5l[2])$d


mean(abs(d.ind.t(t2m[1],t2m[2],t2s[1],t2s[2],t2l[1],t2l[2])$d),
     abs(d.ind.t(t3m[1],t3m[2],t3s[1],t3s[2],t3l[1],t3l[2])$d),
     abs(d.ind.t(t4m[1],t4m[2],t4s[1],t4s[2],t4l[1],t4l[2])$d))




ezANOVA(data = new1x, wid = partno, between = .(sex, diag), #ns
        dv = ITI, type = 3)
ezANOVA(data = new2x, wid = partno, between = .(sex, diag), 
        dv = ITI, type = 3)
ezANOVA(data = new3x, wid = partno, between = .(sex, diag), # diag
        dv = ITI, type = 3)
ezANOVA(data = new4x, wid = partno, between = .(sex, diag), 
        dv = ITI, type = 3)
ezANOVA(data = new5x, wid = partno, between = .(sex, diag),
        dv = ITI, type = 3)


(x1m = with(new1x, tapply(ITI, list(diag),mean,na.rm=T)))
(x1s = with(new1x, tapply(ITI, list(diag),sd,na.rm=T)))
x1l = with(new1x, tapply(ITI, list(diag), length))
d.ind.t(x1m[1],x1m[2],x1s[1],x1s[2],x1l[1],x1l[2])$d

(x2m = with(new2x, tapply(ITI, list(diag),mean,na.rm=T)))
(x2s = with(new2x, tapply(ITI, list(diag),sd,na.rm=T)))
x2l = with(new2x, tapply(ITI, list(diag), length))
d.ind.t(x2m[1],x2m[2],x2s[1],x2s[2],x2l[1],x2l[2])$d

(x3m = with(new3x, tapply(ITI, list(diag),mean,na.rm=T)))
(x3s = with(new3x, tapply(ITI, list(diag),sd,na.rm=T)))
x3l = with(new3x, tapply(ITI, list(diag), length))
d.ind.t(x3m[1],x3m[2],x3s[1],x3s[2],x3l[1],x3l[2])$d

(x4m = with(new4x, tapply(ITI, list(diag),mean,na.rm=T)))
(x4s = with(new4x, tapply(ITI, list(diag),sd,na.rm=T)))
x4l = with(new4x, tapply(ITI, list(diag), length))
d.ind.t(x4m[1],x4m[2],x4s[1],x4s[2],x4l[1],x4l[2])$d

(x5m = with(new5x, tapply(ITI, list(diag),mean,na.rm=T)))
(x5s = with(new5x, tapply(ITI, list(diag),sd,na.rm=T)))
x5l = with(new5x, tapply(ITI, list(diag), length))
d.ind.t(x5m[1],x5m[2],x5s[1],x5s[2],x5l[1],x5l[2])$d














