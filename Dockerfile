# Use Amazon Linux 2 base image with Python 3.8
FROM public.ecr.aws/lambda/python:3.8

# Set working directory in the container
WORKDIR /var/task

# Install Miniconda
RUN yum -y install wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Add Miniconda to PATH
ENV PATH="/miniconda/bin:$PATH"

# Copy Conda environment YAML file and install dependencies
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean --all -y

# Set the Conda environment as default
ENV PATH="/miniconda/envs/movie-hit-predictor/bin:$PATH"

# Copy the model and Lambda function code
COPY movie_hit_predictor.pkl .
COPY lambda_function.py .

# Command for Lambda to run the handler
CMD ["lambda_function.lambda_handler"]