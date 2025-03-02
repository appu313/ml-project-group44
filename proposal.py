import streamlit as st

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Project Proposal')

#----- Introduction ------

st.header('Introduction/Background')
st.markdown('''
<p class="justified-text">
In today's competitive retail landscape, customers have no dearth of options. 
Boosting sales hinges on strategies spanning effective product placement, efficient inventory management 
that ensures product availability, and compelling promotions to induce customers to buy more. 
Analyzing purchase history can reveal valuable insights that are often not intuitive, 
such as the surprising correlation between diapers and beer found in a case study.
</p> 
<p class="justified-text">
Instacart, a popular grocery ordering platform, has open-sourced their anonymized transactional data spanning 
3 million grocery orders from more than 200,000 users. The <a href="https://www.kaggle.com/competitions/instacart-market-basket-analysis/data" target="_blank">Dataset</a> is ideal for analysis as it 
provides user-specific purchase history and captures purchase sequence, re-ordered items, and order 
placement times. Previous work in this domain has utilized association rule algorithms and regression 
models. In this project, we will build on these approaches to identify frequently purchased items, 
re-ordering patterns, peak purchase times, and other trends.
</p>
''', unsafe_allow_html=True)


#----- Problem Definition ------
st.header("Problem Definition")
st.markdown('''
<p class="justified-text">
The objective of this project is to convert data given in the form of past customer orders 
to actionable knowledge/insights, which can be used to provide a better experience to the customers, 
while at the same time growing sales/revenue for the company.

We aim to achieve this by targeting two key objectives:
</p>
''', unsafe_allow_html=True)

st.markdown('''
<p class="justified-text">
1. <strong>Purchase Trend Discovery</strong> - Given a user and past user order history, identify purchasing patterns (e.g., clustering users with similar 
    purchasing behavior for product recommendation) through unsupervised learning algorithms. 
    This could be a useful input for product re-order prediction.
<br><br>
2. <strong>Product Re-order Prediction</strong> - Given a user, product, and user order history, predict if the user will re-order the given product in 
    their next order through supervised learning algorithms.
</p>
''', unsafe_allow_html=True)

st.markdown('''
<p class="justified-text">
Solving for these objectives would provide valuable insights, which can be used for product inventory 
management and improving customer experience (through bundled offers and effective product 
recommendation).
</p>
''', unsafe_allow_html=True)


#----- Methods ------
st.header("Methods")

st.subheader("Data Preprocessing")
st.markdown('''
<p class="justified-text">
1. <strong>Data Cleaning</strong> - Take care of null/non-existent values.
<br><br>
2. <strong>Data Transformation</strong> - The dataset contains tables on prior orders, 
    training and testing orders, aisle information, product information and department information. 
    To train models, we would need to join these tables to make the data usable.
<br><br>
3. <strong>Feature Engineering</strong> - As the dataset simply provides us with order information, 
            feature engineering is also essential for accuracy in the ultimate classification. 
            Examples of created features could be – if a customer is a weekly or monthly shopper, 
            customers most active day of week/time of day, etc. 
</p>
''', unsafe_allow_html=True)

st.subheader("Purchase Trend Discovery")
st.markdown('''
<p class="justified-text">
To identify purchasing patterns, we will leverage the aisle and department information to create customer 
            clusters. These clusters would signify the customer’s product purchase habits and would serve 
            as an additional feature to the classification models (T. Lim, 2021). </p>
''', unsafe_allow_html=True)

st.subheader("Product Re-order Prediction")
st.markdown('''
<p class="justified-text">
Treating the reorder prediction as a classification problem of whether a product exists in the future order
            or not, we will employ classification models like Gradient Boosted Trees and Neural Networks.
</p>
''', unsafe_allow_html=True)

#----- Potential Results ------

