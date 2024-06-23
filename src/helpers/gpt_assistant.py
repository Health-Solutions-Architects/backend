import openai
import orjson

PROMPT_TRIAGEM = """Você irá realizar classificação de risco do paciente, de acordo com o sistema de triagem de Manchester.
Você irá responder apenas com a classificação de risco, baseados na protocolo de Manchester e no JSON abaixo.
{ 
    "vermelho": { "nível": 1, "classificação": "emergente", "tempo": "imediato" }, 
    "laranja": { "nível": 2, "classificação": "muito urgente", "tempo": "10 minutos" }, 
    "amarelo": { "nível": 3, "classificação": "urgente", "tempo": "60 minutos" }, 
    "verde": { "nível": 4, "classificação": "pouco urgente", "tempo": "120 minutos" }, 
    "azul": { "nível": 5, "classificação": "não urgente", "tempo": "240 minutos" } 
}
Responda no formato JSON: 
{
    "classificacao": "(Urgente, Pouco Urgente, etc)", 
    "cor": "Cor da classificacao",
    "nivel": "Nivel da classificacao",
    "descricao": "Descricao para o prontuario"
}
"""


def get_assistant_classification(dados: dict) -> dict | None:
    user_message = f"""Nome: {dados['nome']} Peso: {dados['peso']} Altura: {dados['altura']} Sintomas: {dados['sintomas']}"""
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": PROMPT_TRIAGEM},
            {"role": "user", "content": user_message}
        ]
    )
    try:
        content = response.choices[0].message.content
        return orjson.loads(content)
    except Exception as e:
        print(e)
        return None
