# ml-album-popularity
Predict Genre and Popularity of a music album, based on the album's cover.


**1 - Spotify API**

Contains the implementation of the SpotifyAPI class.

Features:
* Spotify API token generation and renewal
* Various endpoints requests

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/1%20-%20Spotify%20API.ipynb)


**2 - Build Dataset**

Used to build the dataset.

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/2%20-%20Build%20Dataset.ipynb)


**3 - Explore Dataset**

Expore the dataset regarding album popularity and genres. 

Spotify API returns multiple genres per artist, we keep the most common and filter out the rest based on their corellation.

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/3%20-%20Explore%20Dataset.ipynb)



**Challenges so far**
* Spotify API prevents continuous requests for downloading album cover images. Added 1 sec delay and a retry method.
* Artist genres are returned as a list, which is a bit tricky to handle in pandas. 
* Spotify API returns a large number of different genres. Had to keep the most common ones by using corellation matrix. (Perform clustering for better results)
