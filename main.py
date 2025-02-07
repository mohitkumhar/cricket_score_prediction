import streamlit as st
import pickle
import pandas as pd
import sklearn

pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'New Zealand',
    'West Indies',
    'South Africa',
    'India',
    'England',
    'Australia',
    'Hong Kong',
    'Bangladesh',
    'Oman',
    'Zimbabwe',
    'Ireland',
    'Scotland',
    'Pakistan',
    'Sri Lanka',
]

cities = ['Dubai',
 'Harare',
 'Dhaka',
 'Colombo',
 'Abu Dhabi',
 'Lahore',
 'Sydney',
 'Auckland',
 'Lauderhill',
 'Melbourne',
 'Karachi',
 'Al Amarat',
 'Hobart',
 'Christchurch',
 "St George's",
 'Sharjah',
 'Wellington',
 'Dublin',
 'Mount Maunganui',
 'Centurion',
 'Johannesburg',
 'Edinburgh',
 'Adelaide',
 'Southampton',
 'Bridgetown',
 'Gros Islet',
 'Cape Town',
 'Perth',
 'Cardiff',
 'Ahmedabad',
 'Brisbane',
 'Manchester',
 'Basseterre',
 'Providence',
 'Kolkata',
 'Belfast',
 'Napier',
 'Hamilton',
 'Rawalpindi',
 'Chattogram',
 'Canberra',
 'Bristol',
 'Rajkot',
 'Tarouba',
 'Kandy',
 'Durban',
 'Bready',
 'Lucknow',
 'Nottingham',
 'Indore',
 'Kingston',
 'Mumbai',
 'Birmingham',
 'Coolidge',
 'Delhi',
 'Trinidad',
 'Ranchi',
 'Thiruvananthapuram']


st.title("Cricket Score Predictor")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select batting team", sorted(teams))
    
with col2:
    bowling_team = st.selectbox("Select Bowling Team", sorted(teams))

city = st.selectbox("Select City", sorted(cities))


col3, col4, col5 = st.columns(3)

with col3:
    current_score = st.number_input("Enter Current Score")

with col4:
    overs_done = st.number_input("Enter Overs Done")

with col5:
    wickets = st.number_input("Wickets Out")

last_five = 0

if overs_done >= 5:
    last_five = st.number_input("Runs scored in last 5 overs")



if st.button("Predict Score"):
    
    features = {
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'current_score': [current_score],
        'balls_left': [120 - 6 * overs_done],
        'wickets_left': [10 - wickets],
        'run_rate': [(current_score / overs_done) if overs_done > 0 else 0],
        'last_five': [last_five],
    }
    
    features_df = pd.DataFrame(features)
    
    st.table(features_df)
    
    
    pred = pipe.predict(features_df)
    
    st.header(f"The Predicted Score is: {str(int(pred[0]))}")
    



