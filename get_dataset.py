import pandas as pd
import random
random.seed(123)

DATASET_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/?company=WELLS%20FARGO%20%26%20COMPANY&date_received_max=2022-12-31&date_received_min=2019-01-01&field=all&format=csv&has_narrative=true&no_aggs=true&size=15261&sort=created_date_desc"

def main():
    df = pd.read_csv(DATASET_URL)
    dfs = []
    # Product = "Checking or savings account"
    dfs.append(df[df['Sub-product'] == "Checking account"].sample(n=200, random_state=123))
    dfs.append(df[df['Sub-product'] == "Other banking product or service"].sample(n=200, random_state=123))
    dfs.append(df[df['Sub-product'] == "Savings account"].sample(n=200, random_state=123))

    # Product = "Mortage"
    dfs.append(df[df['Sub-product'] == "Conventional home mortgage"].sample(n=120, random_state=123))
    dfs.append(df[df['Sub-product'] == "FHA mortgage"].sample(n=120, random_state=123))
    dfs.append(df[df['Sub-product'] == "VA mortgage"].sample(n=120, random_state=123))
    dfs.append(df[df['Sub-product'] == "Home equity loan or line of credit (HELOC)"].sample(n=120, random_state=123))
    dfs.append(df[df['Sub-product'] == "Other type of mortgage"].sample(n=120, random_state=123))

    # Product = "Credit reporting, credit repair services, or other personal consumer reports"
    dfs.append(df[df['Sub-product'] == "Credit reporting"].sample(n=600, random_state=123))
    
    # Product = "Credit card or prepaid card"
    dfs.append(df[df['Sub-product'] == "General-purpose credit card or charge card"].sample(n=600, random_state=123))
    
    # Product = "Money transfer, virtual currency, or money service"
    dfs.append(df[df['Sub-product'] == "Domestic (US) money transfer"].sample(n=300, random_state=123))
    dfs.append(df[df['Sub-product'] == "Mobile or digital wallet"].sample(n=300, random_state=123))
    
    # Product = "Vehicle loan or lease"
    dfs.append(df[df['Sub-product'] == "Loan"].sample(n=559, random_state=123))

    # Join all dfs 
    df = pd.concat(dfs)
    # only keep the columns "Product", "Consumer complaint narrative"
    df = df[['Product', 'Sub-product', 'Consumer complaint narrative']]
    df.to_csv('wells_fargo.csv', index=False)

if __name__ == "__main__":
    main()

