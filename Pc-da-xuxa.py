import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Orçamento de PC do perigo",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Cabeçalho fofo
st.markdown("# 🖥️ Loja do Perigo Gamer")
st.markdown("### 💸 Calculadora de Orçamento para Montagem de PC")
st.markdown("Onde o seu sonho de ter um Pc pode ser realizado por nós, basta ter o dinheiro")
st.markdown("Preencha o valor **disponível** e os preços de cada componente. O total será atualizado automaticamente.")

# Coluna para o orçamento disponível
col_budget, col_empty = st.columns([2, 3])
with col_budget:
    st.markdown('<div class="budget-card">', unsafe_allow_html=True)
    valor_disponivel = st.number_input(
        "💰 Valor disponível para a montagem (R$)",
        min_value=0.0,
        value=5000.0,
        step=100.0,
        format="%.2f",
        key="budget",
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 🛒 Digite o valor de cada peça (R$)")

# Lista de componentes (todos os exigidos)
componentes = {
    "placa_mae": "🔌 Placa-mãe",
    "memoria_ram": "🧠 Memória RAM",
    "processador": "⚡ Processador",
    "placa_video": "🎮 Placa de vídeo",
    "armazenamento": "💾 Armazenamento (SSD/HD)",
    "fonte": "🔋 Fonte de alimentação",
    "gabinete": "📦 Gabinete",
    "cooler": "❄️ Cooler",
    "monitor": "🖥️ Monitor",
    "teclado_mouse": "⌨️🖱️ Teclado + Mouse",
    "sistema_operacional": "💿 Sistema operacional",
    "outros_perifericos": "🎧 Outros periféricos",
}

# Organizar em 3 colunas para ficar compacto
col1, col2, col3 = st.columns(3)

# Dicionário para armazenar os valores
valores = {}

# Distribuir os componentes nas colunas
items = list(componentes.items())
for idx, (key, label) in enumerate(items):
    target_col = col1 if idx % 3 == 0 else (col2 if idx % 3 == 1 else col3)
    with target_col:
        valores[key] = st.number_input(
            label,
            min_value=0.0,
            value=0.0,
            step=50.0,
            format="%.2f",
            key=key,
        )

# Calcular total
total = sum(valores.values())

# Mostrar resultados e comparação com orçamento disponível
st.markdown("---")
st.subheader("📊 Resumo do Orçamento")

col_total, col_restante, col_status = st.columns(3)

with col_total:
    st.metric("💰 Total dos componentes", f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col_restante:
    restante = valor_disponivel - total
    cor_restante = "normal" if restante >= 0 else "inverse"
    st.metric(
        "💵 Saldo (orçamento - total)",
        f"R$ {restante:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        delta_color=cor_restante,
    )

with col_status:
    if total > valor_disponivel:
        st.markdown(
            '<div class="warning" style="padding: 0.8rem; border-radius: 15px;">'
            '<h4 style="margin: 0; color: #d32f2f;">⚠️ ATENÇÃO</h4>'
            f'<p style="margin: 0;">Você excedeu o orçamento em <strong>R$ {(total - valor_disponivel):,.2f}</strong>!</p>'
            '</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="success" style="padding: 0.8rem; border-radius: 15px;">'
            '<h4 style="margin: 0; color: #2e7d32;">✅ DENTRO DO ORÇAMENTO</h4>'
            f'<p style="margin: 0;">Sobrou <strong>R$ {restante:,.2f}</strong> para outros gastos ou upgrades.</p>'
            '</div>',
            unsafe_allow_html=True,
        )

# Barra de progresso do orçamento
if valor_disponivel > 0:
    percent = min(100, (total / valor_disponivel) * 100)
    st.progress(percent / 100)
    st.caption(f"📈 {percent:.1f}% do orçamento utilizado")
else:
    st.warning("Defina um orçamento disponível maior que zero para ver a proporção.")

# Rodapé fofinho
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.8rem;'>🐣 Feito com carinho para seu sonho gamer • Ajuste os valores e veja o total em tempo real</p>",
    unsafe_allow_html=True,
)