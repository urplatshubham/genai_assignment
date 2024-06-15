import pandas as pd

# Load the Excel file
file_path = r'D:/C# training/Python-GenAI-assignment/HDFC132-02.5.23.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')
# Clean the data by removing rows with missing dates

cleaned_data = data.dropna(subset=['Date'])
# Convert the 'Date' column to a proper datetime format, specifying dayfirst=True for dd/mm/yy format
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'], dayfirst=True, errors='coerce')

# Group the data by date and calculate the required statistics
day_wise_analysis = cleaned_data.groupby(cleaned_data['Date'].dt.date).agg(
    total_deposits=pd.NamedAgg(column='Deposit Amt.', aggfunc='sum'),
    total_withdrawals=pd.NamedAgg(column='Withdrawal Amt.', aggfunc='sum'),
    closing_balance=pd.NamedAgg(column='Closing Balance', aggfunc='last')
).reset_index()

# Display the day-wise analysis
print(day_wise_analysis)
