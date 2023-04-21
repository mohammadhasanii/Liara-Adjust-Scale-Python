
# Liara-Adjust-Scale-Python

This service is an automatic scaler for Liara's cloud infrastructure and does not require anything to run. It provides the ability to automatically check the app scale every few seconds and zoom in or out.



![Logo](https://middleware.io/static/79f5bb408800e7b54c2269add486c153/12bf8/auto-scale-2.jpg)


## How to work ?


```
1-First of all, make sure that Python is installed on your system

2-To connect to the program, you must receive your token from Liara

3- After receiving the token from Liara, change the token in the token variable in the main.py file

4-Your application conainer runs once every 1000 seconds and the scale of the program changes automatically

5-If the program needs to increase the resources, the scale will be bigger, otherwise, if it needs to reduce the resources, the scale of the program will be as small as possible.
```
[Get Token Api](https://console.liara.ir/API)



## Running Application

To run tests, run the following command

```bash
  python main.py 
```


## Run the container on Liara

[Deploy docker documentation](https://docs.liara.ir/app-deploy/docker/getting-started)

