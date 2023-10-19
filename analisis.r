library(tidyverse)
library(janitor)
library(skimr)
library(GGally)
library(ggpubr)
library(hexbin)
library(glue)
library(scales)
library(corrplot)

dataset <- read.csv("S:\\Github\\preditiva\\dataset\\origen.csv")
cc <- read.csv("S:\\Github\\preditiva\\dataset\\train.csv")
dataset %>%
  select(runtimeMinutes,titleType) %>%
  View()

cc %>%
    select(averageRating, numVotes, runtimeMinutes, isAdult, startYear,endYear,directors_exp,writers_exp) %>%
  cor(method = "spearman") %>%
  corrplot(type = "upper", method = "circle", tl.col = "black", tl.srt = 45)
# Calculate the correlation between each column and averageRating
correlations <- sapply(cc, function(x) cor(x, cc$averageRating, method = "spearman"))

# Create a data frame with the results
results <- data.frame(variable = names(cc), correlation = correlations)

# Print the results
print(results)


dataset %>%
  group_by(titleType)%>%
  n()%>%
  View()

glimpse(dataset)
skim(dataset)
# if isAdult is > 1, then delete the row
dataset <- dataset %>% filter(isAdult <= 1)
# count where runtimeMinutes is 0
dataset %>%
    filter(runtimeMinutes != 0) %>%
    count()
ggplot(dataset, aes(x = averageRating)) +
    geom_histogram()

# finding the correlation of averageRating and the rest of the variables

dataset %>%
    select(averageRating, numVotes, runtimeMinutes, startYear,endYear,revenue) %>%
    cor(method = "spearman") %>%
    corrplot(type = "upper", method = "circle", tl.col = "black", tl.srt = 45)

#ANOVA test between averageRating and isAdult with graph. isAdult is categorical, so it should be 1 or 0, not between 0 and 1
dataset %>%
    ggplot(aes(x = factor(isAdult), y = averageRating, fill = factor(isAdult))) +
    geom_boxplot() +
    geom_hline(yintercept = 6.5, linetype = "dashed") +
    scale_fill_manual(values=c("blue", "red")) +
    labs(x = "isAdult", y = "averageRating", fill = "isAdult") +
    theme_minimal() +
    theme(text = element_text(size=20))

aov(isAdult ~ averageRating, data = dataset) %>% summary() # P-value muy chico, hay diferencia significativa entre las medias

dataset %>%
    group_by(titleType)%>%
    summarise(mean = mean(averageRating), sd = sd(averageRating), n = n()) %>%
    arrange(desc(mean))%>%
    View()

#ANOVA test between averageRating and titleType

dataset %>%
    ggplot(aes(x = factor(titleType), y = averageRating, fill = factor(titleType))) +
    geom_boxplot() +
    geom_hline(yintercept = 6.5, linetype = "dashed") +
    
    labs(x = "titleType", y = "averageRating", fill = "titleType") +
    theme_minimal() +
    theme(text = element_text(size=20))


aov(titleType ~ averageRating, data = dataset) %>% summary()

#Show the % of completeness of the dataset on all the columns
dataset %>%
    select(language,isOriginalTitle) %>%
    map_df(~sum(!is.na(.x))/length(.x)) %>%
    gather() %>%
    ggplot(aes(x = key, y = value)) +
    geom_bar(stat = "identity") +
    geom_text(aes(label = scales::percent(value, accuracy = 1)), vjust = -0.5) +
    theme_minimal() +
    theme(text = element_text(size=20))

dataset %>%
  group_by(directors) %>%
  count() %>%
  View()
d2 = read.csv("S:\\Github\\preditiva\\train.csv")

#corr plot between all the variables
d2 %>%
    select(averageRating, numVotes, runtimeMinutes, isAdult, startYear,endYear,directors_exp,writers_exp,revenue) %>%
    cor(method = "spearman") %>%
    corrplot(type = "upper", method = "circle", tl.col = "black", tl.srt = 45)
