# MLOPs
This project is an MLOPs assignment that has a basic ML model that predicts the brain weight for a given head size using Linear regression.
It takes the head size as the feature (x) and the brain weight as the label(Y).
This is a basic flask application that exposes the ML model to a port. The flask server takes the head size JSON input and returns brain weight JSON.

#### Format for input JSON   
<code>{"number": anyNumber} 
</code>
where any number is a positive number

Response:  <code>{"prediction":output}</code>

## Docker Containerization
Step 1. In the same folder as the app.py, make a file named "dockerfile".<br><br>
Step 2. This dockerfile is uploaded to the repository.<br><br>
Step 3. The dockerfile is set up to expose port number 5000 and also run on Python 3.9, install all the requirements in the image and finally run the flask server using gunicorn.<br><br>
Step 4. Now within the folder, We build the image using the command docker -t build imageName.<br><br>
Step 5. With that, we finish building our docker image.<br><br>
Step 6. We pushed our image to the docker hub using docker Desktop. To do this we simply tag our image with the appropriate name and then push it to the docker repository.<br><br>

That is how we built our docker image with the machine-learning model. To look at the output, we can run the image on any container of our choice.<br><br>


### Cloud Deployment
The docker image was pushed to Google Cloud's artifact Registry and then we deployed the image using GKE(Google Kubernetes Engine).<br><br>
To do this we used the GCP CLI to authorize our docker to push images to asia-south1.gcr.io.<br><br>
Next we tagged our docker image with the following command <br><br>
<code>docker tag devops/devops asia-south1.gcr.io/mlops-401117/devops</code><br>
where devops/devops was the local image name and the next one was the GCP image name.<br>

This would push the image to google cloud artifact registry.<br>
Next we create a new kubernetes cluster and then deploy this image by selecting it in the artifact registry.<br>
Finally in the options for the cluster. We choose to expose the image's port number 5000 i.e the port where flask is running. This way we have our ML api ready and deployed.<br><br>

### Automated Testing
To implement a continuous integration pipeline, we decided to choose the travis CI for its easy to use tool and since our project is a very small scale.<br><br>
To do this, we first created some unit tests in a python file called test.py and pushed it to the git repo.<br>
We then simply added a .travis.yml file to the repo which is a CI configuration/instruction file.<br>
We set it up to run python 3.9, then install all our requirements and then to run the test.py file.<br><br>

On the travis CI website, we linked our git repo and added the travis CI user. We then proceeded to push the file on which travis which listened to the repo, with python 3.9 ran 2 unit tests.
<br><br><br>
The test logs from travis:
<code>Downloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/16.04/x86_64/python-3.9.tar.bz2
0.36s$ curl -sSf --retry 5 -o python-3.9.tar.bz2 ${archive_url}
10.98s$ sudo tar xjf python-3.9.tar.bz2 --directory /
0.00s
git.checkout
0.00s0.53s$ git clone --depth=50 --branch=master https://github.com/MKoushikYadav/MLOps.git MKoushikYadav/MLOps
0.01s0.00s$ source ~/virtualenv/python3.9/bin/activate
$ python --version
Python 3.9.6
$ pip --version
pip 22.2.2 from /home/travis/virtualenv/python3.9.6/lib/python3.9/site-packages/pip (python 3.9)
install
13.74s$ pip install -r requirements.txt
1.00s$ python test.py
<WrapperTestResponse streamed [200 OK]>
.<WrapperTestResponse streamed [200 OK]>
.
----------------------------------------------------------------------
Ran 2 tests in 0.010s
OK
The command "python test.py" exited with 0.
Done. Your build exited with 0.</code>

###