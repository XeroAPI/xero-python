#!/bin/bash
branchName=${1:-"master"}

prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero_accounting.yaml --host 127.0.0.1 --port 4010 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-app-store.yaml --host 127.0.0.1 --port 4011 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero_assets.yaml --host 127.0.0.1 --port 4012 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero_bankfeeds.yaml --host 127.0.0.1 --port 4013 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-finance.yaml --host 127.0.0.1 --port 4014 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-payroll-uk.yaml --host 127.0.0.1 --port 4015 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-payroll-nz.yaml --host 127.0.0.1 --port 4016 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-payroll-au.yaml --host 127.0.0.1 --port 4017 &
prism mock https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/refs/heads/$branchName/xero-projects.yaml --host 127.0.0.1 --port 4018
