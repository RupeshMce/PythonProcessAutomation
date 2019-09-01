# PythonProcessAutomation


Hi,

  I developed this tools to imitate human interaction with machines. There are many tools in real world to do the same , but it an opensource and it is not OS dependent. It will run in any OS which supports Python.


  It is a **lightweight** and customizable tool ,so you can use it in any kind of lower-end machines to high-end GPU's. 

 ## Follow the steps for installation,
	1. Confirm that your machine has python3 and its corresponding pip version.
	2. Clone the **Git repository**
	3. I have attached all the dependencies in requirements.txt file which has a set of python packages with its version.
	4. Install using **pip install -r requirements.txt**.
  
  
## What It has:
  It has two files **train.py** and **execute.py** . Here, train is used to read/record the human interaction with machine     whereas excute is used to imitate/reproduce the human interaction. The interactions are saved in a file foramt called         *pickle*.

## Training Part:
  Before running the training part the filename need to be specified in order to save the actions in the same name.
  ```python train.py -n scrapInfo.pickle``` 
  Once the script start run. Do all the actions need to be done *but the exceptional case is ESC key is not allowed to use*     because only the ESC is pressed the training part will get terminated. In case you need to use ESC as key replace the ESC     with some other key, to avoid this issue .

## Execution Part:
  You need to specify the which file need to execute.
  ```python execute.py -e scrapInfo.pickle```
  
 Here, I have developed this tools which can support all kinds of keyboard combinations which we generally used in real time. In case if you need to customize it you can do.
 
 
 
  

 
