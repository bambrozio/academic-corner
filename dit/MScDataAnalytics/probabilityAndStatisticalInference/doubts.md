# Doubts

# W1:
- Ok, we use range with ordinal data. But, for which purpose?

- Is the Variance used ONLY to calculate standard deviation, or does it have any other purpose? 

- Slide 77 says the IQR of `"2, 4, 6, 8, 10, 12, 14, 20, 30, 60"` is 10, but R says 12:
    ```
    > IQR(c(2, 4, 6, 8, 10, 12, 14, 20, 30, 60))
    [1] 12
    > quantile(c(2, 4, 6, 8, 10, 12, 14, 20, 30, 60))
    0%  25%  50%  75% 100% 
    2.0  6.5 11.0 18.5 60.0
    ```
Why? (realise that the formula taught it's not applied in R): `IQR = (Q3 - Q1) / 2`
Ignoring the first as it brought 5 quantiles:
(18.5 - 6.5) / 2 = 6
Looks like R simply does Q4 - Q2

---

W2:
 - About fish example. Following instructions of slides, Standard Deviation of `3, 4, 5, 6, 8, 10` is 6.8. But in R, i says 2.6:
 ```
 > sd(c(3, 4, 5, 6, 8, 10))
 [1] 2.607681
 ```
 > only if I square it I will have 6.8. Why R doesn't complete the formula? Is it correct to assume that R `sd` formula returns the Variance instead?

