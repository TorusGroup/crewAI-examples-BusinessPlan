from crewai import Task

class CustomTasks:
    def __init__(self):
        pass

    def create_task(self, agent, business_type, task_type):
        task_descriptions = {
            "market_analysis": (
                f"Realizar uma análise de mercado aprofundada para um(a) {business_type}, focando em entender o tamanho do mercado, "
                f"identificar tendências atuais, analisar estratégias dos concorrentes e avaliar os dados demográficos dos clientes. "
                f"Avaliar o ambiente regulatório e possíveis barreiras à entrada que possam afetar o lançamento e a sustentabilidade do negócio."
            ),
            "marketing_strategy": (
                f"Desenvolver uma estratégia de marketing detalhada para um(a) {business_type} utilizando os insights obtidos na "
                f"análise de mercado. Esta estratégia deve delinear os canais de marketing direcionados, planos de engajamento do cliente, "
                f"posicionamento da marca e táticas promocionais. Incluir uma previsão orçamentária e impactos esperados na penetração de mercado."
            ),
            "integration": (
                f"Criar um plano abrangente de lançamento de 30 dias para um(a) {business_type}, delineando atividades diárias, "
                f"objetivos estratégicos e requisitos operacionais. Garantir que o plano inclua um cronograma para cada fase "
                f"do lançamento, identifique marcos chave e descreva a alocação de recursos para estabelecer um roteiro para "
                f"uma entrada bem-sucedida no mercado."
            )
        }

        expected_outputs = {
            "market_analysis": (
                f"Relatório detalhado sobre as condições de mercado para um(a) {business_type}, incluindo dados sobre tamanho de mercado, potencial de crescimento, "
                f"principais concorrentes e perfis de clientes. O relatório também deve fornecer insights acionáveis e recomendações estratégicas."
            ),
            "marketing_strategy": (
                f"Manual abrangente de marketing para um(a) {business_type}, detalhando todos os esforços de marketing, estratégias de canal, "
                f"e planos de comunicação, juntamente com um cronograma e resultados projetados. O manual deve estar alinhado com os objetivos gerais do negócio "
                f"e as metas de aquisição de clientes."
            ),
            "integration": (
                f"Um plano de lançamento totalmente articulado de 30 dias para um(a) {business_type} com itens de ação claros, responsabilidades, "
                f"e pontos de verificação. O plano deve cobrir todas as preparações necessárias para que o negócio inicie suas operações "
                f"sem problemas e atinja uma tração inicial."
            )
        }

        return Task(
            description=task_descriptions[task_type],
            agent=agent,
            expected_output=expected_outputs[task_type]
        )
