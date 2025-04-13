# CPU Load Generator

A lightweight CPU stress-testing tool written in Python 3. Simulates configurable CPU load for benchmarking, diagnostics, or CI environments.

## 📌 Features

* Generate custom CPU load (1%–100%)
* Control test duration (in seconds)
* Load specific number of CPU cores
* Clean interruption handling (Ctrl+C)

## ⚙️ Requirements

- Python 3.6 or newer
- Linux, Windows

## 🚀 Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/laspavel/cpu_load.git
cd cpu_load
chmod +x cpu_load.py
```

Python dependencies are only from the standard library, no installation of packages is required.


```bash
./cpu_load.py [-i INTERVAL] [-u UTILIZATION] [-c CPUS] [-v]
```

Parameters:

| Parameters         | Description                                           |  Default             |
| ------------------ | ----------------------------------------------------- |  --------------------|
| -i, --interval     | Duration in seconds to run the test                   |  30                  |
| -u, --utilization  | CPU load percentage per core                          |  50                  |
| -c, --cpus         | Number of CPU cores to load  (max = physical cores)   |  all available cores |
| -v, --version      | Show program version and exit	                       |                      |

## 🧩  Example Usage

```bash
./load_cpu.py -i 60 -u 90 -c 2   # Run for 60 seconds at 90% load on 2 CPU cores
```

## Build binary file

```bash
./build.sh
```

## 🧪 Testing the Load Script

If you prefer to run the load script directly on your host system:​

```bash
chmod +x load_cpu.sh
./load_cpu.py
```

Note: Ensure that Python 3 is installed on your system.​

## 📁 Project Structure
```plaintext
cpu_load/
├── cron/                   # Cron job configurations (if any)
├── src/                    # Source code for load generation
├── build.sh                # Script to build binary file
├── Dockerfile.build        # Docker image for build binary file
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