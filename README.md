# MLE-counting-billionaires
</br>
An Implementation of Maximum Likelihood Estimation to estimate the number of billionaires in different countries.

Original Research Work: Motta, Victor. (2019). Estimating Poisson pseudo-maximum-likelihood rather than log-linear model of a log-transformed dependent variable. RAUSP Management Journal, 54(4), 508-518. Epub December 13, 2019.https://doi.org/10.1108/rausp-05-2019-0110
</br>
## Background Information
MLE is used to estimate parameters of a probability distribution to model a given random process.

Given C sets of classes represented by w<sub>j</sub> (0 <= j < C) where each class have a number of samples and a feature vector x.

Representing a class conditional density that fits a certain distribution.

i.e if the distribution is gaussian.
</br>
### &#420;(x | w<sub>j</sub>) &asymp; &#413;(&#613;<sub>j</sub>, &#425;<sub>k</sub>),
where &#613;<sub>j</sub> is the mean vector value for a given class and &#425;<sub>k</sub> is the standard deviation vector of its k samples.

### &#420;(x | w<sub>j</sub>) &asymp; <sup>1</sup>&frasl;<sub>&sigma;&#8730;2&Pi;</sub>e<sup>-(x-&#654;)<sup>2</sup>/2&sigma;<sup>2</sup></sup>

</br>
</br>

## Counting Billionaires
The number of billionaires is integer-valued.

Hence we consider distributions that take values only in the nonnegative integers.

(This is one reason least squares regression is not the best tool for the present problem, since the dependent variable in linear regression is not restricted to integer values)

One integer distribution is the Poisson distribution, the probability mass function (pmf) of which is
</br>

### f(y)=<sup>μ<sup>y</sup></sup>&frasl;<sub>y!</sub>e<sup>−μ</sup>,     y=0,1,2,…,∞

</br>
Poisson distribution over y for different values of μ.
</br>
![download](https://user-images.githubusercontent.com/25469826/82766926-66905380-9e23-11ea-8a6d-fdf108369fbb.png)
</br>
</br>
The dependent variable — the number of billionaires y<sub>i</sub> in country i — is modeled as a function of GDP per capita, population size, and years membership in GATT and WTO.
</br>
Hence, the distribution of y<sub>i</sub> needs to be conditioned on the vector of explanatory variables x<sub>i</sub>.
</br>
The standard formulation — the so-called *poisson regression* model —

### f(y)=<sup>μ<sup>y<sub>i</sub></sup></sup>&frasl;<sub>y!</sub>e<sup>−μ<sub>i</sub></sup>,                 y=0,1,2,…,∞
### where, μ<sub>i</sub> = exp(x<sub>i</sub>B) = exp(B<sub>0</sub> + B<sub>1</sub>x<sub>i1</sub> + B<sub>2</sub>x<sub>i2</sub> + ... + B<sub>k</sub>x<sub>ik</sub>)

From the data observations x<sub>i</sub> and the arbitary paramteres B<sub>j</sub> we produce the best fit f(y)' to f(y).

### Requirements
numpy >= 1.18.4 </br>
matlotlib >= 3.2.1 </br>
pandas >= 0.25.3 </br>
scipy >= 1.4.1 </br>
statsmodels >= 0.11.1 </br>

## Applying MLE numerically
In our model for number of billionaires, the featue vector contains 4 parameters that we need to estimate.
GDP per capita, population size, and years membership in GATT and WTO.

B = [B<sub>0</sub>,  B<sub>1</sub>,  B<sub>2</sub>,  B<sub>3</sub>]<sup>T<sup>

Many distributions do not have nice, analytical solutions and therefore require numerical methods to solve for parameter estimates.

One such numerical method is the Newton-Raphson algorithm. </br>
Our goal is to find the maximum likelihood estimate B'. </b>
To estimate the model using MLE, we want to maximize the likelihood that our estimate B' is the true parameter B.
Intuitively, we want to find the B that best fits our data.

Since the number of billionaires in different countries (y<sub>i</sub>) are independent on each other, we can model the likelihood funcion &#8466;(B) as follows.

f(y<sub>i</sub> | x<sub>i</sub>, B) = &Pi;<sub>i=1</sub><sup>n</sup> <sup>μ<sup>y<sub>i</sub></sup></sup>&frasl;<sub>y!</sub>e<sup>−μ<sub>i</sub></sup>