import streamlit as st
import pandas as pd
from financing.src.domain.utils.price_reports import PriceReport


def main():
    st.title('Simulador de Financiamento SAC')

    valor_imovel = st.number_input(
        label='Valor do Imóvel',
        min_value=1000.0,
        max_value=500000000.0,
        value=50000.0,
        step=10000.0,
    )

    taxa_juros = st.number_input('Taxa de Juros mensal (%)', min_value=0.01, max_value=100.0, step=0.1)
    parcelas = st.number_input('Parcelas', value=48, min_value=1, max_value=420, step=12)

    if st.button('Simular'):
        st.write("Os valores estimados são:")
        complete_report = PriceReport.complete_report(valor_imovel, parcelas, taxa_juros)
        complete_report.append(PriceReport.simple_report(valor_imovel, parcelas, taxa_juros))
        cols = ['N°', 'Prestação', 'Juros', 'Amortização', 'Saldo devedor']
        df_complete = pd.DataFrame(complete_report, columns=cols)
        st.write(df_complete)


if __name__ == '__main__':
    main()
