# Question 6

## The Model

For my model I would use a classifier with the output being one hot-encodings with 1 meaning they would throw a pickoff and 0 meaning they wouldn't. In general I would try to keep the model small with something like 2-3 Dense layers. For a loss function I would use Binary Crossentropy as that is best for classification questions with 2 classes.

## The Inputs

For my inputs of the model I would use, the identities of the pitcher, the runner on first, and the first baseman as inputs that would first be processed by an embedding layer. For the rest of the inputs I would use, measurements every 3 seconds of the distance of the runner on first away from the base, the sprint speed of the runner on first, and the past percentage of pick off's thrown for the given pitcher. In general these would probably be all of my features as I wouldn't want to over complicate the model with features that may have very minimal effects on the outcome.

## Training

For training of my model I would train it on the following inputs above with the labels being wether that given pitch resulted in a pitch or a pickoff being thrown. I would use a high amount of epochs (100+) and a low learning rate (0.001) as this problem might take a while for this model to learn without overfitting. I would also implement class weights if the network over generalizes and just guesses no-pick off for all inputs as definitely more pitches result in no-pick off being thrown then those that do.
