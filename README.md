# RAG

## 项目简介
本项目是一个基于检索增强生成 (RAG) 技术的问答系统实现。其核心目标是通过结合私有知识库与大语言模型 (LLM)，解决通用模型在特定领域知识缺失及信息滞后的问题。系统通过提取、索引和检索本地文档，为模型提供可靠的上下文支撑，确保输出结果的准确性与专业性。

## 核心功能
* **文档解析与加载**：支持多种格式（如 PDF, Markdown, TXT）的自动化数据导入。
* **文本切分策略**：内置语义块切分逻辑，优化上下文的长短匹配。
* **向量化存储**：集成向量数据库（如 Chroma / FAISS），支持高效的相似度检索。
* **检索增强生成**：通过 Prompt Engineering 将检索结果整合至 LLM 生成流程。
* **模块化设计**：解耦数据层与模型层，方便更换不同的 Embedding 模型或 LLM 接口。

## 技术栈
* **核心框架**：Python, LangChain / LlamaIndex
* **大语言模型**：OpenAI GPT / Claude / Ollama 本地模型
* **向量数据库**：Chroma / FAISS / Qdrant
* **依赖管理**：Pip / Poetry

## 快速开始

### 1. 环境准备
确保已安装 Python 3.9+ 环境，克隆仓库至本地：
```bash
git clone https://github.com/Seungberry/RAG.git
cd RAG
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置参数
在根目录新建 .env 文件并配置必要的环境变量（如 API 密钥）：
```env
OPENAI_API_KEY=your_api_key
VECTOR_DB_PATH=./data/vector_store
```

### 4. 运行
执行主程序以启动索引构建或查询服务：
```bash
python main.py
```

## 项目结构
* **data/**：存放原始文档与知识库。
* **models/**：存放本地模型或提示词模板。
* **src/**：核心源代码（包含加载、索引、检索及生成模块）。
* **tests/**：单元测试与性能评估脚本。
