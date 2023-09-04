## Table of contents

1. [How to Create Endpoints Using `FastAPI`?](#1-how-to-create-endpoints-using-fastapi)
2. [How to Create Docker Container Locally?](#2-how-to-create-docker-container-locally)
3. [How to Deploy Docker Container to GCP?](#3-how-to-deploy-docker-container-to-gcp)
4. [Description of the Dockerfile](#4-description-of-the-dockerfile)
5. [Most Important `docker` commands](#5-most-important-docker-commands)

NOTE: [this tutorial](https://towardsdatascience.com/how-to-deploy-and-test-your-models-using-fastapi-and-google-cloud-run-82981a44c4fe)
has helped me to write this readme file.

## 1. How to Create Endpoints Using `FastAPI`?

Have a look at the file `main.py`. The file
contains the following code:

```python
from fastapi import FastAPI

app = FastAPI()
...
@app.get("/")
async def root():
    return {"message": "Hello World from root!"}
```
That's how you create the root endpoint.

Other possibilities inside `FastAPI` are [explained here](https://fastapi.tiangolo.com/).
These are:
1. Query parameters - cf. function `my_query_paramater` inside `main.py`
2. Path parameters - cf. function `my_path_paramater` inside `main.py`



## 2. How to Create Docker Container Locally?

### 2.1. Create the Container Locally
If you are working on Mac platform, make sure that `Dockerfile`
has the following line:
```dockerfile
FROM --platform=linux/arm64 python:3.11-slim
```

Alternatively, if you are using Linux platform, the first line 
of the `Dockerfile` should be:
```dockerfile
FROM --platform=linux/amd64 python:3.11-slim
```

Now, navigate to the `fastapi_gcp_app` directory in the CLI.

In order to create the Docker image run the command:
```commandline
docker build -t my_image .
```

After the command completes make sure that the image 
``myimage`` is listed in the output of the command:

```commandline
docker image ls -a
```

Now that the Docker image `myimage` exists, create the 
container using the command:

```commandline
docker run -d --name mycontainer -p 80:80 myimage
```
Let's break down the command:
1. `docker run` - run the container
2. `-d` - run the container in the background
3. `-p 80:80` - map port 80 of the host to port 80 of the container
4. `--name mycontainer` - name the container `mycontainer`

### 2.2. Test the Local Container
The testing of the local container can be done using the script
`test_local_container.py`.

## 3. How to Deploy Docker Container to GCP?
`NOTE 1`: I am assuming that all the GCP APIs needed to deploy the app have already
been enabled on your account. If not, please enable them.

`NOTE 2`: remember that the docker should be configured if 
you are pushing an image for the first time on your platform.

`NOTE 3`: remember that the image you need to push 
to the GCP should be built on the Linux platform, i.e. 
that the `dockerfile` should start with the line:
```dockerfile
FROM --platform=linux/amd64 python:3.11-slim
```

First, create a new repository in GCP's `Artifact Registry`.
For the purpose of this tutorial I am assuming that this 
repository is calles `fastapi-tutorial-repo`. I create 
it in the location `europe-central2`.

Secondly, what you want to do is to push an image to the 
artifact repository. 
This can be done using the commands:

```commandline
docker tag IMAGE-NAME LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE-NAME
docker push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE-NAME
```

In our case:
* IMAGE-NAME is `myimage`
* LOCATION is `europe-central2`
* PROJECT-ID is name of the project (I'll keep it secret)
* REPOSITORY is `fastapi-tutorial-repo`

so that the commands become:
```commandline
docker tag myimage europe-central2-docker.pkg.dev/PROJECT-ID/fastapi-tutorial-repo/myimage
docker push europe-central2-docker.pkg.dev/PROJECT-ID/fastapi-tutorial-repo/myimage
```

`IMPORTANT NOTE`: if you are running the `push` command
for the first time on your platform remember to 
configure `docker` first by 
[running the command](https://stackoverflow.com/questions/75840164/permission-artifactregistry-repositories-uploadartifacts-denied-on-resource-usin):
```commandline
gcloud auth configure-docker europe-central2-docker.pkg.dev
```
 
The image `myimage` should be visible inside 
the repo 'fastapi-tutorial-repo' in the GCP console in the 
`Artifact Registry`.

Now we can move on to create a `Cloud Run` service.
This can be done using the UI.
Remember to select `Require authentication` in 
the `Authentication` section.

The `Cloud Run` service is created now.
Let's try to test the deployed service keeping in mind 
that **authentication is required**.



## 4. Description of the Dockerfile
The `Dockerfile` contains the following lines:
```dockerfile
```

## 5. Most Important `docker` commands
### 5.1. List All Images: 
```commandline
docker image ls -a
```

### 5.2. List All Containers:
```commandline
docker container ls -a
```

### 5.3. Create Image:
In order to create image from Dockerfile in the current directory 
using the
`--tag`/`-t` flag to pass your own image name
(`myimage` in this case)
```commandline
docker build -t my_image .
```

### 5.4. Create Container `mycontainer` 
In order to create a container from image `myimage` 
with port mapping and 
run it in the background and name it `mycontainer`
use the following command:
```commandline
docker run -d --name mycontainer -p 80:80 myimage
```
`IMPORTANT - PORTS MAPPING`: note that the port mapping is done
in the following way: `-p 80:80`. The first `80` is the port
of the host machine, the second `80` is the port of the container.
Furthermore, note that the `FastAPI` app port is defined
in the `Dockerfile` in the `CMD` command:
```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

### 5.5. Stop Running Container `mycontainer`
```commandline
docker container stop mycontainer
```

### 5.6. Stop Running Container `mycontainer`
```commandline
docker container rm mycontainer
```

### 5.7. Remove Stopped Container `mycontainer`
```commandline
docker container rm mycontainer
```

## 5.8. Remove All Stopped Containers
```commandline
docker container prune
```

## 5.9. Remove Image `myimage`
```commandline
docker image rm myimage
```
