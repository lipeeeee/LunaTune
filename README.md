# LunaTune
Predicting music genre via deep learning.

# Datasets
## Pre-built
[GTZAN](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/data)

## Self-Built
Like [LDANet](https://github.com/lipeeeee/league-draft-analyzer), we would likely need to extract & parse songs from either
youtube/soundcloud(not sure about spotify rate limits, but we can surpass both yt and soundcloud) + we would need a database
that contains the genres of all of the songs in order for us to actually train the DL model.

# "Hacking" data
If limited data is an issue we can split a song in chunks of `x` seconds. However this will probably
come at some accuracy cost.
