import pandas as pd
import configparser
from datetime import datetime as dt
from datetime import timedelta


rent = 10000
coef = 0.7


def profit_calculation(profit, rent=rent, coef=coef):
    """
    Доход ОСА и ЦКБ
    """
    if profit >= 0:
        if (profit * coef) % 50 == 0:
            ckb = profit * coef // 50 * 50
            osa = profit - profit * coef // 50 * 50
        else:
            ckb = (profit * coef + 50) // 50 * 50
            osa = profit - (profit * coef + 50) // 50 * 50
    elif -rent <= profit < 0:
        if (profit * coef) % 50 == 0:
            # Аренду убираем, оставляем только прибыль. Аренда rent.
            ckb = ((profit + rent) * coef) // 50 * 50
            osa = (profit + rent) - (profit + rent) * coef // 50 * 50
        else:
            ckb = ((profit + rent) * coef + 50) // 50 * 50
            osa = (profit + rent) - ((profit + rent) * coef + 50) // 50 * 50
    else:
        ckb = 0
        osa = 0
    return ckb, osa


def rent_calculation(profit, rent=rent):
    if profit > 0:
        return rent / 2
    else:
        return 0


def main():
    # input_filepath = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSq9eXRVWlIHj1UxPk1gwhfwCpEI490C7xbS9BY24-hQM1HQOhixFBIZcQkCWpEHhaA24iKKNZMCi-G/pub?gid=37&single=true&output=csv'
    config = configparser.ConfigParser()
    config.read('Report_DK/config.ini')
    config.sections()

    df = pd.read_csv(config['PATH']['Input_filepath'])
    df['Сумма'] = df['Сумма'].apply(lambda x: str(x).replace(' ', ''))
    df['Сумма'] = df['Сумма'].apply(lambda x: str(x).replace('р.', ''))
    df['Сумма'] = df['Сумма'].apply(lambda x: str(x).replace(u'\xa0', ''))
    df['Сумма'] = df['Сумма'].apply(lambda x: str(x).replace(',', '.'))
    df['Сумма'] = df['Сумма'].astype(float)
    profit_tmp = df['Сумма'].sum()
    df_debts = df.loc[df['Долг'] == 'сергей']
    # Долги ДК -> ОСА
    debt_dk_to_osa = df_debts[df_debts['Категория'] != 'улучшения']['Сумма'].sum()
    # Все улучшения за месяц
    upgrade_all = df[df['Категория'] == 'улучшения']['Сумма'].sum()
    # Прибыль/убыток с учетом трат на улучшения
    profit = profit_tmp - upgrade_all
    # Улучшения за счет ОСА в месяц
    upgrade_osa = df_debts[df_debts['Категория'] == 'улучшения']['Сумма'].sum()
    # Улучшения за счет ЦКБ в месяц
    upgrade_ckb = upgrade_all - upgrade_osa
    # Улучшения 50/50: ЦКБ -> ОСА
    upgrade_debts = upgrade_osa / 2 - (upgrade_osa / 2 % 50) - upgrade_ckb / 2 - (upgrade_ckb / 2 % 50)

    report_period = dt.now().date()
    report_period = report_period-timedelta(days=report_period.day)
    text = ''
    text += f"Итоги {report_period.strftime('%b %Y')}г.:\n"
    text += f'Аренда: {rent_calculation(profit)}р. ЦКБ, {rent_calculation(profit)}р. ОСА\n'
    text += f"Чистая прибыль/убыток: {profit}р. ЦКБ {profit_calculation(profit)[0]}р. ОСА {profit_calculation(profit)[1]}р.\n-----\n"
    text += f"Долги ДК -> ОСА {-debt_dk_to_osa}р.\n"

    for i, row in df_debts[~(df_debts['Категория']=='улучшения')].iterrows():
        if df_debts[~(df_debts['Категория']=='улучшения')].shape[0]!=0:
            row_without_line_break = str(row.values).replace('\n', '')
            text += f"{i} {row_without_line_break}\n"

    text +='-----\n'
    # Итог по улучшениям
    if upgrade_osa <= upgrade_ckb:
       text += f'Улучшения 50/50: ЦКБ -> ОСА {-upgrade_debts}р.\n'
       upgrade=-upgrade_debts
    else:
        text += f'Улучшения 50/50: ОСА -> ЦКБ {upgrade_debts}р.\n'
        upgrade=upgrade_debts

    for i, row in df_debts[(df_debts['Категория']=='улучшения')].iterrows():
        if df_debts[(df_debts['Категория']=='улучшения')].shape[0]!=0:
            row_without_line_break = str(row.values).replace('\n', '')
            text += f"{i} {row_without_line_break}\n"

    text +='-----\n'
    text += f"Итого с ЦКБ -> ОСА {rent_calculation(profit)+profit_calculation(profit)[1]-debt_dk_to_osa+upgrade}р."
    for el in text.split('\n'):
        print(el)


if __name__ == '__main__':
    main()
