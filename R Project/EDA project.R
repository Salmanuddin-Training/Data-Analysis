#Loading of Dataset

heart = read.csv("C:/Users/DELL/Desktop/Heart.csv")
library(corrplot)
corrplot(cor(heart), type="upper")
heart = subset(heart, select=c(-restecg, -chol,-fbs))
#Let's change the categorical variables to the corresponding strings:
heart$sex[heart$sex == 0] = "female"
heart$sex[heart$sex == 1] = "male"

heart$cp[heart$cp == 0] = "typical angina"
heart$cp[heart$cp == 1] = "atypical angina"
heart$cp[heart$cp == 2] = "non-anginal pain"
heart$cp[heart$cp == 3] = "asymptomatic"

heart$exang[heart$exang == 0] = "no"
heart$exang[heart$exang == 1] = "yes"

heart$exang[heart$exang == 0] = "no"
heart$exang[heart$exang == 1] = "yes"

heart$slope[heart$slope == 0] = "upsloping"
heart$slope[heart$slope == 1] = "flat"
heart$slope[heart$slope == 2] = "downsloping"

heart$thal[heart$thal == 1] = "normal"
heart$thal[heart$thal == 2] = "fixed defect"
heart$thal[heart$thal == 3] = "reversible defect"

heart$target1 = heart$target

heart$target1[heart$target1 == 0] = "no heart disease"
heart$target1[heart$target1 == 1] = "heart disease"

#The dataset is ready. Let’s dive into exploratory analysis.
#Exploratory Analysis
#the proportion of the people with heart disease and with no heart disease in the dataset.

prop.table(table(heart$target1))

round(prop.table(table(heart$target1)),2)

#2 Finding:-
#Age of the Population
#This is a common idea that older people are more prone to get heart disease. Here is the 
#distribution of the age of the population in the dataset.

library(ggplot2)

ggplot(heart, aes(x=age)) +
  geom_histogram() + ggtitle("Distribution of age of the population")+
  xlab("Age") + ylab("Density")

heart$age_grp = cut(heart$age, breaks = seq(25, 77, 4))

#3-Findings
#Find the number of people with heart disease for each age group.
library(dplyr)

target_by_age = heart %>%
  group_by(age_grp) %>%
  summarise(heart_disease = sum(target))

target_by_age

target_by_age %>%
  ggplot(aes(x=age_grp, y=heart_disease)) +
  geom_bar(stat="identity", fill="#f68060", alpha=.6, width=.4) +
  xlab("") + ylab("No. of People with Heart Disease") + ggtitle("No of 
Heart disease in Age Group") + 
  theme_bw()

#For that let’s find the proportion of people with heart disease in each group.
prop_in_age = heart %>%
  group_by(age_grp) %>%
  summarise(heart_disease_proportion = round(sum(target)/n(), 3)*100)

#Here is the bar plot of this data:
prop_in_age %>%
  ggplot(aes(x=age_grp, y=heart_disease_proportion)) +
  geom_bar(stat="identity", fill="#f68060", alpha=.6, width=.4) +
  xlab("") + ylab("Proportion of People with Heart Disease") + 
  ggtitle("Proportion of Heart disease in Age Groups") + 
  theme_bw()

round(prop.table(table(heart$sex)),2)

round(prop.table(table(heart$sex, heart$target1)), 2)