st.header('Potential Results')
st.markdown('''
<p class="justified-text">
We’ve chosen these specific metrics to directly measure the success of our goal of predicting potential basket orders. To that end, 
we will analyze the effectiveness of our clustering algorithms in grouping similar customer behaviors, involving a qualitative assessment 
of the clusters that we form. In order to predict product re-orders, we’ll use standard classification metrics like the accuracy (overall
average converging on desired result), precision (not much variation in outcomes from each other), confusion matrix, recall, and F1-score 
to evaluate the performance of our classification models. For purchase trend discovery, we’ll use clustering and assess them based on their 
interpretability. We hope to achieve a high F1-score to demonstrate our implementation’s predictive power for the product re-orders. We also
anticipate low rates of false positives and false negatives, which in a real-world implementation (say if we were bought out by Instacart) would
incur unnecessary inventory costs and hurt sales. We aim to identify meaningful customer clusters based on our analysis, driving insights for 
targeted marketing and product recommendations.
</p>
''', unsafe_allow_html=True)


#----- Group Gantt Chart ------
st.header("Group Gantt Chart")
st.image('./Gantt Chart.png')
st.markdown("[Link to Gantt Chart](https://docs.google.com/spreadsheets/d/1IR-oKyq-mOu6G73dS3AN7w5Xej8zgJ7I/edit?usp=sharing&ouid=110666483241984863961&rtpof=true&sd=true)")


#----- Contributions ------
st.header("Contributions")

st.markdown("""
    <style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 16px;
        text-align: center;
    }
    th, td {
        padding: 12px;
        border: 1px solid #ddd;
    }
    th {
        background-color: #343a40;;
        color: white;
        font-weight: bold;
        font-size: 18px;
        padding: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('''
<table>
    <tr>
        <th>Name</th>
        <th>Project Proposal</th>
    </tr>
    <tr>
        <td>Aparna Manoj</td>
        <td>Introduction<br>Presentation<br>Video Recording<br>Proposal Write-Up</td>
    </tr>
    <tr>
        <td>Benjamin Jiras</td>
        <td>Potential Results<br>Proposal Write-Up</td>
    </tr>
    <tr>
        <td>Nitin Chawla</td>
        <td>Project Research<br>Gantt Chart<br>Proposal Write-Up</td>
    </tr>
    <tr>
        <td>Sarika Singh</td>
        <td>Gantt Chart<br>Data Sourcing<br>Project Research<br>Proposal Write-Up</td>
    </tr>
    <tr>
        <td>Yashasvini Pratyaqsha</td>
        <td>Project Webpage Creation<br>Video Recording<br>Proposal Write-Up</td>
    </tr>
</table>
''', unsafe_allow_html=True)

#----- Proposal Video ------
st.header("Proposal Video")
st.markdown("[Link to Youtube Video](https://www.youtube.com/watch?v=MWJNMFsNEYY)")

#----- References ------
st.header("References")

st.markdown('''
<p class="justified-text">
Swoyer, S. (2016, November 15).  Beer and diapers: The impossible correlation. TDWI. 
https://tdwi.org/articles/2016/11/15/beer-and-diapers-impossible-correlation.aspx
</p>
''', unsafe_allow_html=True)

st.markdown('''
<p class="justified-text">
A. Bhargav, R. P. Mathur and M. Bhargav, "Market basket analysis using artificial neural network," International Conference for Convergence 
for Technology-2014, Pune, India, 2014, pp. 1-6, doi: 10.1109/I2CT.2014.7092091. https://ieeexplore.ieee.org/document/7092091.
</p>
''', unsafe_allow_html=True)

st.markdown('''
<p class="justified-text">
T. Lim, "K-Means Clustering-Based Market Basket Analysis: U.K. Online E-Commerce Retailer," 2021 International Conference on Information 
Technology (ICIT), Amman, Jordan, 2021, pp. 126-131, doi: 10.1109/ICIT52682.2021.9491703. 
</p>
''', unsafe_allow_html=True)

# st.markdown("[https://ieeexplore.ieee.org/document/7092091](https://ieeexplore.ieee.org/document/7092091)")

st.markdown('''
<p class="justified-text">
P. Sirohi, N. Singhal, P. Kumar and M. Alam, "Leveraging knowledge of Previous Baskets to Anticipate online Buyer Behaviour," 2023 
International Conference on Advances in Computation, Communication and Information Technology (ICAICCIT), Faridabad, India, 2023, pp. 968-973,
doi: 10.1109/ICAICCIT60255.2023.10465793.
</p>
''', unsafe_allow_html=True)


