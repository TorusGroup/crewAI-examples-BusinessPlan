from crewai import Agent
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        self.gpt_model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def create_agent(self, role):
        descriptions = {
            "Market Analyst": "Eu me especializo em pesquisa e análise de mercado, fornecendo insights que são cruciais para o planejamento estratégico.",
            "Marketing Strategist": "Eu desenvolvo estratégias de marketing que efetivamente atingem os principais segmentos demográficos e maximizam a penetração no mercado."
        }

        return Agent(
            role=role,
            backstory=descriptions[role],
            goal=f"Desenvolver insights detalhados e acionáveis para {role}.",
            verbose=True,
            llm=self.gpt_model
        )
