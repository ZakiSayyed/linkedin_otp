import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()       
# Set your Supabase credentials
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Fetch data from a table
table_name = "linkedin_otp"
response = supabase.table(table_name).select("otp").execute()

if response.data:
    # Extract OTPs into a list
    otps = [row["otp"] for row in response.data if "otp" in row]
    
    for otp in otps:
        st.write(f"Linkedin otp is : {otp}")  # print each OTP nicely
else:
    st.write("No OTP found or error occurred.")
    st.error(response.error if response.error else "Unknown error")