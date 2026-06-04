# Use Python 3.11 slim image
FROM python:3.11-slim

# Install system dependencies required for compiling dlib, face_recognition, and running OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    gfortran \
    git \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    libx11-dev \
    libxext-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file and install python packages
COPY "PROJECT DJ/SecureVote/Secure/project/SecureVote/requirements.txt" .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY "PROJECT DJ/SecureVote/Secure/project/SecureVote/" .

# Expose port 8080 (default for many cloud run providers) or 7860 (HuggingFace)
EXPOSE 8080
EXPOSE 7860

# Run using gunicorn, binding to the PORT environment variable if set, defaulting to 8080
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} --timeout 120 app:app"]
