# Use AWS-provided Lambda base image for Python 3.8
FROM public.ecr.aws/lambda/python:3.11

# Copy the Conda environment configuration file
COPY environment.yml ${LAMBDA_TASK_ROOT}

RUN pip install -r environment.yml

# Copy application code
COPY app.py ${LAMBDA_TASK_ROOT}

# Copy the ML model to the /opt/model directory
COPY movie_hit_predictor.pkl /opt/model/movie_hit_predictor.pkl

# Command for AWS Lambda runtime
CMD ["lambda_function.lambda_handler"]