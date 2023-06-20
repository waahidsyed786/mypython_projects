#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import openai

# openai.api_key = "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"
openai.api_key ="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"

completion = openai.ChatCompletion.create( model="gpt-3.5-turbo",  messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."} ] )
# response = openai.Completion.create( model ="text-davinci-003", prompt =chat_entry.get(), temperature = 0, max_tokens = 4000, top_p =1,frequency_penalty = 0.0, presence_penalty = 0.0)
print(completion.choices[0].message.content)
# print(response["choices"][0]["text"].script())

