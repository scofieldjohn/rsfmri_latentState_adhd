

library(ggplot2)
library(ez)
library(car)
library(MOTE)
library(BayesFactor)
library(cowplot)
library(reshape2)
options(scipen = 999)
setwd("C:/Users/jscof/OneDrive - University of Missouri/John PhD Mizzou/Research/EP/Resting-state functional connectivity sex differences/adhd/adhd200")#setwd("C:/Users/jel7c5/Desktop/adhd200")
theme = theme(panel.grid.major = element_blank(), 
              panel.grid.minor = element_blank(), 
              panel.background = element_blank(), 
              axis.line = element_line(colour = "black"), 
              legend.key = element_rect(fill = "white"),
              text = element_text(size = 15))

ITI_data = read.csv('ITI_data_combined.csv')
NT_data = read.csv('NT_data_combined.csv')
ITI_data_sd = read.csv('ITI_data_combined_sd.csv')
colnames(ITI_data) = c('ID','ITI','TYPE')
colnames(NT_data) = c('ID','NT','TYPE')
colnames(ITI_data_sd) = c('ID','ITI','TYPE')
ITI_data$partno = 1:nrow(ITI_data)
NT_data$partno = 1:nrow(NT_data)
ITI_data_sd$partno = 1:nrow(ITI_data_sd)

ITI_data$sex = NA
ITI_data$diag = NA
for(x in 1:nrow(ITI_data)){
  if(ITI_data$TYPE[x] == 'fa'){
    ITI_data$sex[x] = 'F'
    ITI_data$diag[x] = 'A'
  } else if(ITI_data$TYPE[x] == 'fc'){
    ITI_data$sex[x] = 'F'
    ITI_data$diag[x] = 'C'
  } else if(ITI_data$TYPE[x] == 'ma'){
    ITI_data$sex[x] = 'M'
    ITI_data$diag[x] = 'A'
  } else if(ITI_data$TYPE[x] == 'mc') {
    ITI_data$sex[x] = 'M'
    ITI_data$diag[x] = 'C'
  }
}

ITI_data_sd$sex = NA
ITI_data_sd$diag = NA
for(x in 1:nrow(ITI_data_sd)){
  if(ITI_data_sd$TYPE[x] == 'fa'){
    ITI_data_sd$sex[x] = 'F'
    ITI_data_sd$diag[x] = 'A'
  } else if(ITI_data_sd$TYPE[x] == 'fc'){
    ITI_data_sd$sex[x] = 'F'
    ITI_data_sd$diag[x] = 'C'
  } else if(ITI_data_sd$TYPE[x] == 'ma'){
    ITI_data_sd$sex[x] = 'M'
    ITI_data_sd$diag[x] = 'A'
  } else if(ITI_data_sd$TYPE[x] == 'mc') {
    ITI_data_sd$sex[x] = 'M'
    ITI_data_sd$diag[x] = 'C'
  }
}

NT_data$sex = NA
NT_data$diag = NA
for(x in 1:nrow(NT_data)){
  if(NT_data$TYPE[x] == 'fa'){
    NT_data$sex[x] = 'F'
    NT_data$diag[x] = 'A'
  } else if(NT_data$TYPE[x] == 'fc'){
    NT_data$sex[x] = 'F'
    NT_data$diag[x] = 'C'
  } else if(NT_data$TYPE[x] == 'ma'){
    NT_data$sex[x] = 'M'
    NT_data$diag[x] = 'A'
  } else if(NT_data$TYPE[x] == 'mc'){
    NT_data$sex[x] = 'M'
    NT_data$diag[x] = 'C'
  }
}

ITI_data$sex = factor(ITI_data$sex)
ITI_data$diag = factor(ITI_data$diag)

ITI_data_sd$sex = factor(ITI_data_sd$sex)
ITI_data_sd$diag = factor(ITI_data_sd$diag)

NT_data$sex = factor(NT_data$sex)
NT_data$diag = factor(NT_data$diag)

FO_comb_dat = read.csv('hmm2_frac_occ_common.csv')


