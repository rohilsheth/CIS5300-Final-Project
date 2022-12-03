# Metric
Our metric is the F1 score obtained when comparing the predicted labels with the actual labels. Specifically, the F1 score is the harmonic mean of the precision and recall and is defined as (precision * recall) / (precision + recall). F1 scores are often used to evaluate sexism classifiers, as we saw in our literature review.

# How to run
Run `python3 score.py [manual/simple/strong] [optional y_pred] [optional y_test]` in the command line to obtain a score. If you want to score manual lists, pass in y_pred and y_test as a series of 0s and 1s separated by commas and no spaces (see example arguments below).

Example arguments: 
- python3 score.py manual 0,1,0,1 1,1,1,1
- python3 score.py simple
python3 score.py strong

Example outputs using the example arguments: 
- 0.6666666666666666
- 