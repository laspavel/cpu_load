# CPU Load Generator

cpu_load is a lightweight tool designed to simulate CPU load for testing and benchmarking purposes. It utilizes Python and Bash scripts, encapsulated within a Docker container, to generate controlled CPU stress.​

## 📌 Features

* Simulates CPU load using Python-based computations​
* Containerized with Docker for easy deployment​
* Configurable parameters to adjust load intensity and duration​
* Suitable for performance testing, benchmarking, and system behavior analysis​

## ⚙️ Requirements

* Docker installed on the host system​
* Optional: Docker Compose for simplified orchestration​

## 🚀 Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/laspavel/cpu_load.git
cd cpu_load
```

### Build the Docker Image

```bash
./BuildImage.sh
```

### Run the Container

```bash
docker-compose up -d
```

This will start the container and begin generating CPU load based on the default configuration.​

### Customize Load Parameters

You can modify the docker-compose.yml file to adjust environment variables that control the load intensity and duration. For example:​

```yaml
environment:
  - LOAD_DURATION=60  # Duration in seconds
  - LOAD_INTENSITY=80 # Percentage of CPU load
```

After making changes, restart the container:​

```bash
docker-compose down
docker-compose up -d
```

## 🧪 Testing the Load Script

If you prefer to run the load script directly on your host system:​

```bash
chmod +x cpu_load.sh
./cpu_load.sh
```

Note: Ensure that Python 3 is installed on your system.​

## 📁 Project Structure
```plaintext
cpu_load/
├── cron/                   # Cron job configurations (if any)
├── src/                    # Source code for load generation
├── BuildImage.sh           # Script to build the Docker image
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── cpu_load.sh             # Shell script to initiate CPU load
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## 📄 License
MIT License.​

## 🤝 Contributions

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact

Author: [laspavel](https://github.com/laspavel)

Feel free to reach out with questions or ideas.

---