ITI_data$sub = FO_comb_dat$sub
ITI_data_sd$sub = FO_comb_dat$sub
NT_data$sub = FO_comb_dat$sub


summary(ITI_data)
summary(ITI_data_sd)
summary(NT_data)
summary(FO_comb_dat)

hist(ITI_data$ITI)
hist(ITI_data_sd$ITI)
hist(NT_data$NT)
hist(FO_comb_dat$FO)

table(ITI_data$sex, ITI_data$diag)
table(ITI_data_sd$sex, ITI_data_sd$diag)
table(NT_data$sex, NT_data$diag)




## link up sites
sitez = read.csv('ID_site.csv')
FO_comb_dat$site = 'x'
for(x in 1:nrow(FO_comb_dat)){
  id = FO_comb_dat$sub[x]
  FO_comb_dat$site[x] = as.character(subset(sitez, ScanDirID == id)$Site2[1])
}
ITI_data$site = FO_comb_dat$site
NT_data$site = FO_comb_dat$site
ITI_data_sd$site = FO_comb_dat$site

##ITI histogram
(ITIh = ggplot(ITI_data, aes(x=ITI)) + geom_histogram() + facet_grid(TYPE ~ site))
(ITIhs = ggplot(ITI_data_sd, aes(x=ITI)) + geom_histogram() + facet_grid(TYPE ~ site))
(NTh = ggplot(NT_data, aes(x=NT)) + geom_histogram() + facet_grid(TYPE ~ site))



zscores = scale(ITI_data$ITI)
summary(abs(zscores) < 3)
ITI_noout = subset(ITI_data, abs(zscores) < 3)
table(ITI_noout$sex, ITI_noout$diag)

zscoress = scale(ITI_data_sd$ITI)
summary(abs(zscoress) < 3)
ITI_noout_sd = subset(ITI_data_sd, abs(zscoress) < 3)
table(ITI_noout_sd$sex, ITI_noout_sd$diag)

zscores2 = scale(NT_data$NT)
summary(abs(zscores2) < 3)
NT_noout = subset(NT_data, abs(zscores2) < 3)
table(NT_noout$sex, NT_noout$diag)

zscores3 = scale(FO_comb_dat$FO)
summary(abs(zscores3) < 3)
FO_noout = subset(FO_comb_dat, abs(zscores3) < 3)
table(FO_noout$sex, FO_noout$diag)

