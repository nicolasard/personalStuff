To start working with docker try by installing docker for windows. I have windows 10 core in my personal laptop so I had to follow this non-official guide to install it https://itnext.io/install-docker-on-windows-10-home-d8e621997c1d 

## To create a new image 

You should have a Dockerfile in your folder and run something like this.

```docker build```

## To run a container with docker-compose

This is better explained at https://docs.docker.com/compose/reference/overview/

Create a docker-compose.yml file.

Run the command ```docker-compose up``` (this will read a file named docker-compose.yml from the dir where you run the command). Additionally you can select your custom .yml file name with ```docker-compose -f custon-name.yml up```

## To run a container with an image and debug doing ssh 

This command is really usefull when you want to start an image and do SSH inside and check the stuff you have there.  ```docker run -it --entrypoint=/bin/bash <image-id>```
