import streamlit as st
import pandas as pd

# Load data from CSV
data = pd.read_csv('asd.csv')  # Make sure 'products.csv' is the correct file path

# App title
st.markdown(
            """
            <style>
            /* Basic styling adjustments */
            .stRadio > label { font-size: 18px; }
            .stSelectbox > label, .stTextInput > label { font-size: 16px; }
            .stExpander > label { font-size: 16px; }
            </style>
            """,
            unsafe_allow_html=True,
        )
st.subheader("Ishak Enterprise -")
# Choose search option
search_option = st.radio("Search By", ["Product Name","Group Name","Product Sub Name"])

if search_option == "Product Name":
    # Dropdown to select product name
    product_name = st.selectbox("Select a Product Name", [""] + list(data['product_name'].unique()))

    # Filter and display the data for the selected product
    filtered_data = data[data['product_name'] == product_name]

    if not filtered_data.empty:

        # Display product details row by row
        for _, row in filtered_data.iterrows():
            st.write(f"**Product Name:** {row['product_name']}")
            st.write(f"**DP Price:** {row['dp_price']}")
            st.write(f"**Group Name:** {row['group_name']}")

            st.write("---")  # Divider between entries (if there are multiple)

# Search by Product Name
elif search_option == "Product Sub Name":

    # Text input for searching product names with a placeholder
    product_search = st.text_input("Type to search Product Name", placeholder="Start typing to search...")

    # Filter product names based on input
    if product_search:
        # Display all rows with product names that contain the search text (case-insensitive)
        filtered_products = data[data['product_name'].str.contains(product_search, case=False, na=False)]
    else:
        # Show all products if no search term is provided
        filtered_products = data

    # Check if there are any matching products to display
    if not filtered_products.empty:

        # Display matching product details in a table format
        st.write(filtered_products[['product_name', 'dp_price', 'mrp_price', 'group_name', 'available_stock']])
    else:
        st.write("No matching products found.")

# Search by Group Name
elif search_option == "Group Name":
    # Dropdown to select a group
    group_name = st.selectbox("Select a Group", ["Premium", "Prestige", "Popular", "Prominent","Pacific","Prado","Winner","Bikrampur Plastic","Taj Plastic","Lira Plastic","KRM Plastic","Bengal Plastic","Akij Plastic","Tel","Diamond Plastic","Dhaka Steel","Dhaka Plastic"])

    # Filter and display the data for the selected group
    filtered_data = data[data['group_name'] == group_name]
    st.write(filtered_data[['product_name', 'dp_price', 'mrp_price', 'group_name', 'available_stock']])

else:
    st.error("CSV file is missing required columns. Make sure it contains 'product_name' and 'group_name'.")