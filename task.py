import pandas as pd
import re

class SalesDataProcessor:
    def __init__(self, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path
        self.data = None

    def load_data(self):
        """Loads the dataset into a pandas DataFrame."""
        self.data = pd.read_csv(self.file_path, low_memory=False)

    def clean_date_column(self):
        """Converts the `date` column to the standard yyyy-mm-dd format."""
        self.data['date'] = pd.to_datetime(self.data['date'], errors='coerce').dt.strftime('%Y-%m-%d')

    def clean_price_columns(self):
        """Cleans and converts `discount_price` and `actual_price` columns to float."""
        def clean_price(price):
            if isinstance(price, str):
                return float(re.sub(r'[^\d.]', '', price))
            return price

        self.data['discount_price'] = self.data['discount_price'].apply(clean_price)
        self.data['actual_price'] = self.data['actual_price'].apply(clean_price)

    def calculate_monthly_sales(self):
        """Calculates monthly total sales for discount and actual prices."""
        self.data['month'] = pd.to_datetime(self.data['date']).dt.to_period('M')
        monthly_sales = self.data.groupby('month').agg(
            total_discount_price=('discount_price', 'sum'),
            total_actual_price=('actual_price', 'sum')
        ).reset_index()
        monthly_sales.to_csv(f'{self.output_path}/monthly_sales.csv', index=False)
        return monthly_sales

    def calculate_monthly_avg_discount(self):
        """Calculates the average discount percentage for each month."""
        self.data['discount_percentage'] = (
            1 - self.data['discount_price'] / self.data['actual_price']
        ) * 100
        monthly_avg_discount = self.data.groupby('month').agg(
            avg_discount_percentage=('discount_percentage', 'mean')
        ).reset_index()
        monthly_avg_discount.to_csv(f'{self.output_path}/monthly_avg_discount.csv', index=False)
        return monthly_avg_discount

    def process(self):
        """Executes all steps in sequence."""
        self.load_data()
        self.clean_date_column()
        self.clean_price_columns()
        monthly_sales = self.calculate_monthly_sales()
        monthly_avg_discount = self.calculate_monthly_avg_discount()
        print("Processing complete. Files saved to output directory.")
        return monthly_sales, monthly_avg_discount


# Usage example
if __name__ == "__main__":
    file_path = 'C:/Users/kowsa/OneDrive/Desktop/Amazon-Products - online.csv'
    output_path = 'C:/Users/kowsa/OneDrive/Desktop'

    processor = SalesDataProcessor(file_path, output_path)
    monthly_sales, monthly_avg_discount = processor.process()

    # Print results
    print("\nMonthly Sales:")
    print(monthly_sales)

    print("\nMonthly Average Discount:")
    print(monthly_avg_discount)
