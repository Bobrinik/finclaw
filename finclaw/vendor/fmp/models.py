import pandas as pd

balance_sheet_normalized_names = {
    'date': 'date',
    'symbol': 'symbol',
    'reportedCurrency': 'reported_currency',
    'cik': 'cik',
    'fillingDate': 'filling_date',
    'acceptedDate': 'accepted_date',
    'calendarYear': 'calendar_year',
    'period': 'period',
    'cashAndCashEquivalents': 'cash_and_cash_equivalents',
    'shortTermInvestments': 'short_term_investments',
    'cashAndShortTermInvestments': 'cash_and_short_term_investments',
    'netReceivables': 'net_receivables',
    'inventory': 'inventory',
    'otherCurrentAssets': 'other_current_assets',
    'totalCurrentAssets': 'total_current_assets',
    'propertyPlantEquipmentNet': 'property_plant_equipment_net',
    'goodwill': 'goodwill',
    'intangibleAssets': 'intangible_assets',
    'goodwillAndIntangibleAssets': 'goodwill_and_intangible_assets',
    'longTermInvestments': 'long_term_investments',
    'taxAssets': 'tax_assets',
    'otherNonCurrentAssets': 'other_non_current_assets',
    'totalNonCurrentAssets': 'total_non_current_assets',
    'otherAssets': 'other_assets',
    'totalAssets': 'total_assets',
    'accountPayables': 'account_payables',
    'shortTermDebt': 'short_term_debt',
    'taxPayables': 'tax_payables',
    'deferredRevenue': 'deferred_revenue',
    'otherCurrentLiabilities': 'other_current_liabilities',
    'totalCurrentLiabilities': 'total_current_liabilities',
    'longTermDebt': 'long_term_debt',
    'deferredRevenueNonCurrent': 'deferred_revenue_non_current',
    'deferredTaxLiabilitiesNonCurrent': 'deferred_tax_liabilities_non_current',
    'otherNonCurrentLiabilities': 'other_non_current_liabilities',
    'totalNonCurrentLiabilities': 'total_non_current_liabilities',
    'otherLiabilities': 'other_liabilities',
    'capitalLeaseObligations': 'capital_lease_obligations',
    'totalLiabilities': 'total_liabilities',
    'preferredStock': 'preferred_stock',
    'commonStock': 'common_stock',
    'retainedEarnings': 'retained_earnings',
    'accumulatedOtherComprehensiveIncomeLoss': 'accumulated_other_comprehensive_income_loss',
    'othertotalStockholdersEquity': 'othertotal_stockholders_equity',
    'totalStockholdersEquity': 'total_stockholders_equity',
    'totalEquity': 'total_equity',
    'totalLiabilitiesAndStockholdersEquity': 'total_liabilities_and_stockholders_equity',
    'minorityInterest': 'minority_interest',
    'totalLiabilitiesAndTotalEquity': 'total_liabilities_and_total_equity',
    'totalInvestments': 'total_investments',
    'totalDebt': 'total_debt',
    'netDebt': 'net_debt',
    'link': 'link',
    'finalLink': 'final_link'
}

