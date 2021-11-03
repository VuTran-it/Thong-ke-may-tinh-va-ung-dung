import pandas as pd
path = 'Data_Excercise\csv_Data_Loan.csv'
data = pd.read_csv(path)
data.info()

df_number = data[['loan_amnt','int_rate','emp_length','annual_inc','dti','delinq_2yrs','revol_util','total_acc','bad_loan','longest_credit_length']]
print(df_number.head(5))

print('================================================================================')
df_object = data[['term','home_ownership','purpose','addr_state','verification_status']]
print(df_object.head(5))

print('==========================================')
path_excel = 'Data_Excercise\excel_Data_Movies.xls'
data_excel = pd.read_excel(path_excel)
data_excel.info()

print('==========================================')
path_excel = 'Data_Excercise\excel_Data_Point.xlsx'
data_excel = pd.read_excel(path_excel)
data_excel.info()