# csgo_prediction

### Building a model to predict the round winners in a CSGO match as a part of the Skybox-Technologies [csgo.ai](https://csgo.ai/) challenge

Link for dataset: https://github.com/Skybox-Technologies/csgo-ai-competition

### Steps to Preprocess data:

#### 1. Place the initial dataset in the folder 'datasets/dataset_initial' in the program directory and run 'preprocess.py'. This program extracts all the relevant features from the .json dataset files.

#### 2. Run 'cleaning.py'. This program filters the useful data eliminating the useless feeatures.

#### 3. Run 'finalizing.py'. This adds some new features and finalizes data for training. The final dataset is in 'datasets/dataset_finalized' folder.