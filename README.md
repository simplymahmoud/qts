# qts
Here is the scenario we’d like to test.
•	All necessary components (mentioned below) are setup and running properly.
•	There is a QTS system. It reads XML files which are put to the folder. As soon as file is read and processed (i.e. consumed) file gets deleted. File should be consumed within 60 seconds. 
•	When file is consumed QTS starts the process called ‘consumer’ in Workflow Engine. Process typically runs for 10-60 seconds. It should not take longer than 180 seconds. 
•	The result of the process is published to Media Manager component. If the data is published to Media Manager the scenario is assumed successful.
