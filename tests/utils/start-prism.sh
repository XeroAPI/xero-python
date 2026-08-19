#!/bin/bash
specRef=${1:?pass an immutable Xero-OpenAPI commit SHA}
if ! [[ "$specRef" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Xero-OpenAPI ref must be a full commit SHA" >&2
  exit 2
fi

specUrl="https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/$specRef"

# Every mock is backgrounded so this script returns once they are all spawned.
# The caller is responsible for waiting until ports 4010-4018 accept connections.
prism mock "$specUrl/xero_accounting.yaml" --host 127.0.0.1 --port 4010 &
prism mock "$specUrl/xero-app-store.yaml" --host 127.0.0.1 --port 4011 &
prism mock "$specUrl/xero_assets.yaml" --host 127.0.0.1 --port 4012 &
prism mock "$specUrl/xero_bankfeeds.yaml" --host 127.0.0.1 --port 4013 &
prism mock "$specUrl/xero-finance.yaml" --host 127.0.0.1 --port 4014 &
prism mock "$specUrl/xero-payroll-uk.yaml" --host 127.0.0.1 --port 4015 &
prism mock "$specUrl/xero-payroll-nz.yaml" --host 127.0.0.1 --port 4016 &
prism mock "$specUrl/xero-payroll-au.yaml" --host 127.0.0.1 --port 4017 &
prism mock "$specUrl/xero-projects.yaml" --host 127.0.0.1 --port 4018 &
