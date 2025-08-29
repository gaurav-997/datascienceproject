# create all files and dir using a  template.py file
# create common functionality like logging , reading and loading yaml files e.t.c

# workflows means build ML pipelines [ Data we get to test our validation so we follow below steps ]
ML Workflow Stages

When building an ML pipeline, we typically follow these steps:

1. Data Ingestion – Read raw data from a source (e.g., database, API, CSV, cloud storage).
2. Data Validation – Validate input data (check schema, datatypes, missing values, anomalies) using schema.yaml.
3. Data Transformation – Clean, preprocess, and transform data into a format suitable for Model training , feature engineering, encoding, scaling
4. Model Training – Train ML/DL models using transformed data and specified hyperparameters from params.yaml.
5. Model Evaluation – Evaluate trained model on test/validation data (accuracy, F1-score, etc.) and compare with baseline.

# Steps to Implement Each Workflow in Code

# For each stage of the pipeline (Ingestion → Validation → Transformation → Training → Evaluation), we generally follow:

1. Update config.yaml – Define configuration Input values (data source paths, file names, model save paths, etc.) Holds pipeline-wide configurations.
2. Update schema.yaml – Define schema rules for validation (column names, datatypes, constraints).
3. Update params.yaml – Store model/processing parameters (batch size, learning rate, epochs,learning rate, test/train split, n_estimators, etc.).
4. Update the Entity Layer – Create entities (dataclasses/objects) to hold configurations of config.yaml in structured form ( means data type of values of config.yaml ).
5. Update the Configuration Manager (in src/config/) – Write logic to read from YAML files and pass configs to components.
here we will interlink the config.yaml and entity (data types )  and use this in component 
6. Update the Components – Implement actual business logic for each step (e.g., ingestion component, validation component, etc.).
Implement reusable modules:

data_ingestion.py
data_validation.py
data_transformation.py
model_trainer.py
model_evaluation.py
7. Update the Pipeline – Define pipeline classes (or orchestrators) that sequentially call components.
8. Update main.py – Entry point to trigger the pipeline end-to-end (Ingestion → Validation → Transformation → Training → Evaluation).


echo "# datascienceproject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/gaurav-997/datascienceproject.git
git push -u origin main