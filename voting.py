import streamlit as st
import pandas as pd
import numpy as np

st.image('voting.jpg', width=150)
st.title('To be President')
st.text("Need 269 electoral votes from 538 votes)")
df = pd.read_csv('Dashboard.csv')
font="sans serif"
     
st.write('Data Source: https://github.com/cs109/content/blob/master/HW2_solutions.ipynb')
if st.checkbox('Show 2012 election raw data'):
    st.subheader('Raw data')
    st.write(df)
    
st.sidebar.header('Vote')

st.markdown(f'<h1 style="color:#ad070a;font-size:24px;">{"State Voter Facts"}</h1>', unsafe_allow_html=True) 

st.write('33 states have early voting')
st.write('3 states conduct all elections by mail')
st.markdown('20 states require excuse to vote absentee ballot mail')
st.markdown('Maine and Nebraska can split their electoral votes')

st.markdown(f'<h1 style="color:#072deb;font-size:24px;">{"State Party Affiliation"}</h1>', unsafe_allow_html=True) 
         
st.sidebar.header('Presidential Facts')
st.sidebar.header('46 Presidents have served')
st.sidebar.header('26 Presidents were prior lawyers')
st.sidebar.header('12 Presidents were generals')
st.sidebar.header('VOTE')

# Remove whitespace from the top of the page
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

DATA_URL = ('https://github.com/cs109/content/blob/master/HW2_solutions.ipynb')

import plotly.express as px
state_codes = {
    'District of Columbia' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
    'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
    'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
    'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
    'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
    'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
    'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
    'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
    'Vermont': 'VT', 'Georgia': 'GA', 'North Dakota': 'ND', 
    'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
    'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
    'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 
    'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 
    'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 
    'Nevada': 'NV', 'Maine': 'ME'}

df['state_code'] = df['State'].apply(lambda x : state_codes[x])
df['Party Name'] = df['Party Name'].astype(str)
fig = px.choropleth(df,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Party Name',
                    color_discrete_map= {'Republican': 'red', 'Democratic':'blue'}
                    )

st.plotly_chart(fig)

st.subheader('Electoral Votes')

electoral = st.slider('How many Electoral Votes Need?', 0, 538, 23)
st.write("Have ", electoral, 'Need 269 votes to be President', 269-electoral, 'Still Needed')

voting = st.slider('State Voting?', 0, 51, 23)
st.write("How many states with DC have reported?", voting, "Do we have a winner?", 51-voting, "States have not voted")  

st.header('Political Party Affiliation?') 

option = st.selectbox(
     'What is your political party affiliation?',
     ('Democratic', 'Republican', 'Independent', 'Green Party', 'Other'))

st.write('Your political party: ', option)


st.header('Political Parties: Vote')

options = st.multiselect(
     'What political party nominees have you voted for?',
     ['Democratic', 'Republican', 'Independent', 'Green Party', 'Other'])

st.write('Your Party:', options)

st.markdown(f'<h1 style="color:#ad070a;font-size:30px;">{"Pick a state for more information"}</h1>', unsafe_allow_html=True) 

AL = st.checkbox('Alabama')
if AL:
    st.write('9 Electoral Votes')
    st.write('State Pie: Buttermilk Pie')
    st.write('State Flower: Camellia')
    st.write('Famous Politician: Condoleezza Rice')
    
AK = st.checkbox('Alaska')    
if AK:
    st.write('3 Electoral Votes')
    st.write('State Pie: Pirok Salmon Pie')
    st.write('State Flower: Alpine Forget-me-not')
    st.write('Famous Politician: Mary Peltola')   
       
AZ = st.checkbox('Arizona')    
if AZ:
    st.write('11 Electoral Votes')    
    st.write('State Pie: Prickly Pear Pie')
    st.write('State Flower: Saguaro Cactus Blossom')
    st.write('Famous Politician: Barry Goldwater')
    
AR = st.checkbox('Arkansas')    
if AR:
    st.write('6 Electoral Votes')
    st.write('State Pie: Possum Pie aka Chocolate Layer Pie')
    st.write('State Flower: Apple Blossom')
    st.write('Famous Politician: President Bill Clinton')
        
CA = st.checkbox('California')    
if CA:
    st.write('55 Electoral Votes')
    st.write('State Pie: Boysenberry Pie')
    st.write('State Flower: Poppy')
    st.write('Famous Politician: President Richard Nixon')
        
