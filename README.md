# Crop yield Prediction with Deep Learning
The necessary code for the AAAI-17 paper. "Deep Gaussian Process for Crop Yield Prediction Based on Remote Sensing Data"

This is a preliminary version.

Here is a brief introduction on the utilities for each folder.

**"/download data"** How we download data from Google Earth Engine to Google Drive. Users then need to export data from Google Drive to their local folder, e.g., their clusters.

**"/clean data"** How the raw data is preprocessed, including 3-D histogram calculation

**"/model"** The CNN/LSTM structure

**"/model_batch"** Since we are training different models for each year and each month, a batch code is used for training.

**"/model_semi_supervised"** A recent contribution, extending the model with semi-supervised deep generative model.

**"/result_analysis"** Plot results, plot yield map, etc.

For more information, please contact Jiaxuan You.

youjiaxuan@gmail.com or jiaxuan@stanford.edu.