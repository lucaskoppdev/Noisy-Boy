#Noisy-Boy
Python

##Descrição
Noisy-Boy é um assistente virtual em desenvolvimento, projetado para ser integrado a plataformas de mensagens como WhatsApp e Telegram via APIs. Ele utiliza técnicas de processamento de linguagem natural (PLN) para responder perguntas de usuários com base em um sistema de FAQ (Frequently Asked Questions).
Atualmente, o foco está no módulo de leitura e similaridade de FAQs, que converte um arquivo FAQ em JSON e usa o algoritmo de similaridade de cossenos do scikit-learn para encontrar respostas relevantes. Isso é ideal para cenários de suporte automatizado ou chatbots simples.
Nota: Este é um projeto de portfólio em fase inicial. Integrações com APIs de redes sociais e funcionalidades avançadas estão planejadas, mas ainda não implementadas. Contribuições são bem-vindas!
Funcionalidades Atuais

Leitura de FAQ: Converte FAQs em formato JSON para fácil acesso.
Vetoração TF-IDF: Usa scikit-learn para transformar textos em vetores e calcular similaridade de cossenos entre perguntas do usuário e entradas do FAQ.
Manipulação de Vetores de Usuário: Lida com vetores personalizados para contextos de conversa.

##Funcionalidades futuras:

Integração com APIs do WhatsApp (via Twilio ou oficial) e Telegram Bot API.
Suporte a respostas dinâmicas e aprendizado contínuo.
Interface web para configuração de FAQs.

##Requisitos

Python 3.8 ou superior.
Dependências listadas em requirements.txt (inclui scikit-learn para PLN).

##Instalação

Clone o repositório:textgit clone https://github.com/lucaskoppdev/Noisy-Boy.git
cd Noisy-Boy
Crie um ambiente virtual (opcional, mas recomendado):textpython -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:textpip install -r requirements.txt

##Uso
Por enquanto, o projeto é modular e pode ser testado via scripts Python. Exemplo básico:

Prepare um arquivo FAQ (ex: faq.xlsx com formato "Pergunta, Resposta").
Rode o módulo de leitura:Pythonpython3 read_faq.py

Para testar similaridade:Pythonpython3 tf_idf_vectorizer.py

Mais exemplos e documentação detalhada serão adicionados conforme o projeto avança.
Contribuição
Este projeto está aberto a contribuições! Siga estes passos:

Faça um fork do repositório.
Crie uma branch para sua feature: git checkout -b feature/nova-funcionalidade.
Commit suas mudanças: git commit -m 'Adiciona nova funcionalidade'.
Push para a branch: git push origin feature/nova-funcionalidade.
Abra um Pull Request.