CO = st.checkbox('Colorado')    
if CO:
    st.write('9 Electoral Votes')
    st.write('State Pie: Rocky Road Pie')
    st.write('State Flower: Columbine')
    st.write('Famous Politician: John Kerry')

CT = st.checkbox('Connecticut')    
if CT:
    st.write('7 Electoral Votes')
    st.write('State Pie: Pumpkin Pie')
    st.write('State Flower: Mountain Laurel')
    st.write('Famous Politician: President George W Bush')

DE = st.checkbox('Delaware')    
if DE:
    st.write('7 Electoral Votes')
    st.write('State Pie: Peach Pie')
    st.write('State Flower: Peach Blossom')
    st.write('Famous Politician: Caesar Rodney')

FL = st.checkbox('Florida')    
if FL:
    st.write('29 Electoral Votes')
    st.write('State Pie: Key Lime Pie')
    st.write('State Flower: Orange Blossom')
    st.write('Famous Politician: Janet Reno')

GA = st.checkbox('Georgia')    
if GA:
    st.write('16 Electoral Votes')
    st.write('State Pie: Peach Pie')
    st.write('State Flower: Cherokee Rose')
    st.write('Famous Politician: President Jimmy Carter')

HI = st.checkbox('Hawaii')    
if HI:
    st.write('4 Electoral Votes')
    st.write('State Pie: Chocolate Haupia Pie')
    st.write('State Flower: Hibiscus')
    st.write('Famous Politician: President Barack Obama')

ID = st.checkbox('Idaho')    
if ID:
    st.write('4 Electoral Votes')
    st.write('State Pie: Shephards Pie')
    st.write('State Flower: Syringa')
    st.write('Famous Politician: Sarah Palin')
       
IL = st.checkbox('Illinois')    
if IL:
    st.write('20 Electoral Votes')
    st.write('State Pie: Pumpkin Pie')
    st.write('State Flower: Violet')
    st.write('Famous Politician: President Ronald Reagan')

IN = st.checkbox('Indiana')    
if IN:
    st.write('11 Electoral Votes')
    st.write('State Pie: Hoosier Pie')
    st.write('State Flower: Peony')
    st.write('Famous Politician: Mike Pence')
    
IA = st.checkbox('Iowa')    
if IA:
    st.write('6 Electoral Votes')
    st.write('State Pie: Sour Cream Raisin Pie')
    st.write('State Flower: Prairie Rose')
    st.write('Famous Politician: President Herbert Hoover')    

KS = st.checkbox('Kansas')    
if KS:
    st.write('6 Electoral Votes')
    st.write('State Pie: Cherry Pie')
    st.write('State Flower: Sunflower')
    st.write('Famous Politician: Bob Dole')    
             
KY = st.checkbox('Kentucky')    
if KY:
    st.write('8 Electoral Votes')
    st.write('State Pie: Derby Pie')
    st.write('State Flower: Goldenrod')
    st.write('Famous Politician: President Abraham Lincoln')  

LA = st.checkbox('Louisiana')    
if LA:
    st.write('8 Electoral Votes')
    st.write('State Pie: Natchitoches Meat Pie')
    st.write('State Flower: Magnolia')
    st.write('Famous Politician: Huey Long')  
                  
ME = st.checkbox('Maine')    
if ME:
    st.write('4 Electoral Votes')
    st.write('State Pie: Blueberry Pie')
    st.write('State Flower: White Pine Cone')
    st.write('Famous Politician: Nelson Rockefeller')  

MD = st.checkbox('Maryland')    
if MD:
    st.write('10 Electoral Votes')
    st.write('State Pie: Smith Island Pie')
    st.write('State Flower: Black-Eyed Susan')
    st.write('Famous Politician: Spiro Agnew') 
    
MA = st.checkbox('Massachusetts')    
if MA:
    st.write('11 Electoral Votes')    
    st.write('State Pie: Boston Cream Pie')
    st.write('State Flower: Mayflower')
    st.write('Famous Politician: President John F Kennedy') 
    
MI = st.checkbox('Michigan')    
if MI:
    st.write('16 Electoral Votes') 
    st.write('State Pie: Cherry Pie')
    st.write('State Flower: Apple Blossom')
    st.write('Famous Politician: Dr. Ben Carson') 
    
