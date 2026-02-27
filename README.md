# evaluating-model-prediction-1

In crude oil, there are 2 benchmark.

- WTI (ticker: CL=F) is the benchmark price for US. They are
controlled and affected by US Market, demand, bottleneck for
shipping, etc.
- Brent (ticker: BZ=F) is the benchmark price for Europe, Asia,
and Middle East (basically global). 

Why they are different ?

WTI is landlocked at cushing (America) which mean that its
targeted market can only be around America making it sensitive to America storage constraint, pipeline, and its market.

Brent on the other hand, located near sea which mean it can reached out more country. That's why Brent usually regarded as the global benchmark.

I add checkData.py to check whether they differ that much or not
and after running it, I got
```
diff train: 100.0%
diff test: 100.0%
```
which mean that they are truly different

In evaluating the model we'll use 3 test
1. MAE (Mean abosulte error)
2. MSE (Mean square error)
3. Directional

All of these test will be checked on log(return) which is directly from the data we have (because in getData we have change the price into log(return))