
# Honolulu rental price predictions

# Overview
This is a Flask app for the rental price prediction in Honolulu, the capital
of Hawaii. The dataset for this project was scraped in 2021 using 
Beautiful Soup. The dataset contains 3120 inputs. The final model (Random forest, R2=0.65) was selected after
the comparison of 7 well known machine learning models.
# Motivation
I created this project for myself once I was planning to work
in Hawaii. This project would also be  usefull for rental and
real estate companies, whose job is to deeply understand the factors
affecting the rental price in that USA region. Anybody who is looking for
an apartment of a flat to rent in Honolulu may use it as well.

![image](https://user-images.githubusercontent.com/71885827/187156074-2bc93eb0-dc2f-4d78-8e74-e0af7e736167.png)
## Demo

Honolulu apartments rental price prediction

https://honolulu-app.herokuapp.com/
![image](https://user-images.githubusercontent.com/71885827/187153796-ffd87c31-762a-4dfd-9aa2-3a40d94c3415.png)
## Run Locally


Go to the project directory

```bash
  run app.py
```


## Authors

- [@Valery Liamtsau](https://www.linkedin.com/in/valery-liamtsau/)


## Acknowledgements

 - [University of Hawaii at Manoa](https://manoa.hawaii.edu/)


## Deployment

https://honolulu-app.herokuapp.com/



## Lessons Learned

1. Some interesting behavior during feature selection using
variance inflation factor (VIF) was observed: we should not solely rely on 
the VIF selection algorithms, instead we should combine the domain knowledge
to help VIF select meaningful features.

2. Tree based models are difficult to explain, but they 
generally give the best 
results

3. The less features (2-7) are in regression model, the better it behave in a long run



## Tech Used

**Flask**, **Beautiful Soup**


## Feedback

If you have any feedback, please reach out to us at 
valery.liamtsau@aol.com

