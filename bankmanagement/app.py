import streamlit as st
from improvized import Bank  # Assuming the class above is saved in `bank.py`

bank = Bank()
st.set_page_config(page_title="Bank Management", layout="centered")

st.title("🏦 Bank Management System")

menu = [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "View Account Details",
    "Update Account",
    "Delete Account"
]
choice = st.sidebar.selectbox("Choose operation", menu)

# Account creation
if choice == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0)
    phone = st.text_input("Phone Number")
    pin = st.number_input("4-digit PIN", min_value=1000, max_value=9999, format="%d")

    if st.button("Create Account"):
        result = bank.create_account(name, age, phone, pin)
        if result["success"]:
            st.success("Account created!")
            st.json(result["user"])
        else:
            st.error(result["message"])

# Deposit
elif choice == "Deposit Money":
    st.header("Deposit Funds")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", format="%d")
    amount = st.number_input("Amount", min_value=1, max_value=10000)

    if st.button("Deposit"):
        result = bank.deposit(acc, pin, amount)
        if result["success"]:
            st.success(f"Deposited successfully. New balance: ₹{result['balance']}")
        else:
            st.error(result["message"])

# Withdraw
elif choice == "Withdraw Money":
    st.header("Withdraw Funds")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", format="%d")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        result = bank.withdraw(acc, pin, amount)
        if result["success"]:
            st.success(f"Withdrawn successfully. New balance: ₹{result['balance']}")
        else:
            st.error(result["message"])

# View details
elif choice == "View Account Details":
    st.header("Account Details")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", format="%d")

    if st.button("Fetch Details"):
        result = bank.get_details(acc, pin)
        if result["success"]:
            st.json(result["user"])
        else:
            st.error(result["message"])

# Update details
elif choice == "Update Account":
    st.header("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", format="%d")
    field = st.selectbox("Field to update", ["name", "phno", "pin"])
    if field == "pin":
        new_value = st.number_input("New PIN", min_value=1000, max_value=9999, format="%d")
    else:
        new_value = st.text_input(f"New {field.title()}")

    if st.button("Update"):
        result = bank.update_details(acc, pin, field, new_value)
        if result["success"]:
            st.success("Updated successfully")
            st.json(result["user"])
        else:
            st.error(result["message"])

# Delete account
elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.number_input("PIN", format="%d")
    confirm = st.checkbox("Confirm account deletion")

    if st.button("Delete") and confirm:
        result = bank.delete_account(acc, pin)
        if result["success"]:
            st.success(result["message"])
        else:
            st.error(result["message"])
    elif st.button("Delete"):
        st.warning("You must confirm deletion.")
