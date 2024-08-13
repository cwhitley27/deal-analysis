import streamlit as st
import math

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stApp {
            max-width: 800px;
            margin: auto;
        }
        .stButton>button {
            background-color: #0057B7;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #004a9c;
        }
        .stNumberInput>div>input {
            font-size: 16px;
            padding: 8px;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # App Title
    st.title("Real Estate Investment Calculator")

    # Input Fields
    st.header("Property Information")
    purchase_price = st.number_input("Purchase Price ($)", min_value=0, value=150000, step=1000)
    rehab_costs = st.number_input("Rehabilitation Costs ($)", min_value=0, value=30000, step=1000)
    arv = st.number_input("After Repair Value (ARV) ($)", min_value=0, value=250000, step=1000)

    st.header("Mortgage Information")
    down_payment_percentage = st.number_input("Down Payment (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    loan_term_years = st.number_input("Loan Term (Years)", min_value=5, max_value=30, value=30, step=1)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)

    st.header("Rental Income")
    current_rent = st.number_input("Current Monthly Rent ($)", min_value=0, value=2000, step=100)
    market_rent = st.number_input("Market Monthly Rent ($)", min_value=0, value=2500, step=100)

    st.header("Expenses & Assumptions")
    management_fee_percentage = st.number_input("Property Management Fee (%)", min_value=0.0, max_value=20.0, value=10.0, step=0.1)
    maintenance_fee_percentage = st.number_input("Maintenance Costs (%)", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
    vacancy_rate_percentage = st.number_input("Vacancy Rate (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    property_tax = st.number_input("Annual Property Tax ($)", min_value=0, value=3000, step=100)
    insurance = st.number_input("Annual Homeowners Insurance ($)", min_value=0, value=1500, step=100)

    # Mortgage Calculations
    down_payment = purchase_price * (down_payment_percentage / 100)
    loan_amount = arv - down_payment
    monthly_interest_rate = interest_rate / 100 / 12
    number_of_payments = loan_term_years * 12
    monthly_principal_interest = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments / ((1 + monthly_interest_rate)**number_of_payments - 1)

    # Rental Income Calculations
    annual_current_rental_income = current_rent * 12
    annual_market_rental_income = market_rent * 12

    # Operating Expenses
    management_cost_current = annual_current_rental_income * (management_fee_percentage / 100)
    maintenance_cost_current = annual_current_rental_income * (maintenance_fee_percentage / 100)
    vacancy_reserve_current = annual_current_rental_income * (vacancy_rate_percentage / 100)
    total_operating_expenses_current = management_cost_current + maintenance_cost_current + vacancy_reserve_current + property_tax + insurance

    management_cost_market = annual_market_rental_income * (management_fee_percentage / 100)
    maintenance_cost_market = annual_market_rental_income * (maintenance_fee_percentage / 100)
    vacancy_reserve_market = annual_market_rental_income * (vacancy_rate_percentage / 100)
    total_operating_expenses_market = management_cost_market + maintenance_cost_market + vacancy_reserve_market + property_tax + insurance

    # NOI and Cash Flow Calculations
    noi_current = annual_current_rental_income - total_operating_expenses_current
    cash_flow_current = noi_current - (monthly_principal_interest * 12)

    noi_market = annual_market_rental_income - total_operating_expenses_market
    cash_flow_market = noi_market - (monthly_principal_interest * 12)

    # Cash-on-Cash Return and Cap Rate
    total_cash_invested = down_payment + rehab_costs + property_tax + insurance
    cash_on_cash_return_current = (cash_flow_current / total_cash_invested) * 100
    cash_on_cash_return_market = (cash_flow_market / total_cash_invested) * 100

    cap_rate_current = (noi_current / purchase_price) * 100
    cap_rate_market = (noi_market / purchase_price) * 100

    # Display Results
    st.header("Investment Performance - Current Rents")
    st.write(f"**Loan Amount:** ${loan_amount:,.2f}")
    st.write(f"**Monthly Principal & Interest Payment:** ${monthly_principal_interest:,.2f}")
    st.write(f"**Net Operating Income (NOI):** ${noi_current:,.2f}")
    st.write(f"**Cash Flow:** ${cash_flow_current:,.2f}")
    st.write(f"**Cash-on-Cash Return:** {cash_on_cash_return_current:.2f}%")
    st.write(f"**Cap Rate:** {cap_rate_current:.2f}%")

    st.header("Investment Performance - Market Rents")
    st.write(f"**Net Operating Income (NOI):** ${noi_market:,.2f}")
    st.write(f"**Cash Flow:** ${cash_flow_market:,.2f}")
    st.write(f"**Cash-on-Cash Return:** {cash_on_cash_return_market:.2f}%")
    st.write(f"**Cap Rate:** {cap_rate_market:.2f}%")

if __name__ == "__main__":
    main()