income_statement_normalized_names = {
    'date': 'date',
    'symbol': 'symbol',
    'reportedCurrency': 'reported_currency',
    'cik': 'cik',
    'fillingDate': 'filling_date',
    'acceptedDate': 'accepted_date',
    'calendarYear': 'calendar_year',
    'period': 'period',
    'revenue': 'revenue',
    'costOfRevenue': 'cost_of_revenue',
    'grossProfit': 'gross_profit',
    'grossProfitRatio': 'gross_profit_ratio',
    'researchAndDevelopmentExpenses': 'research_and_development_expenses',
    'generalAndAdministrativeExpenses': 'general_and_administrative_expenses',
    'sellingAndMarketingExpenses': 'selling_and_marketing_expenses',
    'sellingGeneralAndAdministrativeExpenses': 'selling_general_and_administrative_expenses',
    'otherExpenses': 'other_expenses',
    'operatingExpenses': 'operating_expenses',
    'costAndExpenses': 'cost_and_expenses',
    'interestIncome': 'interest_income',
    'interestExpense': 'interest_expense',
    'depreciationAndAmortization': 'depreciation_and_amortization',
    'ebitda': 'ebitda',
    'ebitdaratio': 'ebitda_ratio',
    'operatingIncome': 'operating_income',
    'operatingIncomeRatio': 'operating_income_ratio',
    'totalOtherIncomeExpensesNet': 'total_other_income_expenses_net',
    'incomeBeforeTax': 'income_before_tax',
    'incomeBeforeTaxRatio': 'income_before_tax_ratio',
    'incomeTaxExpense': 'income_tax_expense',
    'netIncome': 'net_income',
    'netIncomeRatio': 'net_income_ratio',
    'eps': 'eps',
    'epsdiluted': 'eps_diluted',
    'weightedAverageShsOut': 'weighted_average_shs_out',
    'weightedAverageShsOutDil': 'weighted_average_shs_out_dil',
    'link': 'link',
    'finalLink': 'final_link'
}

cashflow_statement_normalized_names = {
    'date': 'date',
    'symbol': 'symbol',
    'reportedCurrency': 'reported_currency',
    'cik': 'cik',
    'fillingDate': 'filling_date',
    'acceptedDate': 'accepted_date',
    'calendarYear': 'calendar_year',
    'period': 'period',
    'netIncome': 'net_income',
    'depreciationAndAmortization': 'depreciation_and_amortization',
    'deferredIncomeTax': 'deferred_income_tax',
    'stockBasedCompensation': 'stock_based_compensation',
    'changeInWorkingCapital': 'change_in_working_capital',
    'accountsReceivables': 'accounts_receivables',
    'inventory': 'inventory',
    'accountsPayables': 'accounts_payables',
    'otherWorkingCapital': 'other_working_capital',
    'otherNonCashItems': 'other_non_cash_items',
    'netCashProvidedByOperatingActivities': 'net_cash_provided_by_operating_activities',
    'investmentsInPropertyPlantAndEquipment': 'investments_in_property_plant_and_equipment',
    'acquisitionsNet': 'acquisitions_net',
    'purchasesOfInvestments': 'purchases_of_investments',
    'salesMaturitiesOfInvestments': 'sales_maturities_of_investments',
    'otherInvestingActivites': 'other_investing_activities',
    'netCashUsedForInvestingActivites': 'net_cash_used_for_investing_activities',
    'debtRepayment': 'debt_repayment',
    'commonStockIssued': 'common_stock_issued',
    'commonStockRepurchased': 'common_stock_repurchased',
    'dividendsPaid': 'dividends_paid',
    'otherFinancingActivites': 'other_financing_activities',
    'netCashUsedProvidedByFinancingActivities': 'net_cash_used_provided_by_financing_activities',
    'effectOfForexChangesOnCash': 'effect_of_forex_changes_on_cash',
    'netChangeInCash': 'net_change_in_cash',
    'cashAtEndOfPeriod': 'cash_at_end_of_period',
    'cashAtBeginningOfPeriod': 'cash_at_beginning_of_period',
    'operatingCashFlow': 'operating_cash_flow',
    'capitalExpenditure': 'capital_expenditure',
    'freeCashFlow': 'free_cash_flow',
    'link': 'link',
    'finalLink': 'final_link'
}


def normalize_names(df: pd.DataFrame, statement: str) -> pd.DataFrame:
    rename_map = {
        "bs": balance_sheet_normalized_names,
        "ic": income_statement_normalized_names,
        "cf": cashflow_statement_normalized_names,
    }

    df = df.rename(columns=rename_map[statement])
    df["date"] = pd.to_datetime(df["date"])
    df["filling_date"] = pd.to_datetime(df["filling_date"])
    df["accepted_date"] = pd.to_datetime(df["accepted_date"])
    df["calendar_year"] = pd.to_datetime(df["calendar_year"])
    return df