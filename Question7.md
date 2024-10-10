# Question 7

## Finding X

For finding X I used excel to run a simple linear regression with WAR and Year as my independent variables and Year-to-Year as my dependent variable. The results of this rounded to the second decimal point was

Intercept: -9605.46

WAR Coefficient: -4.97

Year Coefficient: 4.75

Using this to now predict the final 2 years of what the team would pay for the player given the Year-to-Year model.

To do this we do (WAR Coefficient _ That years war) + (Year Coefficient _ That year) + Intercept. The results are as follows

2031: 21.76
2032: 27.99

Now adding all our totals for the player given the Year-to-Year model we have that we would pay them a total of

.76 + .78 + .8 + 6 + 10 + 15 + 21.76 + 27.99 = 83.09

Now looking at our current sum of our guranteed contract we have

2 + 2.5 + 4.5 + 7.5 + 10.5 + 14.5 + 19 = 60.5

Taking the differences of these two totals we get what we would pay to break even:

X = 83.09 - 60.5 = 22.59

So I would offer $22.59 Million to the player in 2032 for the guranteed contract

## Improvements and Assumptions

For this estimate I made the assumption that WAR and Years where linearly related to payment. This is obviously not true, as when a player gets older they eventually become valued less instead of more. A fix that could be made to this is using non linear regression. Some form of polynomial regression would definitely be more effective for modeling this. I also didn't take into account the differences on pricing the terms of the contracts may have. For example the year-to-year creates value from its ability to no re-sign. Alternatively the 8-year contract makes sure the player stays for that time. I would account for this given more time.
