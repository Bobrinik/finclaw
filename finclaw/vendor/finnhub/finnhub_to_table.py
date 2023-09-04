FINNHUB_CANDLES_TO_OHCL_TABLE_MAP = {"c": "close", "h": "high", "l": "low", "o": "open", "t": "timestamp",
                                     "v": "volume"}

FINNHUB_COMPANY_NAME_TO_COMPANY_DESCRIPTION = {"country": "country", "currency": "currency", "exchange": "exchange",
                                               "finnhubIndustry": "sector", "ipo": "ipo",
                                               "marketCapitalization": "market_cap", "name": "name",
                                               "shareOutstanding": "share_outstanding", "ticker": "ticker"}

FINNHUB_DIVIDEND_TO_DIVIDEND_TABLE_MAP = {"symbol": "symbol",
                                          "date": "ex_date",
                                          "amount": "amount",
                                          "currency": "currency",
                                          "payDate": "payment_date",
                                          "declarationDate": "declared_date",
                                          "recordDate": "record_date",
                                          "adjustedAmount": "adjusted_amount"
                                          }

FINNHUB_INSIDER_TO_INSIDER_TABLE_MAP = {"symbol": "symbol",
                                        "change": "shares_traded",
                                        "share": "shares_owned",
                                        "transactionPrice": "price",
                                        "name": "insider_name",
                                        "filingDate": "filing_date",
                                        "transactionDate": "transaction_date",
                                        "transactionCode": "transaction_type"}

FINNHUB_OWNER_TO_INSTITUTIONAL_OWNERSHIP_TABLE_MAP = {"cik": "cik",
                                                      "name": "organization",
                                                      "noVoting": "no_voting",
                                                      "percentage": "portfolio_percentage",
                                                      "putCall": "put_call",
                                                      "share": "shares_owned",
                                                      "sharedVoting": "shared_voting",
                                                      "soleVoting": "sole_voting",
                                                      "value": "value",
                                                      "change": "shares_traded",
                                                      "reportDate": "report_date",
                                                      "cusip": "cusip",
                                                      "symbol": "symbol"}

FINNHUB_FUND_OWNERSHIP_TO_FUND_OWNERSHIP_TABLE_MAP = {"name": "fund_name",
                                                      "share": "shares_held",
                                                      "change": "shares_traded",
                                                      "portfolioPercent": "portfolio_percentage",
                                                      "filingDate": "filling_date",
                                                      "symbol": "symbol"}

FINNHUB_BALANCE_SHEET_TO_BALANCE_SHEET_TABLE = {'inventory': 'inventory',
                                                'cashShortTermInvestments': 'cash_short_term_investments',
                                                'tangibleBookValueperShare': 'tangible_book_value_per_share',
                                                'goodwill': 'goodwill',
                                                'otherReceivables': 'other_receivables',
                                                'insurancePolicyLiabilities': 'insurance_policy_liabilities',
                                                'otherInterestBearingLiabilities': 'other_interest_bearing_liabilities',
                                                'statement': 'statement',
                                                'cashDueFromBanks': 'cash_due_from_banks',
                                                'commonStock': 'common_stock',
                                                'sharesOutstanding': 'shares_outstanding',
                                                'intangiblesAssets': 'intangibles_assets',
                                                'minorityInterest': 'minority_interest',
                                                'totalDebt': 'total_debt',
                                                'otherCurrentliabilities': 'other_current_liabilities',
                                                'accountsReceivables': 'accounts_receivables',
                                                'otherLongTermAssets': 'other_long_term_assets',
                                                'cashEquivalents': 'cash_equivalents',
                                                'period': 'period',
                                                'additionalPaidInCapital': 'additional_paid_in_capital',
                                                'noteReceivableLongTerm': 'note_receivable_long_term',
                                                'cash': 'cash',
                                                'totalDeposits': 'total_deposits',
                                                'longTermDebt': 'long_term_debt',
                                                'accountsPayable': 'accounts_payable',
                                                'currentPortionLongTermDebt': 'current_portion_long_term_debt',
                                                'accruedLiability': 'accrued_liability',
                                                'accumulatedDepreciation': 'accumulated_depreciation',
                                                'netLoans': 'net_loans',
                                                'longTermInvestments': 'long_term_investments',
                                                'deferredIncomeTax': 'deferred_income_tax',
                                                'netDebt': 'net_debt',
                                                'otherEquity': 'other_equity',
                                                'otherLiabilities': 'other_liabilities',
                                                'bankInvestments': 'bank_investments',
                                                'unrealizedProfitLossSecurity': 'unrealized_profit_loss_security',
                                                'customerLiabilityAcceptances': 'customer_liability_acceptances',
                                                'totalEquity': 'total_equity',
                                                'retainedEarnings': 'retained_earnings',
                                                'totalReceivables': 'total_receivables',
                                                'preferredSharesOutstanding': 'preferred_shares_outstanding',
                                                'insuranceReceivables': 'insurance_receivables',
                                                'liabilitiesShareholdersEquity': 'liabilities_shareholders_equity',
                                                'totalAssets': 'total_assets',
                                                'shortTermDebt': 'short_term_debt',
                                                'currentLiabilities': 'current_liabilities',
                                                'totalLiabilities': 'total_liabilities',
                                                'symbol': 'symbol',
                                                'deferredPolicyAcquisitionCosts': 'deferred_policy_acquisition_costs',
                                                'currentAssets': 'current_assets',
                                                'otherCurrentAssets': 'other_current_assets',
                                                'shortTermInvestments': 'short_term_investments',
                                                'otherAssets': 'other_assets',
                                                'treasuryStock': 'treasury_stock',
                                                'propertyPlantEquipment': 'property_plant_equipment'}

