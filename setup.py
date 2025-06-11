from setuptools import setup, find_packages

setup(
    name="aipo_agent_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "slack-bolt>=1.17.0",
        "slack-sdk>=3.19.5",
        "python-dotenv>=1.0.0",
        "openai>=1.3.0",
        "requests>=2.28.2",
        "aiohttp>=3.8.4",
        "langchain>=0.0.267",
        "langchain-openai>=0.0.2",
        "fastapi>=0.100.0",
        "uvicorn>=0.23.2",
    ],
    python_requires=">=3.8",
    author="AipoLabs Intern",
    author_email="intern@aipolabs.com",
    description="A Slack bot with agentic capabilities",
    keywords="slack, bot, llm, agentic, openai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 