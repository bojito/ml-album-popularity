<!-- PROJECT LOGO -->
<p align="center">
  <h3 align="center">Predict Album Genre and Popularity</h3>
  <p align="center">
    Predict Genre and Popularity of a music album, based on the album's cover.
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#spotify-api">Spotify API</a>
    </li>
    <li>
      <a href="#build-dataset">Build Dataset</a>
    </li>
        <li>
      <a href="#explore-dataset">Explore Dataset</a>
    </li>
    <li>
      <a href="#challenges-so-far">Challenges so far</a>
    </li>
  </ol>
</details>
 
 
## Spotify API 

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/1%20-%20Spotify%20API.ipynb)

Contains the implementation of the SpotifyAPI class.

Features:
* Spotify API token generation and renewal
* Various endpoints requests




## Build Dataset

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/2%20-%20Build%20Dataset.ipynb)

Used to build the dataset.




## Explore Dataset 

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/3%20-%20Explore%20Dataset.ipynb)

Expore the dataset regarding album popularity and genres. 

Spotify API returns multiple genres per artist, we keep the most common and filter out the rest based on their corellation.



## Feature Extraction 

[view notebook](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/4%20-%20Extract%20Features.ipynb)

The following features are extracted from each image:

* `has_face`: true if the image contains face(s)
* `hog_descriptor`



## Challenges so far 

* Spotify API prevents continuous requests for downloading album cover images. Added 1 sec delay and a retry method.
* Artist genres are returned as a list, which is a bit tricky to handle in pandas. 
* Spotify API returns a large number of different genres. Had to keep the most common ones by using corellation matrix. (Perform clustering for better results)
