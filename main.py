import os
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

# Configurar variáveis de ambiente
os.environ["OPENAI_API_KEY"] = "SUA CHAVE DE API"

class BusinessAutomationCrew:
    def __init__(self, business_type):
        self.business_type = business_type
        self.agents = CustomAgents()
        self.tasks = CustomTasks()

    def run(self):
        agents = {
            "market_analyst": self.agents.create_agent("Market Analyst"),
            "marketing_strategist": self.agents.create_agent("Marketing Strategist")
        }

        tasks = {
            "market_analysis": self.tasks.create_task(agents["market_analyst"], self.business_type, "market_analysis"),
            "marketing_strategy": self.tasks.create_task(agents["marketing_strategist"], self.business_type, "marketing_strategy"),
            "integration": self.tasks.create_task(agents["marketing_strategist"], self.business_type, "integration")
        }

        crew = Crew(
            agents=list(agents.values()),
            tasks=list(tasks.values()),
            verbose=False
        )

        return crew.kickoff()

if __name__ == "__main__":
    print("Bem-vindo à Configuração da Equipe de Automação de Negócios")
    print("------------------------------------------------")
    business_type = input("Que tipo de negócio você deseja construir hoje? ").strip()

    automation_crew = BusinessAutomationCrew(business_type)
    business_plan = automation_crew.run()

    print("\n\n########################")
    print("## Aqui estão os resultados do seu projeto de automação de negócios:")
    print("########################\n")
    print(business_plan)
