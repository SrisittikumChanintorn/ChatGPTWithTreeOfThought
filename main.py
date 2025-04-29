import os
from openai import OpenAI
from tree_of_thought import *

# Set the API key
OPENAI_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

# Get the permission from the owner of the API key to use it.
LLM1 = OpenAI(api_key=OPENAI_API_KEY) 

# Define the prompt for the first model ( as a root of tree of thought)
QUERY = ""

# Define the model and max token for the models
SLM_MODEL = "gpt-3.5-turbo-16k"



# Branching the query into sub-branches
response_domestic_market_competition = domestic_market_competition(query=QUERY, llm=LLM1, model_name=SLM_MODEL)
# Sub-branches of domestic market competition
response_price_undercutting = price_undercutting(query=response_domestic_market_competition, llm=LLM1, model_name=SLM_MODEL)
response_market_share_losses = market_share_losses(query=response_domestic_market_competition, llm=LLM1, model_name=SLM_MODEL)
response_response_domestic_market_competition = innovation_and_quality_improvement(query=response_domestic_market_competition, llm=LLM1, model_name=SLM_MODEL)

# Branching the query into sub-branches
response_consumer_behavior = consumer_behavior(query=QUERY, llm=LLM1, model_name=SLM_MODEL)
# Sub-branches of consumer behavior
response_demand_for_cheaper_goods = demand_for_cheaper_goods(query=response_consumer_behavior, llm=LLM1, model_name=SLM_MODEL)
response_disposable_income_and_spending_patterns = disposable_income_and_spending_patterns(query=response_consumer_behavior, llm=LLM1, model_name=SLM_MODEL)
response_brand_layalty_and_perception = brand_layalty_and_perception(query=response_consumer_behavior, llm=LLM1, model_name=SLM_MODEL)


# If the Developer consider any of the Sub-branches answer not good enough, they decide to manually remove the Sub-branches.
final_query = response_price_undercutting + \
              response_market_share_losses + \
              response_response_domestic_market_competition + \
              response_demand_for_cheaper_goods + \
              response_disposable_income_and_spending_patterns + \
              response_brand_layalty_and_perception

# Make the final conclusion based on the sub-branches
final_response = make_conclusion(query=final_query, llm=LLM1, model_name=SLM_MODEL)

# Print the final response
print(final_response)
