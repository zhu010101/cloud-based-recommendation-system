# Cloud-Based Recommendation System for E-commerce
## Project Overview
This project implements a cloud-based recommendation system for e-commerce using AWS services to enhance customer experience through personalized shopping recommendations.

## Team Members
- Siyuan Zhu
- Michelle Dong
- Vidhi Mansharamani
- Ziyu Ou

## Executive Summary
- Objective: Enhance customer experience with personalized shopping journeys.
- Problem: Current systems struggle with scalability, data complexity, and processing power.
- Solution: Cloud-based Recommendation System using AWS services (S3, DynamoDB, EC2, API Gateway, Lambda, VPC).

## Data Description
- Source:User-generated content from Amazon.com's 'Grocery_and_Gourmet_Food' category.
  https://amazon-reviews-2023.github.io/index.html
- Size: 5.97GB JSON (3.7GB CSV), 14,318,520 reviews.
- Metrics: Star ratings, review texts, images, ASINs, customer IDs.
- Sample Size for Analysis: 5,000,000 reviews.

## Cloud Architecture & Security
### Recommendation Algorithm
- Framework: Flask application using Singular Value Decomposition (SVD) for collaborative filtering.
- Data Storage: AWS DynamoDB.
- Data Processing: pandas, Surprise library.
- API Endpoint: recommend to serve personalized recommendations.
### Service Delivery
- Frontend: AWS Lambda functions and API Gateway.
- Security: HTTPS endpoints to avoid mixed content errors.
- VPC: Configured for secure and isolated environment across two Availability Zones.
### Security Configuration
- Components: Security Groups, S3 bucket policies, Network ACLs.
- Access Control: Strictly controlled to allow only necessary traffic.
### Cost Analysis
- Comparison: AWS vs. Google Cloud.
- Findings: AWS offers more cost-effective solutions for database services and competitive storage costs. GCP is cheaper for networking.
- Optimizations: Reserved Instances, lifecycle policies, VPC Endpoints, scaling resources, and efficient database use.
## Trials and Attempts
We initially planned to use Amazon Personalize for streamlined recommendation generation, but IAM role constraints prevented us from attaching necessary policies. We then tried Amazon SageMaker's Factorization Machines algorithm, successfully training the model but facing registration issues. Ultimately, we deployed the system on an EC2 instance, which required more manual setup but allowed us to deliver personalized recommendations. Budget constraints quickly arose with Amazon SageMaker, prompting us to continue on an EC2 instance with minimal budget constraints on a separate student account. This experience underscored the importance of careful budget management in future projects. Detailed descriptions of these efforts are provided in the final report uploaded in the main repository.
## Implementation and Demo
<img width="450" alt="image" src="https://github.com/user-attachments/assets/8977add2-93d9-437a-9672-db5f845a2634">
<img width="450" alt="image" src="https://github.com/user-attachments/assets/80cc81da-5a00-4cfc-a150-418ddf1f9962">

## Conclusion
The cloud-based Recommendation System aims to improve the customer shopping experience while providing businesses with actionable insights for optimizing their offerings.
