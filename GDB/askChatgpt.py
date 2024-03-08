import openai
import sys

# 替换成您的 OpenAI API 密钥
api_key = "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"

# 设置 OpenAI API 密钥
openai.api_key = api_key

def chat_with_gpt(question):
    # 向 ChatGPT 提问
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用适合对话的引擎
        prompt=question,  # 用户提供的问题
        max_tokens=1500,  # 最大生成的令牌数
        temperature=1,  # 温度参数，控制生成文本的创造性
    )

    # 返回 ChatGPT 的回答
    return response.choices[0].text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请提供一个问题作为参数。")
    else:
        question = sys.argv[1]
        answer = chat_with_gpt(question)
        print("ChatGPT：", answer)
