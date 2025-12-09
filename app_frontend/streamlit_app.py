#ALGUNS DADOS QUE DEVEM EXISTIR NO INPUT DO USUARIO:

#   age: int, #idade
#   sex: Literal[0, 1] #sexo -> recebe apenas [0 ou 1]
#   cp: #chest pain type (são 4 valores, de 0 a 4) -> recebe apenas [0, 1, 2 ou 4]
#  trestbps:  int,  #resting blood pressure (pressão arterial em repouso) 
#  chol:  int, #serum cholestoral in mg/dl (colesterol sérico em mg/dl)
#  fbs: #fasting blood sugar > 120 mg/dl (fasting blood sugar > 120 mg/dl) -> recebe apenas [0, 1]
# restecg: #resting electrocardiographic results (values 0,1,2) (resultados do eletrocardiograma em repouso) -> recebe apenas [0, 1 ou 2]
#  thalach: int,  #maximum heart rate achieved (frequência cardíaca máxima atingida)
#  exang:  #exercise induced angina (angina induzida por exercício) -> recebe apenas [0, 1]
# oldpeak: float , #ST depression induced by exercise relative to rest (depressão do segmento ST induzida pelo exercício em relação ao repouso)
# slope: the slope of the peak exercise ST segment (inclinação do segmento ST no pico do exercício) -> recebe apenas [0, 1 ou 2]
# ca: number of major vessels (0-3) colored by flourosopy (número de vasos principais (0–3) coloridos por fluoroscopia) -> recebe apenas [0, 1, 2 ou 3]
#  thal: thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (thal: 0 = normal; 1 = defeito fixo; 2 = defeito reversível) -> recebe apenas [0, 1, 2 ou 3]
#
#TODOS OS DADOS ACIMA FORAM RETIRADOS DO CSV DO NOSSO MODELO, SÃO ESSES OS DADOS Q A I.A ESPERA NO INPUT
#CASO DUVIDAS SOBRE OS DADOS ACIMA, CONSULTEM EM: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset?resource=download
#OU https://colab.research.google.com/drive/1Yq_Cbc8-KGwZbna0ByTsFqSQiTOK3oxG?usp=sharing (vai precisar configurar primeiro)


import streamlit as st
import requests

# Configuração visual da página
st.set_page_config(
    page_title="Diagnóstico Cardíaco IA",
    page_icon="💓",
    layout="wide" # Layout amplo para ficar mais bonito
)

# Título e Introdução
st.title("💓 Diagnóstico Assistido por Inteligência Artificial")
st.markdown("""
**Instruções:** Este sistema utiliza IA para calcular a probabilidade de doença cardíaca. 
Preencha os dados abaixo com base nos exames do paciente. Se tiver dúvida, passe o mouse sobre o ícone (?) para ajuda.
""")

st.divider()

# Formulário Principal
with st.form("ficha_medica"):
    st.subheader("📋 Dados Pessoais e Sintomas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Idade", min_value=1, max_value=120, value=40)
        
        # Traduzindo: Sexo
        sex_display = st.radio("Sexo Biológico", ["Masculino", "Feminino"], horizontal=True)
        sex = 1 if sex_display == "Masculino" else 0

    with col2:
        # Traduzindo: CP (Chest Pain)
        cp_labels = {
            0: "Angina Típica (Dor forte/aperto)",
            1: "Angina Atípica (Desconforto)",
            2: "Dor não-cardíaca (Outra origem)",
            3: "Assintomático (Sem dor)"
        }
        cp = st.selectbox(
            "Você sente dor no peito?", 
            options=[0, 1, 2, 3], 
            format_func=lambda x: cp_labels[x]
        )

    with col3:
        # Traduzindo: Exang (Angina por exercício)
        exang_display = st.radio("Sente dor ao fazer esforço físico?", ["Não", "Sim"], horizontal=True)
        exang = 1 if exang_display == "Sim" else 0

    st.subheader("🩺 Resultados de Exames Clínicos")
    col4, col5 = st.columns(2)

    with col4:
        # Traduzindo: Trestbps e Chol
        trestbps = st.slider("Pressão Arterial em Repouso (mmHg)", 90, 200, 120, help="Valor da pressão sistólica (o número maior da medição). Ex: Se 12/8, use 120.")
        chol = st.slider("Colesterol Total (mg/dl)", 100, 600, 200, help="Nível de colesterol no sangue.")
        
        # Traduzindo: FBS (Glicemia)
        fbs_display = st.checkbox("A Glicose (Açúcar) em jejum está alta? (> 120 mg/dl)")
        fbs = 1 if fbs_display else 0

    with col5:
        # Traduzindo: RestECG
        restecg_labels = {
            0: "Normal",
            1: "Com anormalidades (Onda ST-T)",
            2: "Hipertrofia Ventricular (Grave)"
        }
        restecg = st.selectbox(
            "Resultado do Eletrocardiograma (Repouso)", 
            options=[0, 1, 2], 
            format_func=lambda x: restecg_labels[x]
        )
        
        thalach = st.number_input("Frequência Cardíaca Máxima (Batimentos/min)", 60, 220, 150, help="Máximo atingido durante teste de esforço.")

    st.subheader("🔬 Detalhes Técnicos (Para uso médico)")
    with st.expander("Clique para preencher dados avançados do laudo"):
        col6, col7 = st.columns(2)
        with col6:
            oldpeak = st.number_input("Depressão ST (Oldpeak)", 0.0, 10.0, 0.0, step=0.1)
            slope_labels = {0: "Inclinando p/ Cima", 1: "Plano", 2: "Inclinando p/ Baixo"}
            slope = st.selectbox("Inclinação ST (Slope)", [0, 1, 2], format_func=lambda x: slope_labels[x])
        with col7:
            ca = st.selectbox("Vasos coloridos na Fluoroscopia (0-4)", [0, 1, 2, 3, 4])
            thal_labels = {0: "Erro/Nulo", 1: "Normal", 2: "Defeito Fixo", 3: "Defeito Reversível"}
            thal = st.selectbox("Talassemia (Thal)", [0, 1, 2, 3], format_func=lambda x: thal_labels[x])

    # Botão Principal
    submit = st.form_submit_button("🔍 ANALISAR PACIENTE", use_container_width=True, type="primary")

# Lógica de Envio
if submit:
    api_url = "http://localhost:8000/riskpredict"
    payload = {
        "age": int(age), "sex": sex, "cp": cp, "trestbps": int(trestbps),
        "chol": int(chol), "fbs": fbs, "restecg": restecg, "thalach": int(thalach),
        "exang": exang, "oldpeak": float(oldpeak), "slope": slope, "ca": ca, "thal": thal
    }

    try:
        with st.spinner("A Inteligência Artificial está analisando os dados..."):
            response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            resultado = data['predicted_class']
            confianca = data['confidence'] * 100
            
            st.success("Análise Concluída!")
            
            # Mostrando o resultado com destaque
            col_res1, col_res2 = st.columns([1, 2])
            with col_res1:
                if "Alto Risco" in resultado or "Possível Doença" in resultado:
                    st.metric(label="Diagnóstico", value="ALTO RISCO", delta="-Cuidado", delta_color="inverse")
                else:
                    st.metric(label="Diagnóstico", value="BAIXO RISCO", delta="Saudável")
            
            with col_res2:
                st.progress(confianca / 100)
                st.caption(f"Certeza do Modelo: {confianca:.1f}%")
                
        else:
            st.error(f"Erro no servidor: {response.text}")
    except:
        st.warning("Não foi possível conectar ao sistema. Verifique se o 'api.py' está rodando.")