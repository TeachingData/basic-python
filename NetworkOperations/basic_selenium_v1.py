from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Basic overview of selenium over Beautiful Soup for webscrapping.
Doesn't yet use keys (see version 2) but does allow scraping of a table elements for building a csv file.
"""
if __name__ == '__main__':
    # Create the webdriver (using Chrome as most universal)
    driver = webdriver.Chrome()
    driver.get("https://fgcuathletics.com/sports/womens-soccer/stats/2022")
    # Add an Error if 404 or site down
    assert "Page not found" not in driver.page_source

    # Table_rows will be list of list to hold our table for writing
    table_rows = []

    # Grab the first table (only one) and pull its table headers (th) elements
    # Only need first 3 so splice and then use with list comprehension to combine
    table_data = driver.find_elements(By.XPATH, "//table[1]//th")
    table_rows.append([h.text for h in table_data[0:3]])

    # Grab the tr elements now and add to list if more than one
    # there are seperate "headers" in the table for spliting sections - we don't want those
    table_data = driver.find_elements(By.XPATH, "//table[1]/tbody/tr")
    for row in table_data:
        if row.text:
            cur_row = row.text.split(" ")
            if len(cur_row) != 1:
                table_rows.append(cur_row)

    for i, row in enumerate(table_rows):
        print(f"Row {i} is: {row}")
    driver.close()