MN = st.checkbox('Minnesota')    
if MN:
    st.write('10 Electoral Votes') 
    st.write('State Pie: Banana Cream Pie')
    st.write('State Flower: Lady Slipper')
    st.write('Famous Politician: Walter Mondale') 
    
MS = st.checkbox('Mississippi')    
if MS:
    st.write('6 Electoral Votes') 
    st.write('State Pie: Mississippi Mud Pie')
    st.write('State Flower: Magnolia')
    st.write('Famous Politician: Roger Wicker') 
    
MO = st.checkbox('Missouri')    
if MO:
    st.write('10 Electoral Votes') 
    st.write('State Pie: Butterscotch Pie')
    st.write('State Flower: White Hawthorn Blossom')
    st.write('Famous Politician: President Harry S Truman') 
    
MT = st.checkbox('Montana')    
if MT:
    st.write('3 Electoral Votes') 
    st.write('State Pie: Huckleberry Pie')
    st.write('State Flower: Bitterroot')
    st.write('Famous Politician: Jeannette Rankin') 
        
NE = st.checkbox('Nebraska')    
if NE:
    st.write('5 Electoral Votes')     
    st.write('State Pie: Dutch Cranberry-Apple Pie')
    st.write('State Flower: Goldenrod')
    st.write('Famous Politician: President Gerald Ford')
    
NV = st.checkbox('Nevada')    
if NV:
    st.write('6 Electoral Votes')  
    st.write('State Pie: Chocolate Sin Pie')
    st.write('State Flower: Sagebrush')
    st.write('Famous Politician: Harry Reid')

NH = st.checkbox('New Hampshire')    
if NH:
    st.write('4 Electoral Votes')  
    st.write('State Pie: Whoopie Pie')
    st.write('State Flower: Pink Ladys Slipper')
    st.write('Famous Politician: President Franklin Pierce')
       
NJ = st.checkbox('New Jersey')    
if NJ:
    st.write('14 Electoral Votes')    
    st.write('State Pie: Tomato Pie')
    st.write('State Flower: Violet')
    st.write('Famous Politician: President Grover Cleveland')
    
NM = st.checkbox('New Mexico')    
if NM:
    st.write('5 Electoral Votes') 
    st.write('State Pie: Frito Pie')
    st.write('State Flower: Yucca')
    st.write('Famous Politician: Dennis Chavez')
    
NY = st.checkbox('New York')    
if NY:
    st.write('29 Electoral Votes') 
    st.write('State Pie: Concord Grape Pie')
    st.write('State Flower: Rose')
    st.write('Famous Politician: President Donald Trump')   
            
NC = st.checkbox('North Carolina')    
if NC:
    st.write('15 Electoral Votes')
    st.write('State Pie: Sweet Potatoe Pie')
    st.write('State Flower: Dogwood')
    st.write('Famous Politician: President James K Polk')
    
ND = st.checkbox('North Dakota')    
if ND:
    st.write('3 Electoral Votes')     
    st.write('State Pie: Chokecherry Pie')
    st.write('State Flower: Wild Prairie Rose')
    st.write('Famous Politician: Milton R Young')
     
OH = st.checkbox('Ohio')    
if OH:
    st.write('18 Electoral Votes') 
    st.write('State Pie: Shaker Sugar Pie')
    st.write('State Flower: Carnation')
    st.write('Famous Politician: President Ulysses S Grant')
        
OK = st.checkbox('Oklahoma')    
if OK:
    st.write('7 Electoral Votes')     
    st.write('State Pie: Fried Pie')
    st.write('State Flower: Indian Blanket')
    st.write('Famous Politician: Elizabeth Warren')
    
OR = st.checkbox('Oregon')    
if OR:
    st.write('7 Electoral Votes')
    st.write('State Pie: Marionberry Pie')
    st.write('State Flower: Oregon Grape')
    st.write('Famous Politician: Mark Hatfield')
        
PA = st.checkbox('Pennsylvania')    
if PA:
    st.write('20 Electoral Votes')
    st.write('State Pie: Shoofly Pie')
    st.write('State Flower: Mountain Laurel')
    st.write('Famous Politician: President Joseph R Biden')
    
RI = st.checkbox('Rhode Island')    
if RI:
    st.write('4 Electoral Votes')
    st.write('State Pie: Coconut Custard Pie')
    st.write('State Flower: Violet')
    st.write('Famous Politician: Martha McSally')
    
