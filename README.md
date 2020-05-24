# MLE-counting-billionaires
An Implementation of Maximum Likelihood Estimation to estimate the number of billionaires in different countries.

Original Research Work: Motta, Victor. (2019). Estimating Poisson pseudo-maximum-likelihood rather than log-linear model of a log-transformed dependent variable. RAUSP Management Journal, 54(4), 508-518. Epub December 13, 2019.https://doi.org/10.1108/rausp-05-2019-0110

## Background Information
MLE is used to estimate parameters of a probability distribution to model a given random process.

Given C sets of classes represented by w<sub>j</sub> (0 <= j < C) where each class have a number of samples and a feature vector x.

Representing a class conditional density that fits a certain distribution.

i.e if the distribution is gaussian.
### &#420;(x | w<sub>j</sub>) &asymp; &#413;(&#613;<sub>j</sub>, &#425;<sub>k</sub>),
where &#613;<sub>j</sub> is the mean vector value for a given class and &#425;<sub>k</sub> is the standard deviation vector of its k samples.

### &#420;(x | w<sub>j</sub>) &asymp; <sup>1</sup>&frasl;<sub>&sigma;&#8730;2&Pi;</sub>e<sup>-(x-&#654;)<sup>2</sup>/2&sigma;<sup>2</sup></sup>


## Counting Billionaires
The number of billionaires is integer-valued.

Hence we consider distributions that take values only in the nonnegative integers.

(This is one reason least squares regression is not the best tool for the present problem, since the dependent variable in linear regression is not restricted to integer values)

One integer distribution is the Poisson distribution, the probability mass function (pmf) of which is

### f(y)=<sup>μ<sup>y</sup></sup>&frasl;<sub>y!<sub>e<sup>−μ</sup>,     y=0,1,2,…,∞



