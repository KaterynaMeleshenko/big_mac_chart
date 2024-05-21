from calculations import big_mac_price_2024
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

def plot_prices(sort_column):
    
    # Sort the filtered data
    if sort_column == 'name':
        sorted_data = big_mac_price_2024.sort_values(by=sort_column, ascending=False)
    else: sorted_data = big_mac_price_2024.sort_values(by=sort_column, ascending=True)

    # Extract relevant columns
    countries = sorted_data['name']
    nominal_prices = sorted_data['big_mac_doll']  # Nominal prices in USD
    adjusted_prices = sorted_data['adj_doll']  # Adjusted prices in USD

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 12)) 

    # Plot nominal prices
    ax.plot(nominal_prices, range(len(countries)), marker='o', linestyle='', color='b', label='Nominal Price (USD)')

    # Plot adjusted prices
    ax.plot(adjusted_prices, range(len(countries)), marker='*', linestyle='', color='r', label='Adjusted Price (USD)')

    # Add labels and title
    ax.set_yticks(range(len(countries)))
    ax.set_yticklabels(countries)
    ax.set_xlabel('Price (USD)')
    ax.set_title('Nominal vs Adjusted Prices')

    ax.set_xticks(range(0, max(max(nominal_prices.astype(int)), max(adjusted_prices.astype(int))) + 1, 10))  # Adjust the step size as needed

    # Add legend
    ax.legend()

    # Show plot
    plt.show()

# Create interactive widget
interact(plot_prices,
         sort_column=widgets.Dropdown(options=['big_mac_doll', 'adj_doll', 'name'], description='Sort Value:')
        );