SC = st.checkbox('South Carolina')    
if SC:
    st.write('9 Electoral Votes')
    st.write('State Pie: Tomato Pie')
    st.write('State Flower: Yellow Jessamine')
    st.write('Famous Politician: President Andrew Jackson')
    
SD = st.checkbox('South Dakota')    
if SD:
    st.write('3 Electoral Votes')
    st.write('State Pie: Kuchen Pie')
    st.write('State Flower: American Pasque')
    st.write('Famous Politician: Hubert Humphrey')
       
TN = st.checkbox('Tennessee')    
if TN:
    st.write('11 Electoral Votes')
    st.write('State Pie: Bourbon Pecan Pie')
    st.write('State Flower: Iris')
    st.write('Famous Politician: Julian Bond')
    
TX = st.checkbox('Texas')    
if TX:
    st.write('38 Electoral Votes')
    st.write('State Pie: Pecan Pie')
    st.write('State Flower: Bluebonnet')
    st.write('Famous Politician: President Dwight D Eisenhower')
    
UT = st.checkbox('Utah')    
if UT:
    st.write('6 Electoral Votes')
    st.write('State Pie: Rhubarb Cherry Pie')
    st.write('State Flower: Sego Lily')
    st.write('Famous Politician: Florence Ellinwood Allen')
    
VT = st.checkbox('Vermont')    
if VT:
    st.write('3 Electoral Votes')    
    st.write('State Pie: Apple Pie')
    st.write('State Flower: Red Clover')
    st.write('Famous Politician: President Calvin Coolidge')
    
VA = st.checkbox('Virginia')    
if VA:
    st.write('13 Electoral Votes')   
    st.write('State Pie: Peanut Pie')
    st.write('State Flower: American Dogwood')
    st.write('Famous Politician: President George Washington')
        
WA = st.checkbox('Washington')    
if WA:
    st.write('12 Electoral Votes')
    st.write('State Pie: Loganberry Pie')
    st.write('State Flower: Rhododendron')
    st.write('Famous Politician: Patty Murray')
           
WV = st.checkbox('West Virginia')    
if WV:
    st.write('5 Electoral Votes')   
    st.write('State Pie: Pawpaw Pie')
    st.write('State Flower: Rhododendron')
    st.write('Famous Politician: Cyrus Vance')
    
WI = st.checkbox('Wisconsin')    
if WV:
    st.write('10 Electoral Votes')  
    st.write('State Pie: Apple Pie')
    st.write('State Flower: Violet')
    st.write('Famous Politician: Tammy Baldwin')
        
WY = st.checkbox('Wyoming')    
if WY:
    st.write('3 Electoral Votes')  
    st.write('State Pie: Rhubarb Pie')
    st.write('State Flower: Indian Paintbrush')
    st.write('Famous Politician: Lynne Cheney')
                                            
DATE_COLUMN = 'date/time'
st.subheader ("Extra")

DC = st.checkbox('District of Columbia')    
if DC:
    st.write('3 Electoral Votes')
    st.write('Signature Pie: Cherry Pie')
    st.write('Flower: American Beauty Rose')
    st.write('Famous Politician: AL Gore')

st.markdown(f'<h1 style="color:#ad070a;font-size:75px;">{"Election Results"}</h1>', unsafe_allow_html=True) 
dz = pd.read_csv('summary.csv')
if st.checkbox('Summary 2012 election raw data'):
    st.subheader('Results')
    st.write(dz)
    
dz['States'] = df['State'].apply(lambda x : state_codes[x])
dz['Electoral'] = df['Need']
dz['Winner'] = dz["Winner"].astype(str)

st.markdown(f'<h1 style="color:#072deb;font-size:50px;">{"Democratic Party Wins"}</h1>', unsafe_allow_html=True) 
st.header("President Barack Obama is reelected ")
st.header("with 332 electoral votes") 

st.markdown(f'<h1 style="color:#ad070a;font-size:150px;">{"V"}</h1>', unsafe_allow_html=True) 
st.markdown(f'<h1 style="color:#072deb;font-size:150px;">{"O"}</h1>', unsafe_allow_html=True) 
st.markdown(f'<h1 style="color:#ad070a;font-size:150px;">{"T"}</h1>', unsafe_allow_html=True) 
st.markdown(f'<h1 style="color:#072deb;font-size:150px;">{"E"}</h1>', unsafe_allow_html=True) 
