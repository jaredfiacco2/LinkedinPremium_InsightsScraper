from os import link
from statistics import median
import pandas as pd
from time import sleep
from datetime import datetime, timezone

def login(driver, email, password):
    driver.get('https://www.linkedin.com/')
    #Login username/password
    email_box = driver.find_element_by_id('session_key')
    email_box.send_keys(email)
    pass_box = driver.find_element_by_id('session_password')
    pass_box.send_keys(password)
    submit_button = driver.find_element_by_class_name('sign-in-form__submit-button')
    submit_button.click()

def healthcare_companies():
    df = pd.read_csv("data/companies_list.csv")
    df = df.query('`Sector` == "Healthcare"')
    sector = df['Sector']
    companynames = df['CompanyName']
    companynames_lnk = df['LinkedinCompanyName']
    links = df['InsightsLink']
    return sector, companynames, companynames_lnk, links

def top_companies():
    df = pd.read_csv("data/companies_list.csv")
    df = df.query('`Sector` != "Healthcare"').reset_index()
    sector = df['Sector']
    companynames = df['CompanyName']
    companynames_lnk = df['LinkedinCompanyName']
    links = df['InsightsLink']
    return sector, companynames, companynames_lnk, links

def upsert_emp_head_count(driver, sector, companynames, companynames_lnk, links):
    print('starting function')
    original_df  = pd.read_pickle('data/emp_head_count.pkl')
    original_mt_df  = pd.read_pickle('data/med_tenure.pkl')
    print('starting link for loop')
    print(links)
    for l in range(len(links)):
        print(l)
        print(links[l])
        # print(companies.at[c, 'LinkedinCompanyName'])
        # print('https://www.linkedin.com/company/'+companies.at[c, 'LinkedinCompanyName']+'/insights/')
        driver.get(links[l])
        sleep(5)
        #Employee Count Over Time
        # dts_utc = []
        # dts_loc = []
        # dts_loc_nm = []
        date=[]
        month = []
        year = []
        emp=[]
        idx = []
        employee_count_emp = driver.find_elements_by_xpath("//*[@headers='org-insight-headcount__a11y-num-employees']")
        employee_count_date = driver.find_elements_by_xpath("//*[@headers='org-insight-headcount__a11y-date']")
        for i in range(len(employee_count_emp)-1):
            emp.append(int(employee_count_emp[i].get_attribute('textContent').strip()))
            date_str = employee_count_date[i].get_attribute('textContent').strip()
            month_str_len=len(date_str)-5
            # print(s[:j])
            date.append(date_str)
            month.append(date_str[:month_str_len])
            year.append(date_str[-4:])
            idx.append(companynames_lnk[l]+'_'+date_str)
        # 
        df = pd.DataFrame()
        df['month'] = month
        df['year'] = year
        df['date'] = date
        df['emp'] = emp
        df.index = idx
        df['create_dts_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local_type'] = str(datetime.now().astimezone().tzinfo)
        df['sector'] = sector[l]
        df['company_name'] = companynames[l]
        df['linkedin_company_name'] = companynames_lnk[l]
        df['insights_link'] = links[l]
        original_df = original_df.combine_first(df)
        # original_mt
        mt = []
        mt_df = pd.DataFrame()
        median_tenure = driver.find_elements_by_xpath("//*[@class='org-insights-module__facts']")
        print(median_tenure)
        if len(median_tenure) > 0:
            mt.append(median_tenure[0].get_attribute('textContent').strip().replace('Median tenure', ''))
            mt_df['median_tenure'] = mt
            mt_df['create_dts_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            mt_df['create_dts_local'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            mt_df['create_dts_local_type'] = str(datetime.now().astimezone().tzinfo)
            mt_df['sector'] = sector[l]
            mt_df['company_name'] = companynames[l]
            mt_df['linkedin_company_name'] = companynames_lnk[l]
            mt_df['idx'] = companynames_lnk[l]
            mt_df['insights_link'] = links[l]
            mt_df = mt_df.set_index('idx')
            print(mt_df)
            original_mt_df = original_mt_df.combine_first(mt_df)
            print(original_mt_df)
        print(mt)
    original_df.to_pickle('data/emp_head_count.pkl')
    original_mt_df.to_pickle('data/med_tenure.pkl')

def update_employee_func_growth(driver, sector, companynames, companynames_lnk, links):
    original_df = pd.read_pickle('data/emp_func_growth.pkl')
    #original_df = pd.DataFrame(columns=original_df.columns)
    for l in range(len(links)):
        print(links[l])
        driver.get(links[l])
        sleep(5)
        emp=[]
        func = []
        perc=[]
        perc_6 = []
        perc_6_txt = []
        perc_12 = []
        perc_12_txt = []
        idx = []
        employee_func_growth_func = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-functions-function']")
        employee_func_growth_emp = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-functions-num-employees']")
        employee_func_growth_perc = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-functions-percentage']")
        employee_func_growth_perc_6 = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-functions-6']")
        employee_func_growth_perc_12 = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-functions-12']")
        for i in range(len(employee_func_growth_func)-1):
            emp.append(int(employee_func_growth_emp[i].get_attribute('textContent').strip()))
            func.append(employee_func_growth_func[i].get_attribute('textContent').strip())
            perc.append(employee_func_growth_perc[i].get_attribute('textContent').strip())
            perc_6.append(str(employee_func_growth_perc_6[i].get_attribute('textContent').strip()).split('\n')[0].strip())
            perc_6_txt.append(str(employee_func_growth_perc_6[i].get_attribute('textContent').strip()).split('\n')[1].strip())
            perc_12.append(str(employee_func_growth_perc_12[i].get_attribute('textContent').strip()).split('\n')[0].strip())
            perc_12_txt.append(str(employee_func_growth_perc_12[i].get_attribute('textContent').strip()).split('\n')[1].strip())
            idx.append(companynames_lnk[l]+'_'+employee_func_growth_func[i].get_attribute('textContent').strip())
        # 
        df = pd.DataFrame()
        df['employe_count'] = emp
        df['function'] = func
        df['function_percent_of_total'] = perc
        df['percent_func_growth_last6mo'] = perc_6
        df['percent_func_growth_last6mo_txt'] = perc_6_txt
        df['percent_func_growth_last12mo'] = perc_12
        df['percent_func_growth_last12mo_txt'] = perc_12_txt
        df.index = idx
        df['create_dts_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local_type'] = str(datetime.now().astimezone().tzinfo)
        df['sector'] = sector[l]
        df['company_name'] = companynames[l]
        df['linkedin_company_name'] = companynames_lnk[l]
        df['insights_link'] = links[l]
        original_df = original_df.combine_first(df)
    print(original_df)
    original_df.to_pickle('data/emp_func_growth.pkl')

def update_total_job_openings(driver, sector, companynames, companynames_lnk, links):
    original_df = pd.read_pickle('data/total_job_openings.pkl')
    #original_df = pd.DataFrame(columns=original_df.columns)
    for l in range(len(links)):
        print(links[l])
        driver.get(links[l])
        sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        emp=[]
        func = []
        perc=[]
        perc_3 = []
        perc_3_txt = []
        perc_6 = []
        perc_6_txt = []
        perc_12 = []
        perc_12_txt = []
        idx = []
        total_job_openings_func = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-function']")
        total_job_openings_emp = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-num-employees']")
        total_job_openings_perc = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-percentage']")
        total_job_openings_perc_3 = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-3']")
        total_job_openings_perc_6 = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-6']")
        total_job_openings_perc_12 = driver.find_elements_by_xpath("//*[@headers='org-function-growth-table__a11y-jobs-12']")
        for i in range(len(total_job_openings_func)-1):
            emp.append(int(total_job_openings_emp[i].get_attribute('textContent').strip()))
            func.append(total_job_openings_func[i].get_attribute('textContent').strip())
            perc.append(total_job_openings_perc[i].get_attribute('textContent').strip())
            perc_3.append(str(total_job_openings_perc_3[i].get_attribute('textContent').strip()).split('\n')[0].strip())
            perc_3_txt.append(str(total_job_openings_perc_3[i].get_attribute('textContent').strip()).split('\n')[1].strip())
            perc_6.append(str(total_job_openings_perc_6[i].get_attribute('textContent').strip()).split('\n')[0].strip())
            perc_6_txt.append(str(total_job_openings_perc_6[i].get_attribute('textContent').strip()).split('\n')[1].strip())
            perc_12.append(str(total_job_openings_perc_12[i].get_attribute('textContent').strip()).split('\n')[0].strip())
            perc_12_txt.append(str(total_job_openings_perc_12[i].get_attribute('textContent').strip()).split('\n')[1].strip())
            idx.append(companynames_lnk[l]+'_'+total_job_openings_func[i].get_attribute('textContent').strip())
        # 
        df = pd.DataFrame()
        df['employee_count'] = emp
        df['function'] = func
        df['function_percent_of_total'] = perc
        df['percent_func_growth_last3mo'] = perc_3
        df['percent_func_growth_last3mo_txt'] = perc_3_txt
        df['percent_func_growth_last6mo'] = perc_6
        df['percent_func_growth_last6mo_txt'] = perc_6_txt
        df['percent_func_growth_last12mo'] = perc_12
        df['percent_func_growth_last12mo_txt'] = perc_12_txt
        df.index = idx
        df['create_dts_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local_type'] = str(datetime.now().astimezone().tzinfo)
        df['sector'] = sector[l]
        df['company_name'] = companynames[l]
        df['linkedin_company_name'] = companynames_lnk[l]
        df['insights_link'] = links[l]
        print(df)
        original_df = original_df.combine_first(df)
    print(original_df)
    original_df.to_pickle('data/total_job_openings.pkl')

def upsert_new_hires(driver, sector, companynames, companynames_lnk, links):
    original_df  = pd.read_pickle('data/new_hires.pkl')
    for l in range(len(links)):
        print(links[l])
        # print(companies.at[c, 'LinkedinCompanyName'])
        # print('https://www.linkedin.com/company/'+companies.at[c, 'LinkedinCompanyName']+'/insights/')
        driver.get(links[l])
        sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(3)
        #Employee Count Over Time
        # dts_utc = []
        # dts_loc = []
        # dts_loc_nm = []
        date=[]
        month = []
        year = []
        sr_emp=[]
        oth_emp=[]
        idx = []
        new_hires_sr_emp = driver.find_elements_by_xpath('//*[@headers="org-insights-newhires-module__a11y-senior-hires"]')
        # new_hires_sr_emp = driver.find_elements_by_xpath("")
        # print(new_hires_sr_emp)
        new_hires_oth_emp = driver.find_elements_by_xpath('//*[@headers="org-insights-newhires-module__a11y-other-hires"]')
        new_hires_date = driver.find_elements_by_xpath('//*[@headers="org-insights-newhires-module__a11y-date"]')
        for i in range(len(new_hires_oth_emp)-1):
            sr_emp.append(int(new_hires_sr_emp[i].get_attribute('textContent').strip()))
            print(int(new_hires_sr_emp[i].get_attribute('textContent').strip()))
            oth_emp.append(int(new_hires_oth_emp[i].get_attribute('textContent').strip()))
            print(int(new_hires_oth_emp[i].get_attribute('textContent').strip()))
            date_str = new_hires_date[i].get_attribute('textContent').strip()
            month_str_len=len(date_str)-5
            # print(s[:j])
            date.append(date_str)
            month.append(date_str[:month_str_len])
            year.append(date_str[-4:])
            idx.append(companynames_lnk[l]+'_'+date_str)
        # 
        df = pd.DataFrame()
        df['month'] = month
        df['year'] = year
        df['date'] = date
        df['senior_employees'] = sr_emp
        df['other_employees'] = oth_emp
        df.index = idx
        df['create_dts_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['create_dts_local_type'] = str(datetime.now().astimezone().tzinfo)
        df['sector'] = sector[l]
        df['company_name'] = companynames[l]
        df['linkedin_company_name'] = companynames_lnk[l]
        df['insights_link'] = links[l]
        print(df)
        original_df = original_df.combine_first(df)
    print(original_df)
    original_df.to_pickle('data/new_hires.pkl')
