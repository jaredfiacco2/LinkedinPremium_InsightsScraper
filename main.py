from os import link
from selenium import webdriver
from linkedin_tools import login, healthcare_companies, top_companies, upsert_emp_head_count, update_employee_func_growth, upsert_new_hires, update_total_job_openings

# Open Linkedin in Chrome using the chromedriver.exe webdriver
driver = webdriver.Chrome()
driver.get('https://linkedin.com')

# Get info from company_lists.csv
#sector, companynames, companynames_lnk, links = healthcare_companies()
sector, companynames, companynames_lnk, links = top_companies()
print(companynames)
print(sector)
print(companynames_lnk)
print(links)

# Login to linkedin premium using your credentials
email='YOUR_LINKEDIN_PREMIUM_EMAIL_ADDRESS'
password='YOUR_LINKEDIN_PREMIUM_PASSWORD'
login(driver, email, password)

# Loop through company list and pull "HeadCount", "Median Tenure", "Functional Growth", "Total Job Openings", "New Hire" data 
upsert_emp_head_count(driver, sector, companynames, companynames_lnk, links)
update_employee_func_growth(driver, sector, companynames, companynames_lnk, links)
update_total_job_openings(driver, sector, companynames, companynames_lnk, links)
upsert_new_hires(driver, sector, companynames, companynames_lnk, links)
print("Done!")
