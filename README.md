US HOUSING MARKET DYNAMICS

A home is usually the expensive purchase a person makes in one’s lifetime. Ensuring users have
sufficient information about their interested market is paramount. Housing market refers to the type,
cost, supply/demand of homes in a specific region. Housing markets usually experience substantial
short-term price change momentum, supply/demand volatility due to various factors. Market
dynamics can be analyzed using metrics & trends observed over time. Providing insights from market
dynamics data aids buyers/sellers to make better & informed decisions.

Problem Statement:

● Analyze metrics at state & county level provide your insights in an hierarchical fashion.
● Analyze & infer trends, seasonality, cyclic nature of metrics provided.

Approach

1] Extractes the data from source and converted the .tsv file. Performed a transformation of removing the rows that contained null values in any of the columns using python pandas library.
  
2] To build an interactive dashboard i preferred to use Tableau tool for the visualizations such as time line charts and score cards from the inference of all those kpi listed and create a dashboard. This would eliminate the need for an external database for now as the data file can be directly used in tableau.
    
3] That Tableau dahboard can be embedded into VueJS framework using Tableau Javascriot API. 
