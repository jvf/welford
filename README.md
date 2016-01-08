# welford - Online Variance with Welfords method

Computes the variance of a dataset by incrementally adding values to an accumulator. Welfords method is more numerically stable than the standard method.

Welfords method goes back to a 1962 paper by B. P. Welford and is presented in Donald Knuth’s Art of Computer Programming, Vol 2.

This implemenation is modelled after the following:
* [Accurately computing running variance](www.johndcook.com/blog/standard_deviation)
* [Computing skewness and kurtosis in one pass](www.johndcook.com/blog/skewness_kurtosis)

See also:
* [WP: Online Algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm)
* [WP: Parallel Algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm)
