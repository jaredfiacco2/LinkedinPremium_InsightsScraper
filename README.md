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
<div class='tableauPlaceholder' id='viz1646111866122' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ScrapedLinkedinPremuimData&#47;ExecutiveSummary' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1646111866122');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1700px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
<img src="images\tableau.gif" alt="use tableau for visualization" />

<!-- CONTACT -->
## Contact

[Jared Fiacco](https://www.linkedin.com/in/jaredfiacco/) - jaredfiacco2@gmail.com

A GCP Data Engineering Project of Mine: [Publish Computer Statistics to Pub/Sub, Use Cloud Functions to Store in BigQuery](https://github.com/jaredfiacco2/ComputerMonitoring_IOT)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jaredfiacco/