ITI_noout$sex = factor(ITI_noout$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout$diag = factor(ITI_noout$diag, levels = c('A','C'), labels = c('ADHD','Control'))

ITI_noout_sd$sex = factor(ITI_noout_sd$sex, levels = c('F','M'), labels = c('Female','Male'))
ITI_noout_sd$diag = factor(ITI_noout_sd$diag, levels = c('A','C'), labels = c('ADHD','Control'))

NT_noout$sex = factor(NT_noout$sex, levels = c('F','M'), labels = c('Female','Male'))
NT_noout$diag = factor(NT_noout$diag, levels = c('A','C'), labels = c('ADHD','Control'))



#### ANOVA
ezANOVA(data = ITI_noout,
        wid = partno,
        between = .(sex, diag),
        dv = ITI,
        type = 3)

with(ITI_noout, tapply(ITI, list(sex, diag),mean,na.rm=T))
with(ITI_noout, tapply(ITI, list(sex, diag),sd,na.rm=T))

with(ITI_noout, tapply(ITI, list(sex),mean,na.rm=T))
with(ITI_noout, tapply(ITI, list(sex),sd,na.rm=T))

with(ITI_noout, tapply(ITI, list(diag),mean,na.rm=T))
with(ITI_noout, tapply(ITI, list(diag),sd,na.rm=T))


ezANOVA(data = ITI_noout_sd,
        wid = partno,
        between = .(sex, diag),
        dv = ITI,
        type = 3)



with(ITI_noout_sd, tapply(ITI, list(sex),mean,na.rm=T))
with(ITI_noout_sd, tapply(ITI, list(sex),sd,na.rm=T))

with(ITI_noout_sd, tapply(ITI, list(diag),mean,na.rm=T))
with(ITI_noout_sd, tapply(ITI, list(diag),sd,na.rm=T))

with(ITI_noout_sd, tapply(ITI, list(sex, diag),mean,na.rm=T))
with(ITI_noout_sd, tapply(ITI, list(sex, diag),sd,na.rm=T))


ezANOVA(data = NT_noout,
        wid = partno,
        between = .(sex, diag),
        dv = NT,
        type = 3)

with(NT_noout, tapply(NT, list(sex, diag),mean,na.rm=T))
with(NT_noout, tapply(NT, list(sex, diag),sd,na.rm=T))

with(NT_noout, tapply(NT, list(sex),mean,na.rm=T))
with(NT_noout, tapply(NT, list(sex),sd,na.rm=T))

with(NT_noout, tapply(NT, list(diag),mean,na.rm=T))
with(NT_noout, tapply(NT, list(diag),sd,na.rm=T))


cor.test(ITI_data$ITI, NT_data$NT)




############ Plots
library(plyr)
ITI_noout$sex = revalue(ITI_noout$sex, c("Female"="Girls", "Male"="Boys"))
ITI_noout_sd$sex = revalue(ITI_noout_sd$sex, c("Female"="Girls","Male"="Boys"))
NT_noout$sex = revalue(NT_noout$sex, c("Female"="Girls","Male"="Boys"))

dodge = position_dodge(width = 0.8)

ITI_plot = ggplot(ITI_noout, aes(diag,y=ITI, fill = sex)) +
  geom_violin(aes(fill=sex,color=sex),alpha=.8, position = dodge) +
  geom_boxplot(outlier.shape = NA,position=dodge, width=0.1)+
  theme + 
  xlab("Diagnosis") +
  ylab("ITI Means") + scale_fill_manual(values=c('firebrick4','dodgerblue4')) +
  scale_color_manual(values=c('firebrick4','dodgerblue4'))

ITI_plot_sd = ggplot(ITI_noout_sd, aes(diag,y=ITI, fill = sex)) +
    geom_violin(aes(fill=sex,color=sex),alpha=.8, position = dodge) +
    geom_boxplot(outlier.shape = NA,position=dodge, width=0.1)+
    theme + 
    xlab("Diagnosis") +
    ylab("ITI Variability")+ scale_fill_manual(values=c('firebrick4','dodgerblue4')) +
  scale_color_manual(values=c('firebrick4','dodgerblue4'))

theme_set(theme_cowplot(font_size = 16))
plot_grid(ITI_plot,ITI_plot_sd, ncol = 1, labels = c('A)','B)'))




(NT_plot = ggplot(NT_noout, aes(diag,y=NT, fill = sex)) +
    geom_violin(aes(fill=sex,color=sex),alpha=.8, position = dodge) +
    geom_boxplot(outlier.shape = NA,position=dodge, width=0.1)+
    theme + 
    xlab("Diagnosis") +
    ylab("NT")+ scale_fill_manual(values=c('firebrick4','dodgerblue4')) +
    scale_color_manual(values=c('firebrick4','dodgerblue4')))




#### FO Table interaction
FA = read.csv('FO3FA_stateresolved.csv')
FC = read.csv('FO3FC_stateresolved.csv')
MA = read.csv('FO3MA_stateresolved.csv')
MC = read.csv('FO3MC_stateresolved.csv')


FAlong = melt(FA, id.vars = c('partno','sub','sex','diag'))
colnames(FAlong) = c('partno','sub','sex','diag','state', 'FO')
FClong = melt(FC, id.vars = c('partno','sub','sex','diag'))
colnames(FClong) = c('partno','sub','sex','diag','state', 'FO')
MAlong = melt(MA, id.vars = c('partno','sub','sex','diag'))
colnames(MAlong) = c('partno','sub','sex','diag','state', 'FO')
MClong = melt(MC, id.vars = c('partno','sub','sex','diag'))
colnames(MClong) = c('partno','sub','sex','diag','state', 'FO')

bigD = rbind(FAlong,FClong,MAlong,MClong)

ezANOVA(data = bigD,
        wid = sub,
        between = .(sex, diag),
        within = .(state),
        dv = FO,
        type = 3)






