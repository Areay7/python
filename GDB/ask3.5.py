import argparse
import openai
import os

# 将你的API密钥替换成你自己的密钥
api_key = "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"

command = "export https_proxy=http://127.0.0.1:33210 \
http_proxy=http://127.0.0.1:33210 \
all_proxy=socks5://127.0.0.1:33211 "

def chat_with_gpt3(prompt):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用GPT-3.5 Turbo模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message['content']

if __name__ == "__main__":
    os.system(command)
    parser = argparse.ArgumentParser(description="Chat with GPT-3.5 Turbo in the terminal")
    parser.add_argument("prompt", type=str, help="User's input prompt")
    args = parser.parse_args()

    response = chat_with_gpt3(args.prompt)
    print("ChatGPT3.5 Turbo:", response)
