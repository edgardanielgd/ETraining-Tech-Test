# E-training test
--- 
This project aims to create a full data flow where data is extracted and loaded from a set of CSV files to a GCP MySQL instance.

## Architecture
---
First than all, we will plan the architecture to follow for this project, as follows:


## Tools Installation
---
1. Terraform

We'll use Terraform as the main tool to handle our architecture with code

```
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update

sudo apt-get install terraform
```

2. Apache Spark (PySpark)

Having the base infrastructure to deploy this project, the next step is to create a dataflow by means of PySpark, which allows us to create efficient and reliable ETLs by means of Python, making us able to consume and load from and to different source types, among them, CSV files and MySQL databases. 