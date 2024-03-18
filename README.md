**# Vashisht-Hackathon-VH119**
This repository contains solutions for 2 problem statements which we solved during the vashisht hackathon event. Team number - VH119


**Team Details: **
TEAM NUMBER - VH119 
1. MADESHWARAN C (made22081.cs@rmkec.ac.in)
2. LAKSHMANAN V (laks22077.cs@rmkec.ac.in)
3. JAGDISH E (jagd22048.cs@rmkec.ac.in)
4. KAILASH NARAYAN KIRADU A (kail22057.cs@rmkec.ac.in)


**Project 1**


**Title: TENDER ALLOCATION USING BLOCKCHAIN TECHNOLOGY**


**Description:**
Misconduct in some governance procedures, such as government tenders, includes info leaks, corruption, bribery, and so on. The majority of present electronic services and IT infrastructure have restrictions. So we introduce a permissioned block chain network can provide the transparency required to efficiently implement government regulations for the benefit of the country's population while also establishing obligations in the event of system misuse.


**The problem it solves:**
Misconduct in governance procedures, particularly in areas such as government tenders, can encompass various unethical or illegal activities. For example - Information leaks, corruption, bribery, conflict of interest, bid rigging, kickbacks, etc.,

These forms of misconduct not only undermine the principles of transparency, fairness, and accountability but also result in wastage of public funds, substandard service delivery, and erosion of public trust in government institutions. Effective measures such as robust anti-corruption policies, transparent procurement processes, and independent oversight are essential to combatting such misconduct and promoting good governance.


**Use cases**:

![UseCase](https://github.com/kailashkiradu/Vashisht-Hackathon-VH119/assets/119476446/4f448f60-4390-4bca-be6c-0df48305f913)


**Demo video link** - https://youtu.be/u6uK-asgKOc?si=FAM7--zDozCP_1b0

**Images** - https://docs.google.com/document/d/12k2DY0eMKzxSPxEbCDziiKsh1xwZz-UA 


**How to test the project: **
1. Download the zip file
2. extract the zip file 
3. open the java enterprise edition latest and download the tomcat server
4. open the folder section and import the directory of the source file
5. then run index.jsp file


**Technologies used:**
1. frontend : html,css,js
2. Database : mysql db
3. backend : java,jsp,xml 
4. server : Apache tomcat server

**Architecture diagram:** https://docs.google.com/document/d/1FFmCI4vHPubOYdSrr53UH44B9GKrMpbC/edit?usp=sharing&ouid=111630910294398996697&rtpof=true&sd=true






**Project 2**

**Title: Machine Learning-Based Classification and Quantification of Deficiencies in Leaves**


**Description:**
In our work to determine leaf nutrition deficiency , we used K-means algorithm to accurately classify and quantify leaf nutrient shortages in agriculture. The foundation of our work is a broad data set of high-resolution leaf pictures with different nutrient deficits. Effective classification is made possible by identifying different sorts of deficiencies based on visual patterns that are retrieved from the photos and combined with the K-means clustering technique.

**The problem it solves:**
The project addresses the challenge of labor-intensive and subjective methods for detecting nutrient deficiencies in plants by proposing an automated approach. By integrating techniques from image processing, machine learning, and clustering algorithms, it offers a scalable solution for efficient crop management.

**Existing Methodology:**
•	The existing methodology primarily relies on CNN models trained on specific species of plant leaves.
•	It involves data acquisition, pre-processing, CNN model construction, and output evaluation.
•	Challenges include limited applicability to various plant species and the need for human intervention in certain tasks.
•	Technologies used: CNN models, image processing, data augmentation.Proposed Methodology:

**PROPOSED METHODOLOGY:**
Method 1: K-Means with Manual Clustering: Segmentation of leaf images into color clusters using K-Means, followed by manual mapping to nutrient deficiencies.
Method 2: K-Means with Auto Clustering: Utilizes K-Means with automated mapping to streamline nutrient deficiency detection.
Both methods aim to detect and quantify nutrient deficiencies based on color variations in leaf images.



**Use cases:**
1.	Agricultural Monitoring: Farmers can utilize the system to monitor nutrient deficiencies in crops, enabling timely interventions to improve crop health and yield.
2.	Research: Plant scientists and agronomists can employ the tool for studying nutrient deficiencies in different plant species, facilitating research in crop improvement and sustainable agriculture.
3.	Disease Management: The system helps differentiate between nutritional imbalances and disease infections, aiding in effective disease management strategies.

**Challenges encountered:**
1.	Data Acquisition: Obtaining diverse and labeled datasets of leaf images depicting nutrient deficiencies posed a challenge due to variability in plant species and environmental conditions.
2.	Clustering Optimization: Determining the optimal number of clusters (k) in the K-Means algorithm required iterative experimentation and validation to achieve accurate segmentation.
3.	Algorithm Selection: Evaluating the performance of various clustering algorithms and their suitability for nutrient deficiency detection in plant leaves required extensive analysis and comparison.
   

**PPT** - https://docs.google.com/presentation/d/1xq8RlhESvJdd_ndRtf3RlNTKk3amyEz0/edit?usp=sharing&ouid=111630910294398996697&rtpof=true&sd=true


**Demo video link** - https://youtu.be/ubXPvHBi5nw?si=5alsoEXXLZ6pU7L2

**Images** - https://docs.google.com/document/d/14RDMDkAcm6u02nTb9PHZDSw608t6wzG_/edit?usp=sharing&ouid=111630910294398996697&rtpof=true&sd=true


**How to test the project:** 
Method 1
1.	open google colab : https://colab.research.google.com/drive/15pNmUAK7_oNRJGbSz2vwTQ5240brsWZS 
2.	click on “copy to drive“
3.	download dataset : https://drive.google.com/drive/folders/128wQZEWcSHynUeIAh_OfL0IqKE6cWsOz 
4.	run : 
	from google.colab import drive
	drive.mount('/content/drive')
	
5.	upload the dataset to your google drive 
6.	chang image path : image_path = "/content/drive/MyDrive/photo/Phosphorus1.png"  dataset image path(from your google drive)
7.	run the program

Method 2 
1.	download the project file from our repo
2.	open the python file in your favourite IDE
3.	install `matplotlib `, `OpenCV` and `scikit-learn` using the command
	pip install matplotlib
	pip install opencv-python
	pip install scikit-learn
4.	download dataset : https://drive.google.com/drive/folders/128wQZEWcSHynUeIAh_OfL0IqKE6cWsOz 
5.	chang image path : image_path = "/content/drive/MyDrive/photo/Phosphorus1.png"  dataset image path(from your computer)
6.	run the program 




**Technologies used:**
1. Python
2. OpenCV
3. NumPy
4. Scikit-learn
5. Matplotlib
6. Jupyter notebook/Google colab



**FlowChart:** https://docs.google.com/document/d/1o60lKa6WklGkOjJOggef4QGXUSawPwWl/edit?usp=sharing&ouid=111630910294398996697&rtpof=true&sd=true
