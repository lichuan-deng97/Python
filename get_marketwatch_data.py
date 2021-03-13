import api.web.get_html_content as awghc
import api.operation.get_url as aogu
import api.web.get_information_from_html as awgifh
import api.operation.remove_list_get_useful_list as aorlgul
import api.operation.save_file as aosf
import pandas as pd

url = aogu.url_link_marketwatch('A')
html = awghc.get_url_content(url)
item_all_list = awgifh.get_all_item_1(html,'table table--overflow align--right','div')

remove_list = ['Item','2014','2015','2016','2017','2018','2019','2020','2021','5-year trend',' ','']
all_useful_item_list = aorlgul.all_useful_item_list(item_all_list,remove_list)


all_item_list = ['Sales/Revenue','Sales Growth','Cost of Goods Sold (COGS) incl. D&A','COGS Growth','COGS excluding D&A',
                 'Depreciation & Amortization Expense','Depreciation','Amortization of Intangibles','Gross Income',
                 'Gross Income Growth','Gross Profit Margin','SG&A Expense','SGA Growth','Research & Development','Other SG&A',
                 'Other Operating Expense','Unusual Expense','EBIT after Unusual Expense','Non Operating Income/Expense',
                 'Non-Operating Interest Income','Equity in Affiliates (Pretax)','Interest Expense','Interest Expense Growth',
                 'Gross Interest Expense','Interest Capitalized','Pretax Income','Pretax Income Growth','Pretax Margin',
                 'Income Tax','Income Tax - Current Domestic','Income Tax - Current Foreign','Income Tax - Deferred Domestic',
                 'Income Tax - Deferred Foreign','Income Tax Credits','Equity in Affiliates','Other After Tax Income (Expense)',
                 'Consolidated Net Income','Minority Interest Expense','Net Income','Net Income Growth','Net Margin Growth',
                 'Extraordinaries & Discontinued Operations','Extra Items & Gain/Loss Sale Of Assets','Cumulative Effect - Accounting Chg',
                 'Discontinued Operations','Net Income After Extraordinaries','Preferred Dividends','Net Income Available to Common',
                 'EPS (Basic)','EPS (Basic) Growth','Basic Shares Outstanding','EPS (Diluted)','EPS (Diluted) Growth','Diluted Shares Outstanding',
                 'EBITDA','EBITDA Growth','EBITDA Margin','Total Investment Income','Sundry Revenue/Income','Trading Account Income',
                 'Trust Income, Commissions & Fees','Commission & Fee Income','Total Expense','Total Interest Expense',
                 'Depreciation & Amortization Expense','Other Operating Expense','Operating Income','Operating Income Growth',
                 'Non-Operating Income (Expense)','Non-Operating Interest Income','Miscellaneous Non Operating Expense',
                 'Equity in Affiliates (Pretax)','Unusual Expense','Pretax Income','Pretax Income Growth','Pretax Margin',
                 'Interest Income','Interest Income Growth','Interest and Fees on Loans','Interest Income on Fed. Funds',
                 'Interest Income on Fed. Repos','Interest on Bank Deposits','Other Interest or Dividend Income','Total Internest Expense',
                 'Total Internest Expense Growth','Interest Expense on Bank Deposits','Other Interest Expense','Interest Expense on Debt',
                 'Interest Capitalized','Other Borrowed Funds','Net Interest Income','Net Interest Income Growth','Loan Loss Provision',
                 'Loan Loss Provision Growth','Net Interest Income after Provision','Net Interest Inc After Loan Loss Prov Growth',
                 'Net Interest Margin','Non-Interest Income','Securities Gain','Trading Account Income','Trust Income, Commissions & Fees',
                 'Commission & Fee Income','Other Operating Income','Non-Interest Expense','Labor & Related Expense','Equipment Expense',
                 'Other Operating Expense','Operating Income','Operating Income Growth','Operating Income Margin','Non-Operating Income (Expense)',
                 'Non-Operating Interest Income','Miscellaneous Non Operating Expense','Premiums Earned','Realized Gains (Losses)','Losses, Claims & Reserves',
                 'Losses, Claims & Reserves Growth','Losses, Benefits & Adjustments','Loss Ratio','Selling, General & Admin. Expenses & Other',
                 'Income Taxes','Selling, General & Admin. Expenses','Other Selling, General & Admin. Expense','Underwriting & Commissions',
                 'Operating Income Before Interest Expense','Interest Expense, Net of Interest Capitalized','Interest Expense (excl. Interest Capitalized)',
                 'Operating Income After Interest Expense','Income Tax - Current - Domestic','Income Tax - Current - Foreign','Income Tax - Deferred - Domestic',
                 'Income Tax - Deferred - Foreign','Net Income Margin','EPS (Basic) Grwoth']

useful_all_item_name_list = []
for x in all_item_list:
    if x not in useful_all_item_name_list:
        useful_all_item_name_list.append(x)

mark_list = [0] * len(all_useful_item_list)
for number_index in range(len(all_useful_item_list)):
    if all_useful_item_list[number_index] in useful_all_item_name_list:
        mark_list[number_index] = 1

current_attribute = ''
current_data = ''
dict = {}
for number_index in range(len(all_useful_item_list)):
    if mark_list[number_index] == 1:
        current_attribute = all_useful_item_list[number_index]
    else:
        if current_attribute in dict:
            dict[current_attribute].append(all_useful_item_list[number_index])
        else:
            dict[current_attribute] = [all_useful_item_list[number_index]]

df = pd.DataFrame(dict)
aosf.save_df_as_csv(df,'A')
