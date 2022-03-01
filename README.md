<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jaredfiacco2/LinkedinPremium_InsightsScraper">
    <img src="images/Linkedin-Logo.png" alt="Logo" width="150" height="80">
  </a>

  <h3 align="center">Automatically log into Linkedin, Scrape insights data, Store it locally, and Visualize with Jupyter Notebook and Tableau.</h3>

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites & Instructions</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

- This code uses python and selenium to log into a Linkedin Premium Account, loop through a list of companies, and harvest the hidden table data from the HTML. 
- I then used pandas to store the data in .pkl files. 
- Finaly, I created data visualizations using Pandas and MatplotLib in Jupyter Notebook as well as Tableau.  

<img src="images\ProcessMap.png" alt="Process Map"/>

### Built With

* [Python](https://python.org)
* [Selenium](https://www.selenium.dev/)
* [MatplotLib](https://matplotlib.org/)
* [Pandas](https://pandas.pydata.org/)
* [Tableau](https://public.tableau.com/app/profile/jared.fiacco/viz/ScrapedLinkedinPremuimData/ExecutiveSummary)

### Prerequisites & Instructions

1. Installing all Required Packages
  ```sh
  pip install -r requirements.txt
  ```

2. Use Python to run 'main.py'. This will log into Linkedin, loop through a list of companies, and scrape the data from hidden tables, saving it to pickle files for future visualizations.
<img src="images\linkedin.gif" alt="linkedin premium data that gets scraped" /> 

3. Use Jupyter Notebook to manipulate the dat frames and create visualizations in matplotlib.
<img src="images\jupyternotebook.gif" alt="jupyter notebook for dataframe manipulations and visualizations" />

4. Use Tableau to visualize the data.
<img src="images\tableau.gif" alt="use tableau for visualization" />

<!-- CONTACT -->
## Contact

[Jared Fiacco](https://www.linkedin.com/in/jaredfiacco/) - jaredfiacco2@gmail.com

A GCP Data Engineering Project of Mine: [Publish Computer Statistics to Pub/Sub, Use Cloud Functions to Store in BigQuery](https://github.com/jaredfiacco2/ComputerMonitoring_IOT)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaredfiacco/