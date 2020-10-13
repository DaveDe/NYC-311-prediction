Code for NYCER: A Non-Emergency Response Predictor for NYC using Sparse Gaussian Conditional Random Fields

GCRF model taken from https://github.com/dswah/sgcrfpy

Objective:

Predict NYC 311 short term median response time

Filtering:

- Remove rows that dont have valid close date
- Remove rows that are not responded to by a top 8 agency
- Remove rows that dont have a top 32 complaint type
- Remove rows with complaint type Request Large Bulky Item Collection
- Remove rows that dont have 1 of the 5 major boroughs listed
- Remove rows before 2015
- Remove rows that have negative response times

Splitting:

- Split filtered data into 3 datasets: agency, complaint type, and location
- For each dataset, produce 2 time series for each type of agency, complaint type, and location. One time series for median response time per day, one for demand per day.
- For each time series, split data into samples using a sliding window that moves 1 day at a time. Each sample has t weeks historical data, and 1 week of future data to predict.

Models:

- GCRF Response, using only historical response times.
- GCRF Demand, using historical response times, and historical demand.
- Baseline linear regression, fits a line on each test sample.

Evaluation:

- RMSE, averaged per day across samples.
- Relative error, also averaged per day.

Future ideas:

- Experiment with descriptors (more descriptive complaint types).
- Long term response time prediction