FINNHUB_INCOME_STATEMENT_TO_INCOME_STATEMENT_TABLE = {'bankNonInterestIncome': 'bank_non_interest_income',
                                                      'researchDevelopment': 'research_development',
                                                      'operationsMaintenance': 'operations_maintenance',
                                                      'revenue': 'revenue',
                                                      'equityEarningsAffiliates': 'equity_earnings_affiliates',
                                                      'sgaExpense': 'sga_expense',
                                                      'grossIncome': 'gross_income',
                                                      'minorityInterest': 'minority_interest',
                                                      'purchasedFuelPowerGas': 'purchased_fuel_power_gas',
                                                      'interestExpense': 'interest_expense',
                                                      'netIncome': 'net_income',
                                                      'period': 'period',
                                                      'netInterestIncome': 'net_interest_income',
                                                      'bankInterestIncome': 'bank_interest_income',
                                                      'totalOperatingExpense': 'total_operating_expense',
                                                      'otherRevenue': 'other_revenue',
                                                      'interestIncomeExpense': 'interest_income_expense',
                                                      'benefitsClaimsLossAdjustment': 'benefits_claims_loss_adjustment',
                                                      'dilutedEPS': 'diluted_e_p_s',
                                                      'costOfGoodsSold': 'cost_of_goods_sold',
                                                      'gainLossOnDispositionOfAssets': 'gain_loss_on_disposition_of_assets',
                                                      'provisionforIncomeTaxes': 'provision_for_income_taxes',
                                                      'grossPremiumsEarned': 'gross_premiums_earned',
                                                      'otherOperatingExpensesTotal': 'other_operating_expenses_total',
                                                      'nonRecurringItems': 'non_recurring_items',
                                                      'depreciationAmortization': 'depreciation_amortization',
                                                      'pretaxIncome': 'pretax_income',
                                                      'totalOtherIncomeExpenseNet': 'total_other_income_expense_net',
                                                      'ebit': 'ebit',
                                                      'bankNonInterestExpense': 'bank_non_interest_expense',
                                                      'loanLossProvision': 'loan_loss_provision',
                                                      'netIncomeAfterTaxes': 'net_income_after_taxes',
                                                      'dilutedAverageSharesOutstanding': 'diluted_average_shares_outstanding',
                                                      'symbol': 'symbol',
                                                      'netInterestIncAfterLoanLossProv': 'net_interest_inc_after_loan_loss_prov'}

FINNHUB_CASHFLOW_STATEMENT_TO_CASHFLOW_STATEMENT_TABLE = {'cashDividendsPaid': 'cash_dividends_paid',
                                                          'changeinCash': 'change_in_cash',
                                                          'fcf': 'fcf',
                                                          'netInvestingCashFlow': 'net_investing_cash_flow',
                                                          'cashTaxesPaid': 'cash_taxes_paid',
                                                          'changesinWorkingCapital': 'changes_in_working_capital',
                                                          'netCashFinancingActivities': 'net_cash_financing_activities',
                                                          'depreciationAmortization': 'depreciation_amortization',
                                                          'deferredTaxesInvestmentTaxCredit': 'deferred_taxes_investment_tax_credit',
                                                          'capex': 'capex',
                                                          'otherInvestingCashFlowItemsTotal': 'other_investing_cash_flow_items_total',
                                                          'period': 'period',
                                                          'issuanceReductionCapitalStock': 'issuance_reduction_capital_stock',
                                                          'cashInterestPaid': 'cash_interest_paid',
                                                          'netIncomeStartingLine': 'net_income_starting_line',
                                                          'symbol': 'symbol',
                                                          'netOperatingCashFlow': 'net_operating_cash_flow',
                                                          'otherFundsFinancingItems': 'other_funds_financing_items',
                                                          'foreignExchangeEffects': 'foreign_exchange_effects',
                                                          'otherFundsNonCashItems': 'other_funds_non_cash_items',
                                                          'issuanceReductionDebtNet': 'issuance_reduction_debt_net',
                                                          'cashNet': 'cash_net'}

FINNHUB_SPLIT_TO_SPLIT_TABLE = {'date': "split_date",
                                'fromFactor': "from_factor",
                                'symbol': "symbol",
                                'toFactor': "to_factor"}

FINNHUB_OWNER_TO_OWNER_TABLE = {'change': "shares_traded",
                                'filingDate': "filing_date",
                                'name': "name",
                                'share': "shares_owned",
                                "symbol": "symbol"}
