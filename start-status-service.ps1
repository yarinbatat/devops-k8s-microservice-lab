# נווט לתיקיית הפרויקט
Set-Location "C:\Users\UBS\Documents\Devops project\devops-k8s-microservice-lab"

Write-Host "מריץ פורוורד מ-service/status-service ל-localhost:5000 ..."
Write-Host "ניתן כעת לשלוח בקשות לכתובת http://localhost:5000/status"
Write-Host "כדי לצאת לחץ Ctrl+C"

# ביצוע הפורוורד של הפורטים
kubectl port-forward service/status-service 5000:80
