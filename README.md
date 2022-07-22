# pingpong

Open the Projects Folder using Idea Intellij. 
Install gradle before running the code.
All the other depencies should be installed automatically as the project is modified. 

Instructions for Signature Generation and Validation can be found in the pdf document shared.

After the signatures are generated for the individual (Inside Standalone folder for the shared dataset) devices, the signatures were processed and buckets containing those signatures were created. 

Inside the Buckets and Defense folder those signature buckets and Python code for Individual devices defense mechanism can be found. The time delay added can be adjusted inside the python scripts. 

After the defense mechanism was successfull, the modified pcap files path needs to be given while running the signature validation code, which is inside te Projects folder.

