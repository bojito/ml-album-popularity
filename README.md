<!-- PROJECT LOGO -->
<p align="center">
  <h2 align="center">Predict Album Genre and Popularity</h2>
  <p align="center">
    Predict Genre and Popularity of a music album, based on the album's cover.
  </p>
  <br>
  <br>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
      <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#spotify-api">Spotify API</a>
    </li>
    <li>
      <a href="#build-dataset">Build Dataset</a>
    </li>
        <li>
      <a href="#explore-dataset">Explore Dataset</a>
    </li>
     </li>
    <li>
      <a href="#feature-extraction">Feature Extraction</a>
    </li>
     <li>
      <a href="#classify-genre">Classify Genre</a>
    </li>
    <li>
      <a href="#predict-popularity">Predict Popularity</a>
    </li>
    <li>
      <a href="#challenges-so-far">Challenges so far</a>
    </li>
      <li>
      <a href="#next-steps">Next Steps</a>
    </li>
  </ol>
  <br>
  <br>
</details>
 

## Installation 

1. Get a free [Spotify API](https://developer.spotify.com/) Key
2. Clone the repo
   ```sh
   git clone https://github.com/bojito/ml-album-popularity.git
   ```
3. Install requirements  
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API keys in `config.py`
   ```JS
   client_id = 'YOUR_CLIENT_ID'
   client_secret = 'YOUR_CLIENT_SECRET'
  
## Spotify API    

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/1%20-%20Spotify%20API.ipynb)
  
Contains the implementation of the SpotifyAPI class. 

The Client Credentials Flow is used for authentication, please refer to [https://developer.spotify.com](https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow)

**Features:**
* Spotify API token generation and renewal
* Various endpoints requests

**Usage:**
* Create a config.py with your `client_id`, `client_secret` keys.



## Build Dataset

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/2%20-%20Build%20Dataset.ipynb)

To build the dataset, the playlist [*Most Popular Songs of All Time*](https://open.spotify.com/playlist/4o8NBsWreC3OnKePUYw0dg?si=KfEHTYmESlORo6CeDsf1bg) from Spotify was used.

Up to the point of downloading the metadata, the playlist consisted of **3.300 songs** and 204 hours of music.

**Key points**

* the playlist contained songs from the same album. Each album cover is downloaded once and the final dataset has **2.370 unique album cover images**.
* the genres are maintained at artist level in the spotify API. Seperate request per album artist.
* the dataset is stored in a `json` file with the following keys: {artist_id, artist_name, album_id, album_name, album_popularity, genres, album_url}

A sample `json` dataset file is stored in `\data` directory.

## Explore Dataset 

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/3%20-%20Explore%20Dataset.ipynb)

Expore the dataset regarding album popularity and genres. 

**Key points**

* Filter out albums with popularity less than 40. Spotify API returns a popularity value between 0-100.
* Spotify API returns multiple genres per artist, we keep the most common and filter out the rest based on their corellation.
* The albums are annotated as pop, rap and rock. The albums that don't belong to one of these genres are removed. 



The final dataset contains **1.592 samples** and has the folowing distribution of genres:

| Genre         | Albums Count      | 
| ------------- |-----------:| 
| pop           |         751| 
| rap           |         542| 
| rock          |         299| 



## Feature Extraction 

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/4%20-%20Extract%20Features.ipynb)

The following features are extracted from each image:

* `has_face`: that indicates if a **face** is present in the album cover
* `hog_descriptor` : that quantifies the **structure** of the image  
* `hsv_hist` : that quantifies the **color** of the image
* `lbp_hist` : that quantifies the **texture** of the image

**Combining Features**

`hog_descriptor`, `hsv_hist`, `lbp_hist` are  feature descriptors that quantify an image **globally**.  To combine them, we concatenate each feature vector to form a single global feature vector. 

<p align="center">
  <a>
    <img src="other/features.png" alt="Logo" width="830" height="141">
  </a>
</p>

## Classify Genre

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/5%20-%20Classify%20Genre.ipynb)

A set of different classifiers is tested using K-Fold Cross Validation. 

Random Forest Classifier gives the best overall accuracy but **overfits** the train dataset. Our model has **Low Bias** but **High Variance** and does not generalize well.

The most notable result is the F1-Score for `pop` genre: 65%

*Check Next Steps section for optimization proposals.*

**Sample Execution on Test Data**

<p align="center">
  <a>
    <img src="other/pred_test.png" alt="Logo" width="731" height="238">
  </a>
</p>

## Predict Popularity

[`view notebook`](https://nbviewer.jupyter.org/github/bojito/ml-album-popularity/blob/main/6%20-%20Predict%20Popularity.ipynb)

We classify albums as **popular** if album popularity > 70, **common** otherwise. 

The tested classifiers can not make useful predictions, F1-Score is 50%.

*Check Next Steps section for optimization proposals.*

## Challenges so far 

* Spotify API prevents continuous requests for downloading album cover images. Added 1 sec delay and a retry method.
* Artist genres are returned as a list, which is a bit tricky to handle in pandas. 
* Spotify API returns a large number of different genres. Had to keep the most common ones by using corellation matrix. (Perform clustering for better results)
* Dataset contains more examples from pop genre compared to rock, rap. Should balance classes with more data.


## Next Steps 

To address the overfitting issue, the following steps can be performed:

* Collect more data for each class. Try 500-1000 images per class.
* Data augmentation using various transformations on the dataset images.
* Use also Local Image features with the Bag of Visual Words(BOVW) technique. For example SIFT, SURF, KAZE.
* Consider using a dimensionality reduction technique.
