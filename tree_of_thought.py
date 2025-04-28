# make domestic market competition perspective from branch function
def domestic_market_competition(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Domestic Market Competition.'"""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result



# make price undercutting perspective from sub-branch function
def price_undercutting(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Price Undercutting.'
                        Effect on Thai producers and small businesses.
                        Sectors most vulnerable to Chinese price competition."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model= model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make market share losses perspective from sub-branch function
def market_share_losses(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Market Share Losses.'
                        Displacement of local products by cheaper Chinese alternatives.
                        Survival strategies for Thai businesses."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make innovation and quality improvement perspective from sub-branch function
def innovation_and_quality_improvement(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Innovation and Quality Improvement.'
                        Need for innovation in Thai industries to compete on quality rather than price.
                        Investments in technology and R&D by Thai companies."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make consumer behavior perspective from sub-branch function
def consumer_behavior(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Consumer Behavior.'"""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make demand for cheaper goods perspective from sub-branch function
def demand_for_cheaper_goods(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Demand for Cheaper Goods.'
                        Shift in consumer preferences toward lower-cost Chinese products.
                        Impact on local brands and traditional products."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make disposable income and spending patterns perspective from sub-branch function
def disposable_income_and_spending_patterns(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Disposable Income and Spending Patterns.'
                        Increase in consumer spending power due to lower prices.
                        Changes in household consumption patterns."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result


# make brand loyalty and perception perspective from sub-branch function 
def brand_layalty_and_perception(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, respond from the perspective of 'Brand Loyalty and Perception.'
                        Erosion of brand loyalty for Thai products.
                        Perception of Chinese goods in the Thai market."""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result

# make conclusion function
def make_conclusion(query, llm, model_name):

    full_query = f"\nUser: {query}"

    system_content = """Based on the user's input, draw the best conclusion"""

    messages = [
        {"role": "system", "content": f"{system_content}"},
        {"role": "user", "content": full_query}
    ]

    chain1 = llm.chat.completions.create(
        model=model_name,
        messages=messages
    )

    result = chain1.choices[0].message.content
    return result