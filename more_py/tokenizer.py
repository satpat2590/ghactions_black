import tiktoken

tokenizer = tiktoken.get_encoding("cl100k_base")

long_text = """
    Gerald went to the store to buy ice cream and then feed his kids the ice cream but by the time he came home, the ice cream melted 
    and now Gerald wants revenge against the ice cream store even though it was his fault that his car was 85 degrees during the 1 hour drive home, so 
    what can Gerald possibly do? 

    To be continued on: Gerald vs US Supreme Court... 
"""

tokens = tokenizer.encode(long_text)

single_tokens_from_id = [tokenizer.decode_single_token_bytes(x) for x in tokens]

print(tokens)
print(single_tokens_from_id)
