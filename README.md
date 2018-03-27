# This is an IOT Demo App

This app is to be a starter to get other SE's up and running with the Salesforce IOT Demo using the following hardware;

1. Raspberry Pi Zero
2. Pimoroni Enviro Phat

## Hardware

This demo is built on the following hardware, it will probably work on others. 

* Raspbery Pi Model 3b and Raspberry Pi Zero (recommend the zero for form factor reasons)
* Pimoroni [Enviro PHAT](https://shop.pimoroni.com/products/enviro-phat) 

## Prerequisites

This assumes you've done the following already. 

1. Soldered on you PHat - instructions on soldering stuff can be found [here](https://learn.pimoroni.com/tutorial/sandyj/soldering-phats) if you need them. 
2. Installed Raspbian on your Pi Zero - [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). As another helpful hint, [this blog](https://www.desertbot.io/blog/ssh-into-pi-zero-over-usb) helped me connect to the pi over usb.
3. Installed node and setup your enviro phat.
  * Install node from CLI for pi [instructions](https://github.com/sdesalas/node-pi-zero)
  * Setup the Phat [instructions](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat)

## Build the iotDemo

Clone the git repo
```
git clone https://github.com/adamSellers/iotDemo.git
```

Install the dependencies
```
cd iotDemo && npm install
```

### Important - stuff you need to do!
You can get this to work directly with a Salesforce Org by installing [this package](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t7F000004DE7P).

Once installed, do the following from within the iotDemo folder. 

Create a .env file. 
````
touch .env
````
Open the .env file and add some vars
````
nano .env
````
Enter the following config vars: 
````
* SF_USER={enter your username}
* SF_PASS={enter your password}
````

Once setup, run all the things.
````
node app.js
````