az functionapp config storage-config --name script-mensajeria-osa --resource-group Mensajeria --storage-account-name mensajeria --container-name wwwroot


az functionapp config appsettings list --name script-mensajeria-osa --resource-group Mensajeria


az storage blob list --container-name wwwroot --connection-string z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==
az storage blob list --account-key z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g== --account-name mensajeria --container-name /site/wwwroot/TimerTrigger1



DefaultEndpointsProtocol=https;AccountName=mensajeria;AccountKey=z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==;EndpointSuffix=core.windows.net

echo DefaultEndpointsProtocol=https;AccountName=mensajeria;AccountKey=z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==;EndpointSuffix=core.windows.net | awk -F/ '{print $3}'
echo "DefaultEndpointsProtocol=https;AccountName=mensajeria;AccountKey=z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==;EndpointSuffix=core.windows.net" | awk -F/ '{print $3}'

[
  {
    "name": "APPINSIGHTS_INSTRUMENTATIONKEY",
    "slotSetting": false,
    "value": "22b1c315-e1a9-4d4d-8af6-678c1cd04e60"
  },
  {
    "name": "APPLICATIONINSIGHTS_CONNECTION_STRING",
    "slotSetting": false,
    "value": "InstrumentationKey=22b1c315-e1a9-4d4d-8af6-678c1cd04e60;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/"
  },
  {
    "name": "AzureWebJobsStorage",
    "slotSetting": false,
    "value": "DefaultEndpointsProtocol=https;AccountName=mensajeria;AccountKey=z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==;EndpointSuffix=core.windows.net"
  },
  {
    "name": "FUNCTIONS_EXTENSION_VERSION",
    "slotSetting": false,
    "value": "~4"
  },
  {
    "name": "FUNCTIONS_WORKER_RUNTIME",
    "slotSetting": false,
    "value": "python"
  },
  {
    "name": "token_api",
    "slotSetting": false,
    "value": "5743813753:AAFuPL5KTJeOZLC1UpL5CCn2Ggv-hZbZSi4"
  },
  {
    "name": "WEBSITE_CONTENTAZUREFILECONNECTIONSTRING",
    "slotSetting": false,
    "value": "DefaultEndpointsProtocol=https;AccountName=mensajeria;AccountKey=z7eFwTdluW5XeHTngKoauE5IVQ82uln2AfgU7G5cHCSZONBSyYXevZjrLmqa5bT+7xYiIslLzxN3+ASteuvh2g==;EndpointSuffix=core.windows.net"
  },
  {
    "name": "WEBSITE_CONTENTSHARE",
    "slotSetting": false,
    "value": "script-mensajeria-osa80d2"
  }
]



az functionapp config set --name script-mensajeria-osa --resource-group Mensajeria --linux-fx-version "PYTHON|3.9" --app-settings "WEBSITES_ENABLE_APP_SERVICE_STORAGE=false"





az functionapp deployment source config-zip --resource-group Mensajeria --name script-mensajeria-osa --src <zip-file-path>
