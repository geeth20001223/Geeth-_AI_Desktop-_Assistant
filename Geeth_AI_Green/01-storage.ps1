$rg = 'arm-introduction-01'
New-AzResourceGroup -Name $rg -Location southeastasia -Force
New-AzResourceGroupDeployment `
    -Name 'new-storage' `
    -ResourceGroupName $rg `
    -TemplateFile '01-storage.json'