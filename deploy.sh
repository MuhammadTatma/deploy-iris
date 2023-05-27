gcloud builds submit --tag gcr.io/mldeployment-387918/iris --project=mldeployment-387918

gcloud run deploy irisapi --image gcr.io/mldeployment-387918/iris /
 --platform managed --region asia-southeast2 /
 --allow-unauthenticated --project=mldeployment-387918