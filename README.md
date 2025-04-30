# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
  
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- We opine that mildew-infected cherry leaves have clear signs of fungus infection, characterized typically by discolouration and white powedry spots all over the leaf, that differentiate them from a healthy cherry leaf.
  
- An Image Montage shows that typically a mildew-infected cherry leaf is mostly discoloured and has white powdery patches across it. Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

Extensive consultations with the client and stakeholders culminated in 2 business requirements:

1. #### Business Requirement 
- "Conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew." 
  
  The rationale to map this business requirement to the Data Visualisations and ML tasks is predicated on the need to create a human-interpretable, and visual proof of differences between healthy and mildew-infected leaves. This would help field workers recognize symtoms manually without ML tools.

2. #### Business Requirement
- "Predicting if a cherry tree is healthy or contains powdery mildew."
  
  The rationale to map this business requirement to the Data Visualisations and ML tasks harps on the goal to automate classificaton for scalability. This would save labor cost as against manual inspection and would also help to reduce economic losses since early detection prevents crop spread.

## ML Business Case

1. #### Business Case Title:
   - Automated Powdery Mildew Detection to Save Cherry Crop Yields
  
2. #### Business Objective:
   - Avoid supplying the market with a product of compromised quality. 

3. #### ML Task translation of Business Case:
   - A binary classification model to distinguish healthy leaves from infected ones, paired with visual explainability tools.

4. #### Data Availability:
   - Existing dataset of 4,208 labeled cherry leaf images (healthy vs. infected).
  
5. #### Technical and Non-Technical Success Metrics:
   - Develop a model to classify leaves with 97%+ accuracy.
   - Prototype the model on a Streamlit dashboard.

6. #### Risks and Constraints:
   - Risk: Model bias due to limited data. Mitigation: Augment dataset with synthetic samples.
   - Constraint: Data provided under an NDA (non-disclosure agreement): Mitigation: Data anonymization.

7. #### ML Suitability:
   - Conventional data analysis can be used to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

## Dashboard Design

1. ### Quick Project Summary App Screenshot
   
![Quick Project Summary Screenshot](docs/images/Capture.PNG1.PNG)
    - 

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
