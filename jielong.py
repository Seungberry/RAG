from langchain.prompts.chat import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate, 
    ChatPromptTemplate
)
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. 配置大语言模型
chat_model = ChatOpenAI(
    openai_api_key="ollama", # 本地模型 API Key 通常设为 ollama 或 EMPTY [cite: 13, 14, 26]
    base_url="http://localhost:11434/v1", # Ollama 默认端口 [cite: 14, 26]
    model="qwen2.5:0.5b",
    temperature=0.7 # 适当增加随机性以生成更多样的成语 
)

# 2. 定义成语接龙的提示词模板 
system_template = "你是一个成语接龙高手。请根据用户提供的成语，接出一个新的成语。要求：新成语的首字必须是前一个成语的尾字（音同即可）。只输出成语本身，不要有其他解释。"
system_message = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{idiom}"
human_message = HumanMessagePromptTemplate.from_template(human_template)

# 将模板组合成对话提示词 
chat_prompt = ChatPromptTemplate.from_messages([
    system_message,
    human_message,
])

# 3. 创建 RunnableSequence 链
# 链的流程：输入成语 -> 格式化 Prompt -> 输入 LLM -> 解析为字符串输出
chain = chat_prompt | chat_model | StrOutputParser()

# 4. 测试成语接龙
input_idiom = "胸有成竹"
response = chain.invoke({"idiom": input_idiom})

print(f"用户输入: {input_idiom}")
print(f"机器人接龙: {response}")