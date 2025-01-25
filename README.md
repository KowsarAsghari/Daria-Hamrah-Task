Prompt 1:
I am working on a task to process a CSV file containing sales data. I want to use Python with pandas and re libraries. The tasks include cleaning a date column to convert it to the yyyy-mm-dd format, cleaning two price columns (discount_price and actual_price) to remove currency symbols and separators, and converting them to float. Finally, I need to calculate monthly sales totals and average discount percentages, saving these results to CSV files.

Prompt 2:
Please structure the solution using Object-Oriented Programming (OOP) in Python. Create a class called SalesDataProcessor with methods to load data, clean the date column, clean the price columns, calculate monthly total sales, calculate average monthly discounts, and save the results to CSV files. Include a process() method to run all these steps in sequence.

Prompt 3:
Write the clean_date_column method in the class. It should convert the date column to the yyyy-mm-dd format, handling invalid dates gracefully using errors='coerce'. Use pandas for this task.

Prompt 4:
Write the clean_price_columns method. It should clean the discount_price and actual_price columns by removing any non-numeric characters (e.g., currency symbols, commas) and converting the values to float. Use the re library for regex matching.

Prompt 5:
Write the calculate_monthly_sales method. It should calculate the total sales for both the discount price and the actual price, grouped by month. The result should be saved as a CSV file named monthly_sales.csv. Use pandas for grouping and aggregation.

Prompt 6:
Write the calculate_monthly_avg_discount method. It should calculate the average discount percentage offered each month. The discount percentage for each row is 1 - (discount_price / actual_price). Group by month, calculate the average, and save the result to a CSV file named monthly_avg_discount.csv.

Prompt 7:
Combine all these methods into a process() method in the class, which will call all the steps in sequence. Ensure it returns the processed DataFrames for monthly sales and average discounts. Add an example usage under the if __name__ == "__main__": block, and make it executable.

Prompt 8:
Add functionality to print the resulting DataFrames for monthly_sales and monthly_avg_discount at the end of the script, after they are processed.
